"""
Test script for file download endpoints
Tests both /download/<file_id> and /api/download/<filename>
"""

import requests
import os

BASE_URL = "http://localhost:5000"

print("\n" + "="*60)
print("🧪 Testing File Download System")
print("="*60 + "\n")

# First, check if there are any files in outputs folder
outputs_dir = "outputs"
if os.path.exists(outputs_dir):
    files = [f for f in os.listdir(outputs_dir) if f.endswith('.docx')]
    if files:
        print(f"📁 Found {len(files)} document(s) in outputs folder\n")
        
        # Test with the first file
        test_file = files[0]
        print(f"Testing with: {test_file}")
        
        # Extract file ID (last part before .docx)
        file_id = test_file.rsplit('_', 1)[-1].replace('.docx', '')
        print(f"File ID: {file_id}\n")
        
        # Test 1: Download by file ID
        print("1️⃣ Testing /download/<file_id>...")
        response = requests.get(f"{BASE_URL}/download/{file_id}")
        
        if response.status_code == 200:
            print(f"✅ SUCCESS!")
            print(f"   Status: {response.status_code}")
            print(f"   Content-Type: {response.headers.get('Content-Type')}")
            print(f"   Content-Length: {len(response.content)} bytes")
            print(f"   Content-Disposition: {response.headers.get('Content-Disposition')}")
            
            # Save test file
            test_filename = f"test_download_by_id_{file_id}.docx"
            with open(test_filename, 'wb') as f:
                f.write(response.content)
            print(f"   Saved as: {test_filename}")
        else:
            print(f"❌ FAILED!")
            print(f"   Status: {response.status_code}")
            try:
                error = response.json()
                print(f"   Error: {error.get('error')}")
                print(f"   Code: {error.get('error_code')}")
            except:
                print(f"   Response: {response.text[:200]}")
        
        print()
        
        # Test 2: Download by full filename
        print("2️⃣ Testing /api/download/<filename>...")
        response = requests.get(f"{BASE_URL}/api/download/{test_file}")
        
        if response.status_code == 200:
            print(f"✅ SUCCESS!")
            print(f"   Status: {response.status_code}")
            print(f"   Content-Type: {response.headers.get('Content-Type')}")
            print(f"   Content-Length: {len(response.content)} bytes")
            
            # Save test file
            test_filename = f"test_download_by_name_{file_id}.docx"
            with open(test_filename, 'wb') as f:
                f.write(response.content)
            print(f"   Saved as: {test_filename}")
        else:
            print(f"❌ FAILED!")
            print(f"   Status: {response.status_code}")
            try:
                error = response.json()
                print(f"   Error: {error.get('error')}")
            except:
                print(f"   Response: {response.text[:200]}")
        
        print()
        
        # Test 3: Invalid file ID
        print("3️⃣ Testing invalid file ID...")
        response = requests.get(f"{BASE_URL}/download/invalid123")
        
        if response.status_code == 404:
            print(f"✅ Correctly returned 404")
            error = response.json()
            print(f"   Error: {error.get('error')}")
            print(f"   Code: {error.get('error_code')}")
        else:
            print(f"⚠️  Unexpected status: {response.status_code}")
        
        print()
        
        # Test 4: Invalid filename
        print("4️⃣ Testing invalid filename...")
        response = requests.get(f"{BASE_URL}/api/download/nonexistent.docx")
        
        if response.status_code == 404:
            print(f"✅ Correctly returned 404")
            error = response.json()
            print(f"   Error: {error.get('error')}")
            print(f"   Code: {error.get('error_code')}")
        else:
            print(f"⚠️  Unexpected status: {response.status_code}")
        
        print()
        
        # Test 5: Invalid file format
        print("5️⃣ Testing invalid file format...")
        response = requests.get(f"{BASE_URL}/api/download/test.txt")
        
        if response.status_code == 400:
            print(f"✅ Correctly returned 400")
            error = response.json()
            print(f"   Error: {error.get('error')}")
            print(f"   Code: {error.get('error_code')}")
        else:
            print(f"⚠️  Unexpected status: {response.status_code}")
        
    else:
        print("⚠️  No .docx files found in outputs folder")
        print("   Generate a document first using: python test_generate.py")
else:
    print("⚠️  Outputs folder not found")
    print("   Generate a document first using: python test_generate.py")

print("\n" + "="*60)
print("✅ Download tests completed!")
print("="*60 + "\n")
