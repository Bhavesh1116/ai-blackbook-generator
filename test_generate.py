"""
Quick test for the /generate endpoint
"""

import requests
import json

BASE_URL = "http://localhost:5000"

print("\n" + "="*60)
print("🧪 Testing /generate Endpoint")
print("="*60 + "\n")

# Test 1: Check server is running
print("1️⃣ Checking server status...")
try:
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("✅ Server is running\n")
    else:
        print("❌ Server not responding properly\n")
        exit(1)
except Exception as e:
    print(f"❌ Cannot connect to server: {e}")
    print("Make sure the server is running: python app.py\n")
    exit(1)

# Test 2: Test /generate endpoint
print("2️⃣ Testing /generate endpoint...")
print("Topic: 'Artificial Intelligence in Education'\n")

data = {
    "topic": "Artificial Intelligence in Education"
}

try:
    response = requests.post(
        f"{BASE_URL}/generate",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    
    if response.status_code == 200 and result.get('success'):
        print("\n🎉 SUCCESS! Document generated!\n")
        print(f"✅ Topic: {result['topic']}")
        print(f"✅ File ID: {result['file_id']}")
        print(f"✅ Filename: {result['filename']}")
        print(f"\n📊 Document Info:")
        doc_info = result['document_info']
        print(f"   Size: {doc_info['file_size_kb']} KB")
        print(f"   Sections: {doc_info['sections_count']}")
        print(f"   Content: {', '.join(doc_info['sections'])}")
        print(f"\n🤖 AI Metadata:")
        ai_info = result['ai_metadata']
        print(f"   Model: {ai_info['model']}")
        print(f"   Words: {ai_info['word_count']}")
        print(f"\n⬇️  Download Link:")
        print(f"   {result['download_url']}")
        print(f"\n💾 File Location: outputs/{result['filename']}")
        
        # Save full response
        with open('outputs/test_generate_response.json', 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n📄 Full response saved to: outputs/test_generate_response.json")
        
        # Test download by file ID
        print(f"\n3️⃣ Testing file download by ID...")
        file_id = result['file_id']
        download_response = requests.get(f"{BASE_URL}/download/{file_id}")
        
        if download_response.status_code == 200:
            print(f"✅ Download successful!")
            print(f"   Content-Type: {download_response.headers.get('Content-Type')}")
            print(f"   Content-Length: {len(download_response.content)} bytes")
            
            # Save downloaded file
            test_filename = f"test_downloaded_{file_id}.docx"
            with open(test_filename, 'wb') as f:
                f.write(download_response.content)
            print(f"   Saved as: {test_filename}")
        else:
            print(f"❌ Download failed: {download_response.status_code}")
        
    else:
        print(f"\n❌ FAILED!\n")
        print(f"Error: {result.get('error')}")
        print(f"Error Code: {result.get('error_code')}")
        
        if result.get('error_code') == 'API_NOT_CONFIGURED':
            print("\n💡 TIP: Add your Gemini API key to .env file:")
            print("   1. Get key from: https://makersuite.google.com/app/apikey")
            print("   2. Add to .env: GEMINI_API_KEY=your-key-here")
            print("   3. Restart server: python app.py")
    
    print("\n" + "="*60)
    print("✅ Test completed!")
    print("="*60 + "\n")
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")
    import traceback
    traceback.print_exc()
