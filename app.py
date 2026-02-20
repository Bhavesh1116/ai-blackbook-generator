"""
AI Blackbook Generator - Main Application
==========================================

This is the main Flask application that provides API endpoints for:
1. Generating AI-powered academic content using Google Gemini
2. Creating professionally formatted Word documents
3. Downloading generated documents

Author: AI Blackbook Generator Team
Version: 1.0.0
"""

# ============================================
# IMPORTS
# ============================================

# Flask framework imports
from flask import Flask, jsonify, request, send_file, render_template
from flask_cors import CORS

# Service imports (our custom modules)
from services.ai_client import gemini_client
from services.doc_generator import document_generator
from utils.helpers import format_api_response, validate_topic
from utils.logger import logger

# Standard library imports
import os


# ============================================
# APPLICATION SETUP
# ============================================

# Create Flask application instance
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
# This allows the API to be accessed from web browsers
CORS(app)

# Application configuration
app.config['DEBUG'] = True              # Enable debug mode (disable in production)
app.config['JSON_SORT_KEYS'] = False    # Keep JSON keys in original order


# ============================================
# BASIC ENDPOINTS
# ============================================

@app.route('/')
def home():
    """
    Home endpoint - Serves the web UI
    
    Returns:
        HTML: Web interface for the blackbook generator
    """
    logger.info("Home page accessed")
    return render_template('index.html')


@app.route('/api')
def api_info():
    """
    API information endpoint - Returns API details
    
    Returns:
        JSON: Server status and API information
    """
    logger.info("API info endpoint accessed")
    
    return jsonify({
        "status": "running",
        "message": "AI Blackbook Generator API is active",
        "version": "2.0.0",
        "endpoints": {
            "web_ui": "GET /",
            "api_info": "GET /api",
            "generate": "POST /generate",
            "download": "GET /download/<file_id>",
            "health": "GET /health"
        }
    })


@app.route('/health')
def health_check():
    """
    Health check endpoint - Verifies server and services are working
    
    Returns:
        JSON: Health status of server and connected services
    """
    logger.info("Health check requested")
    
    # Check if Gemini AI client is initialized
    gemini_status = "connected" if gemini_client else "not configured"
    
    return jsonify({
        "status": "healthy",
        "service": "AI Blackbook Generator",
        "gemini_api": gemini_status,
        "timestamp": logger.get_timestamp()
    })


# ============================================
# MAIN GENERATION ENDPOINT
# ============================================

@app.route('/generate', methods=['POST'])
def generate_blackbook():
    """
    Main endpoint: Generate AI content and create Word document
    
    This endpoint:
    1. Receives a topic from the client
    2. Generates academic content using Gemini AI
    3. Creates a professionally formatted Word document
    4. Returns file information and download link
    
    Request Body:
        {
            "topic": "Your academic topic here"
        }
    
    Returns:
        JSON: Success response with file info or error details
    """
    try:
        logger.info("=" * 60)
        logger.info("NEW GENERATION REQUEST")
        logger.info("=" * 60)
        
        # ----------------------------------------
        # STEP 1: Validate Gemini API is configured
        # ----------------------------------------
        if not gemini_client:
            logger.error("Gemini API not configured")
            return jsonify(format_api_response(
                success=False,
                error="Gemini API is not configured. Please add GEMINI_API_KEY to .env file",
                error_code="API_NOT_CONFIGURED"
            )), 500
        
        # ----------------------------------------
        # STEP 2: Get and validate request data
        # ----------------------------------------
        request_data = request.get_json()
        
        # Check if request body exists
        if not request_data:
            logger.warning("Request received without body")
            return jsonify(format_api_response(
                success=False,
                error="Request body is required",
                error_code="MISSING_BODY"
            )), 400
        
        # Check if topic field exists
        if 'topic' not in request_data:
            logger.warning("Request missing 'topic' field")
            return jsonify(format_api_response(
                success=False,
                error="Missing 'topic' field in request body",
                error_code="MISSING_TOPIC"
            )), 400
        
        # Get and clean the topic
        topic = request_data.get('topic', '').strip()
        
        # Validate topic using helper function
        is_valid, error_message, error_code = validate_topic(topic)
        if not is_valid:
            logger.warning(f"Invalid topic: {error_message}")
            return jsonify(format_api_response(
                success=False,
                error=error_message,
                error_code=error_code
            )), 400
        
        logger.info(f"Topic received: {topic}")
        
        # ----------------------------------------
        # STEP 3: Generate AI content
        # ----------------------------------------
        logger.info("Step 1/2: Generating AI content with Gemini...")
        
        ai_result = gemini_client.generate_academic_content(topic)
        
        # Check if AI generation was successful
        if not ai_result.get('success'):
            error_msg = ai_result.get('error', 'Unknown error')
            logger.error(f"AI generation failed: {error_msg}")
            return jsonify(format_api_response(
                success=False,
                error=error_msg,
                error_code="AI_GENERATION_FAILED",
                topic=topic
            )), 500
        
        logger.success("AI content generated successfully")
        
        # ----------------------------------------
        # STEP 4: Extract and validate sections
        # ----------------------------------------
        logger.info("Extracting content sections...")
        
        sections = ai_result.get('content', {})
        
        # Remove full_text (we only need individual sections)
        if 'full_text' in sections:
            del sections['full_text']
        
        # Verify we have sections
        if not sections:
            logger.error("No sections found in AI content")
            return jsonify(format_api_response(
                success=False,
                error="AI generated content but no sections were found",
                error_code="NO_SECTIONS_FOUND",
                topic=topic
            )), 500
        
        logger.info(f"Found {len(sections)} sections: {', '.join(sections.keys())}")
        
        # ----------------------------------------
        # STEP 5: Create Word document
        # ----------------------------------------
        logger.info("Step 2/2: Creating Word document...")
        
        doc_result = document_generator.create_blackbook(
            title=topic,
            sections_dict=sections
        )
        
        # Check if document creation was successful
        if not doc_result.get('success'):
            error_msg = doc_result.get('error', 'Unknown error')
            logger.error(f"Document creation failed: {error_msg}")
            return jsonify(format_api_response(
                success=False,
                error=error_msg,
                error_code="DOCUMENT_CREATION_FAILED",
                topic=topic
            )), 500
        
        logger.success(f"Document created: {doc_result['filename']}")
        
        # ----------------------------------------
        # STEP 6: Prepare response
        # ----------------------------------------
        
        # Extract file information
        filename = doc_result['filename']
        file_id = filename.rsplit('_', 1)[-1].replace('.docx', '')
        
        # Build response object
        response_data = {
            "success": True,
            "message": "Document generated successfully",
            "topic": topic,
            "file_id": file_id,
            "filename": filename,
            "download_link": f"/download/{file_id}",
            "download_url": f"http://localhost:5000/download/{file_id}",
            "download_link_full": f"/api/download/{filename}",
            "download_url_full": f"http://localhost:5000/api/download/{filename}",
            "document_info": {
                "file_size": doc_result['file_size'],
                "file_size_kb": round(doc_result['file_size'] / 1024, 2),
                "sections_count": doc_result['sections_count'],
                "sections": list(sections.keys())
            },
            "ai_metadata": {
                "model": ai_result.get('metadata', {}).get('model', 'gemini-pro'),
                "word_count": ai_result.get('metadata', {}).get('word_count', 0),
                "character_count": ai_result.get('metadata', {}).get('character_count', 0)
            }
        }
        
        logger.success(f"Generation complete! File ID: {file_id}")
        logger.info("=" * 60)
        
        return jsonify(response_data), 200
        
    except Exception as e:
        # Catch any unexpected errors
        logger.error(f"Unexpected error in generate endpoint: {str(e)}")
        
        return jsonify(format_api_response(
            success=False,
            error=f"Server error: {str(e)}",
            error_code="INTERNAL_SERVER_ERROR"
        )), 500


# ============================================
# DOWNLOAD ENDPOINTS
# ============================================

@app.route('/download/<file_id>')
def download_by_file_id(file_id):
    """
    Download a document by its file ID (Recommended method)
    
    This is the preferred download method as it uses short, clean URLs.
    
    Args:
        file_id: The UUID identifier (e.g., "a1b2c3d4")
        
    Returns:
        File: Word document with proper headers
        JSON: Error message if file not found
    """
    try:
        logger.info(f"Download requested for file ID: {file_id}")
        
        # ----------------------------------------
        # STEP 1: Validate file ID format
        # ----------------------------------------
        
        # Check if file_id is not empty
        if not file_id:
            logger.warning("Empty file ID provided")
            return jsonify(format_api_response(
                success=False,
                error="File ID cannot be empty",
                error_code="INVALID_FILE_ID"
            )), 400
        
        # Check if file_id contains only valid characters
        # Valid: alphanumeric and hyphens/underscores
        if not all(c.isalnum() or c in '-_' for c in file_id):
            logger.warning(f"Invalid file ID format: {file_id}")
            return jsonify(format_api_response(
                success=False,
                error="Invalid file ID format. Use only letters, numbers, hyphens, and underscores",
                error_code="INVALID_FILE_ID"
            )), 400
        
        # ----------------------------------------
        # STEP 2: Search for file in outputs folder
        # ----------------------------------------
        
        outputs_directory = 'outputs'
        matching_files = []
        
        # Check if outputs directory exists
        if os.path.exists(outputs_directory):
            # Search for files containing this ID
            for filename in os.listdir(outputs_directory):
                if filename.endswith('.docx') and file_id in filename:
                    matching_files.append(filename)
        
        # Check if we found any matching files
        if not matching_files:
            logger.warning(f"No file found for ID: {file_id}")
            return jsonify(format_api_response(
                success=False,
                error=f"No document found with file ID: {file_id}",
                error_code="FILE_NOT_FOUND",
                file_id=file_id
            )), 404
        
        # ----------------------------------------
        # STEP 3: Send file to client
        # ----------------------------------------
        
        # Use the first matching file (should only be one)
        filename = matching_files[0]
        filepath = os.path.join(outputs_directory, filename)
        
        logger.info(f"Sending file: {filename}")
        
        # Send file with proper headers
        return send_file(
            filepath,
            as_attachment=True,                    # Force download
            download_name=filename,                # Filename for download
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
    except Exception as e:
        logger.error(f"Error downloading file: {str(e)}")
        return jsonify(format_api_response(
            success=False,
            error=f"Download failed: {str(e)}",
            error_code="DOWNLOAD_ERROR"
        )), 500


@app.route('/api/download/<filename>')
def download_by_filename(filename):
    """
    Download a document by full filename (Legacy method)
    
    This method is kept for backward compatibility.
    Use /download/<file_id> for new implementations.
    
    Args:
        filename: Full filename including .docx extension
        
    Returns:
        File: Word document with proper headers
        JSON: Error message if file not found
    """
    try:
        logger.info(f"Download requested for filename: {filename}")
        
        # ----------------------------------------
        # STEP 1: Validate filename
        # ----------------------------------------
        
        # Check if filename is provided
        if not filename:
            logger.warning("Empty filename provided")
            return jsonify(format_api_response(
                success=False,
                error="Filename cannot be empty",
                error_code="INVALID_FILENAME"
            )), 400
        
        # Check if filename has .docx extension
        if not filename.endswith('.docx'):
            logger.warning(f"Invalid filename extension: {filename}")
            return jsonify(format_api_response(
                success=False,
                error="Invalid filename. Must be a .docx file",
                error_code="INVALID_FILENAME"
            )), 400
        
        # ----------------------------------------
        # STEP 2: Sanitize and locate file
        # ----------------------------------------
        
        # Prevent directory traversal attacks
        # This ensures filename doesn't contain path separators
        filename = os.path.basename(filename)
        
        # Build full file path
        filepath = os.path.join('outputs', filename)
        
        # Check if file exists
        if not os.path.exists(filepath):
            logger.warning(f"File not found: {filename}")
            return jsonify(format_api_response(
                success=False,
                error=f"File not found: {filename}",
                error_code="FILE_NOT_FOUND",
                filename=filename
            )), 404
        
        # Verify it's actually a file (not a directory)
        if not os.path.isfile(filepath):
            logger.error(f"Path is not a file: {filepath}")
            return jsonify(format_api_response(
                success=False,
                error="Invalid file path",
                error_code="INVALID_PATH"
            )), 400
        
        # ----------------------------------------
        # STEP 3: Send file to client
        # ----------------------------------------
        
        # Log file size for monitoring
        file_size = os.path.getsize(filepath)
        logger.info(f"Sending file: {filename} ({file_size} bytes)")
        
        # Send file with proper headers
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
    except Exception as e:
        logger.error(f"Error downloading file: {str(e)}")
        return jsonify(format_api_response(
            success=False,
            error=f"Download failed: {str(e)}",
            error_code="DOWNLOAD_ERROR"
        )), 500


# ============================================
# ADDITIONAL API ENDPOINTS
# ============================================

@app.route('/api/generate', methods=['POST'])
def generate_content_only():
    """
    Generate AI content only (without creating document)
    
    This endpoint only generates the AI content and returns it as JSON.
    Use /generate endpoint to also create a Word document.
    
    Returns:
        JSON: Generated content sections
    """
    try:
        # Check if Gemini is configured
        if not gemini_client:
            return jsonify(format_api_response(
                success=False,
                error="Gemini API is not configured",
                error_code="API_NOT_CONFIGURED"
            )), 500
        
        # Get request data
        request_data = request.get_json()
        
        if not request_data or 'topic' not in request_data:
            return jsonify(format_api_response(
                success=False,
                error="Missing 'topic' in request body",
                error_code="MISSING_TOPIC"
            )), 400
        
        topic = request_data.get('topic', '').strip()
        
        # Validate topic
        is_valid, error_message, error_code = validate_topic(topic)
        if not is_valid:
            return jsonify(format_api_response(
                success=False,
                error=error_message,
                error_code=error_code
            )), 400
        
        logger.info(f"Generating content for: {topic}")
        
        # Generate content
        result = gemini_client.generate_academic_content(topic)
        
        if result['success']:
            logger.success("Content generated successfully")
            return jsonify(result), 200
        else:
            logger.error(f"Content generation failed: {result.get('error')}")
            return jsonify(result), 500
            
    except Exception as e:
        logger.error(f"Error in generate content endpoint: {str(e)}")
        return jsonify(format_api_response(
            success=False,
            error=f"Server error: {str(e)}",
            error_code="INTERNAL_SERVER_ERROR"
        )), 500


@app.route('/api/create-document', methods=['POST'])
def create_document_from_content():
    """
    Create a Word document from provided content
    
    This endpoint creates a document from content you provide,
    without using AI generation.
    
    Request Body:
        {
            "title": "Document Title",
            "sections": {
                "abstract": "content...",
                "introduction": "content...",
                ...
            }
        }
    
    Returns:
        JSON: Document information and download link
    """
    try:
        # Get request data
        request_data = request.get_json()
        
        # Validate request
        if not request_data or 'title' not in request_data or 'sections' not in request_data:
            return jsonify(format_api_response(
                success=False,
                error="Missing 'title' or 'sections' in request body",
                error_code="MISSING_FIELDS"
            )), 400
        
        title = request_data.get('title', '').strip()
        sections = request_data.get('sections', {})
        
        # Validate title
        if not title:
            return jsonify(format_api_response(
                success=False,
                error="Title cannot be empty",
                error_code="EMPTY_TITLE"
            )), 400
        
        # Validate sections
        if not sections or not isinstance(sections, dict):
            return jsonify(format_api_response(
                success=False,
                error="Sections must be a non-empty dictionary",
                error_code="INVALID_SECTIONS"
            )), 400
        
        logger.info(f"Creating document: {title}")
        
        # Create document
        result = document_generator.create_blackbook(title, sections)
        
        if result['success']:
            # Add download URL to response
            result['download_url'] = f"/api/download/{result['filename']}"
            logger.success(f"Document created: {result['filename']}")
            return jsonify(result), 200
        else:
            return jsonify(result), 500
            
    except Exception as e:
        logger.error(f"Error in create document endpoint: {str(e)}")
        return jsonify(format_api_response(
            success=False,
            error=f"Server error: {str(e)}",
            error_code="INTERNAL_SERVER_ERROR"
        )), 500


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 Not Found errors"""
    logger.warning(f"404 error: {request.url}")
    return jsonify(format_api_response(
        success=False,
        error="The requested endpoint does not exist",
        error_code="NOT_FOUND"
    )), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 Internal Server errors"""
    logger.error(f"500 error: {str(error)}")
    return jsonify(format_api_response(
        success=False,
        error="Internal server error occurred",
        error_code="INTERNAL_SERVER_ERROR"
    )), 500


# ============================================
# APPLICATION STARTUP
# ============================================

if __name__ == '__main__':
    """
    Start the Flask development server
    
    Note: This is for development only.
    For production, use a WSGI server like Gunicorn or uWSGI.
    """
    
    # Print startup information
    print("\n" + "="*60)
    print("🚀 AI Blackbook Generator - Starting Server")
    print("="*60)
    print(f"📍 Server URL: http://localhost:5000")
    print(f"📖 API Docs: http://localhost:5000/")
    print(f"💚 Health Check: http://localhost:5000/health")
    print("="*60)
    print("\n⚡ Server is starting...\n")
    
    # Start Flask development server
    app.run(
        host='0.0.0.0',      # Listen on all network interfaces
        port=5000,           # Port number
        debug=True           # Enable debug mode (auto-reload on code changes)
    )
