"""
Test script for AI Blackbook Generator API
Run this after starting the server to test the endpoints
"""

import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"


def test_home():
    """Test the home endpoint"""
    print("\n🧪 Testing Home Endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_health():
    """Test the health check endpoint"""
    print("\n🧪 Testing Health Check Endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_generate_academic():
    """Test academic content generation"""
    print("\n🧪 Testing Academic Content Generation...")
    
    data = {
        "topic": "The Impact of Machine Learning on Modern Education"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/generate",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ Success!")
        print(f"Topic: {result.get('topic')}")
        print(f"\nSections generated:")
        
        content = result.get('content', {})
        for section in ['abstract', 'introduction', 'literature_review', 
                       'methodology', 'results', 'conclusion']:
            section_content = content.get(section, '')
            word_count = len(section_content.split()) if section_content else 0
            print(f"  - {section.replace('_', ' ').title()}: {word_count} words")
        
        print(f"\nMetadata: {json.dumps(result.get('metadata'), indent=2)}")
        
        # Save full content to file
        with open('outputs/test_output.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print("\n📄 Full content saved to: outputs/test_output.json")
    else:
        print(f"❌ Error: {response.json()}")


def test_generate_simple():
    """Test simple content generation"""
    print("\n🧪 Testing Simple Content Generation...")
    
    data = {
        "prompt": "Explain quantum computing in simple terms"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/generate/simple",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ Success!")
        print(f"Content preview: {result.get('content', '')[:200]}...")
        print(f"\nMetadata: {json.dumps(result.get('metadata'), indent=2)}")
    else:
        print(f"❌ Error: {response.json()}")


def test_generate_document():
    """Test complete document generation (AI + DOCX) - Main endpoint"""
    print("\n🧪 Testing Main /generate Endpoint...")
    
    data = {
        "topic": "The Role of Blockchain Technology in Modern Finance"
    }
    
    response = requests.post(
        f"{BASE_URL}/generate",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ Success!")
        print(f"Message: {result.get('message')}")
        print(f"Topic: {result.get('topic')}")
        print(f"File ID: {result.get('file_id')}")
        print(f"Filename: {result.get('filename')}")
        print(f"\nDocument Info:")
        doc_info = result.get('document_info', {})
        print(f"  - File Size: {doc_info.get('file_size_kb')} KB")
        print(f"  - Sections: {doc_info.get('sections_count')}")
        print(f"  - Sections List: {', '.join(doc_info.get('sections', []))}")
        print(f"\nAI Metadata:")
        ai_meta = result.get('ai_metadata', {})
        print(f"  - Model: {ai_meta.get('model')}")
        print(f"  - Word Count: {ai_meta.get('word_count')}")
        print(f"\nDownload:")
        print(f"  - Link: {result.get('download_link')}")
        print(f"  - Full URL: {result.get('download_url')}")
        print(f"\n📄 Document saved in outputs/ folder")
    else:
        result = response.json()
        print(f"❌ Error: {result.get('error')}")
        print(f"Error Code: {result.get('error_code')}")


def test_create_document():
    """Test document creation from custom content"""
    print("\n🧪 Testing Custom Document Creation...")
    
    data = {
        "title": "Sample Academic Paper",
        "sections": {
            "abstract": "This is a sample abstract for testing purposes.",
            "introduction": "This is the introduction section with some content.",
            "conclusion": "This is the conclusion section."
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/api/create-document",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ Success!")
        print(f"Filename: {result.get('filename')}")
        print(f"File Size: {result.get('file_size')} bytes")
        print(f"Download URL: {result.get('download_url')}")
    else:
        print(f"❌ Error: {response.json()}")


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 AI Blackbook Generator - API Test Suite")
    print("=" * 60)
    
    try:
        # Test basic endpoints
        test_home()
        test_health()
        
        # Test AI generation endpoints
        print("\n" + "=" * 60)
        print("Testing AI Generation Endpoints")
        print("=" * 60)
        
        test_generate_academic()
        test_generate_simple()
        
        # Test document generation
        print("\n" + "=" * 60)
        print("Testing Document Generation")
        print("=" * 60)
        
        test_create_document()
        test_generate_document()
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server.")
        print("Make sure the Flask server is running: python app.py")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
