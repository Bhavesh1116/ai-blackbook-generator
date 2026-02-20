# AI Blackbook Generator - API Guide

## 🚀 Main Endpoint: `/generate`

The `/generate` endpoint is your one-stop solution for creating academic blackbook documents. It combines AI content generation with professional document formatting in a single API call.

### Endpoint Details

```
POST /generate
Content-Type: application/json
```

### Request Format

```json
{
  "topic": "Your academic topic here"
}
```

### Success Response (200 OK)

```json
{
  "success": true,
  "message": "Document generated successfully",
  "topic": "Artificial Intelligence in Healthcare",
  "file_id": "a1b2c3d4",
  "filename": "Artificial_Intelligence_in_Healthcare_a1b2c3d4.docx",
  "download_link": "/api/download/Artificial_Intelligence_in_Healthcare_a1b2c3d4.docx",
  "download_url": "http://localhost:5000/api/download/Artificial_Intelligence_in_Healthcare_a1b2c3d4.docx",
  "document_info": {
    "file_size": 45678,
    "file_size_kb": 44.61,
    "sections_count": 6,
    "sections": [
      "abstract",
      "introduction",
      "literature_review",
      "methodology",
      "results",
      "conclusion"
    ]
  },
  "ai_metadata": {
    "model": "gemini-pro",
    "word_count": 1500,
    "character_count": 9500
  }
}
```

### Error Response (400/500)

```json
{
  "success": false,
  "error": "Error message describing what went wrong",
  "error_code": "ERROR_CODE",
  "topic": "Your topic"
}
```

## 📋 Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| `API_NOT_CONFIGURED` | Gemini API key not set | Add GEMINI_API_KEY to .env file |
| `MISSING_BODY` | No request body provided | Send JSON body with request |
| `MISSING_TOPIC` | Topic field missing | Include "topic" field in JSON |
| `EMPTY_TOPIC` | Topic is empty | Provide a non-empty topic |
| `TOPIC_TOO_SHORT` | Topic less than 3 characters | Use at least 3 characters |
| `AI_GENERATION_FAILED` | AI content generation failed | Check API key and try again |
| `NO_SECTIONS_FOUND` | No sections in generated content | Try a different topic |
| `DOCUMENT_CREATION_FAILED` | Document creation failed | Check server logs |
| `INTERNAL_SERVER_ERROR` | Unexpected server error | Contact support |

## 🔄 Processing Flow

```
1. Receive Request
   ↓
2. Validate Input
   ↓
3. Generate AI Content (Gemini)
   ↓
4. Structure Sections
   ↓
5. Create Word Document
   ↓
6. Return Response with Download Link
```

## 💡 Usage Examples

### Python (requests)

```python
import requests

response = requests.post(
    'http://localhost:5000/generate',
    json={'topic': 'Machine Learning in Healthcare'},
    headers={'Content-Type': 'application/json'}
)

result = response.json()

if result['success']:
    print(f"Document created: {result['filename']}")
    print(f"Download: {result['download_url']}")
else:
    print(f"Error: {result['error']}")
```

### cURL

```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Quantum Computing Applications"}'
```

### JavaScript (fetch)

```javascript
fetch('http://localhost:5000/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    topic: 'Blockchain Technology in Finance'
  })
})
.then(response => response.json())
.then(data => {
  if (data.success) {
    console.log('Document created:', data.filename);
    console.log('Download:', data.download_url);
  } else {
    console.error('Error:', data.error);
  }
});
```

## 📥 Downloading Documents

After successful generation, download the document using the file ID:

### Recommended: Download by File ID

```
GET /download/<file_id>
```

**Example:**
```
GET /download/a1b2c3d4
```

**Advantages:**
- Shorter, cleaner URLs
- No need to remember full filename
- Works with any matching file

**Response Headers:**
```
Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
Content-Disposition: attachment; filename="Machine_Learning_in_Healthcare_a1b2c3d4.docx"
```

### Alternative: Download by Full Filename

```
GET /api/download/<filename>
```

**Example:**
```
GET /api/download/Machine_Learning_in_Healthcare_a1b2c3d4.docx
```

### Error Responses

**File Not Found (404):**
```json
{
  "success": false,
  "error": "No document found with file ID: xyz",
  "error_code": "FILE_NOT_FOUND",
  "file_id": "xyz"
}
```

**Invalid File ID (400):**
```json
{
  "success": false,
  "error": "Invalid file ID format",
  "error_code": "INVALID_FILE_ID"
}
```

**Download Error (500):**
```json
{
  "success": false,
  "error": "Download failed: ...",
  "error_code": "DOWNLOAD_ERROR"
}
```

### Document Features

The downloaded file will be a Word document (.docx) with:
- Times New Roman font
- Professional formatting
- Centered title page
- Proper chapter headings
- 1.5 line spacing
- Justified text alignment

## 🔧 Setup Requirements

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Get your Gemini API key from: https://makersuite.google.com/app/apikey

Add to `.env` file:
```
GEMINI_API_KEY=your-actual-api-key-here
```

### 3. Start Server

```bash
python app.py
```

Server will run at: `http://localhost:5000`

## 🧪 Testing

### Quick Test

```bash
python test_generate.py
```

### Full Test Suite

```bash
python test_api.py
```

### Example Usage

```bash
python example_usage.py
```

## 📊 Document Specifications

Generated documents include:

### Sections
1. **Abstract** - 150-200 words summary
2. **Introduction** - 300-400 words context and objectives
3. **Literature Review** - 400-500 words existing research
4. **Methodology** - 250-300 words research approach
5. **Results** - 300-400 words key findings
6. **Conclusion** - 250-300 words summary and implications

### Formatting
- Font: Times New Roman, 12pt
- Headings: Times New Roman, 14pt, Bold
- Title: Times New Roman, 18pt, Bold, Centered
- Line Spacing: 1.5
- Alignment: Justified
- Title Page: Centered with date
- Page Break: After title page

## 🎯 Best Practices

1. **Topic Selection**
   - Be specific and clear
   - Use academic language
   - Minimum 3 characters
   - Avoid special characters

2. **Error Handling**
   - Always check `success` field
   - Handle error codes appropriately
   - Log errors for debugging

3. **File Management**
   - Files saved in `outputs/` folder
   - Unique UUID-based filenames
   - Download immediately after generation

4. **API Key Security**
   - Never commit `.env` file
   - Use environment variables
   - Rotate keys regularly

## 🔒 Security Notes

- API key stored in environment variables
- Files saved locally in `outputs/` folder
- No data sent to external services except Gemini API
- CORS enabled for cross-origin requests

## 📞 Support

For issues or questions:
1. Check error code in response
2. Review server logs
3. Verify API key configuration
4. Check `outputs/` folder permissions

## 🎉 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key
echo "GEMINI_API_KEY=your-key-here" > .env

# 3. Start server
python app.py

# 4. Test endpoint
python test_generate.py
```

That's it! You're ready to generate academic blackbooks! 🚀
