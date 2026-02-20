"""
Example Usage: AI Blackbook Generator
Shows how to use the /generate endpoint
"""

import requests
import json

# API endpoint
BASE_URL = "http://localhost:5000"

def generate_blackbook(topic):
    """
    Generate a complete academic blackbook document
    
    Args:
        topic (str): The academic topic
        
    Returns:
        dict: Response with file info or error
    """
    print(f"\n{'='*60}")
    print(f"🚀 Generating Blackbook: {topic}")
    print(f"{'='*60}\n")
    
    # Make API request
    response = requests.post(
        f"{BASE_URL}/generate",
        json={"topic": topic},
        headers={"Content-Type": "application/json"}
    )
    
    # Parse response
    result = response.json()
    
    if response.status_code == 200 and result.get('success'):
        print("✅ SUCCESS!\n")
        print(f"📝 Topic: {result['topic']}")
        print(f"🆔 File ID: {result['file_id']}")
        print(f"📄 Filename: {result['filename']}")
        print(f"\n📊 Document Info:")
        doc_info = result['document_info']
        print(f"   - Size: {doc_info['file_size_kb']} KB")
        print(f"   - Sections: {doc_info['sections_count']}")
        print(f"   - Content: {', '.join(doc_info['sections'])}")
        print(f"\n🤖 AI Info:")
        ai_info = result['ai_metadata']
        print(f"   - Model: {ai_info['model']}")
        print(f"   - Words: {ai_info['word_count']}")
        print(f"\n⬇️  Download:")
        print(f"   {result['download_url']}")
        print(f"\n💾 File saved in: outputs/{result['filename']}")
        
        return result
    else:
        print("❌ ERROR!\n")
        print(f"Error: {result.get('error')}")
        print(f"Code: {result.get('error_code')}")
        return None


def download_document_by_id(file_id, save_as=None):
    """
    Download a generated document by file ID
    
    Args:
        file_id (str): The file ID
        save_as (str): Optional filename to save as
    """
    print(f"\n📥 Downloading file ID: {file_id}")
    
    response = requests.get(f"{BASE_URL}/download/{file_id}")
    
    if response.status_code == 200:
        # Get filename from Content-Disposition header or use file_id
        if save_as:
            filename = save_as
        else:
            content_disp = response.headers.get('Content-Disposition', '')
            if 'filename=' in content_disp:
                filename = content_disp.split('filename=')[1].strip('"')
            else:
                filename = f"document_{file_id}.docx"
        
        # Save file locally
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        file_size_kb = len(response.content) / 1024
        print(f"✅ Downloaded successfully!")
        print(f"   Filename: {filename}")
        print(f"   Size: {file_size_kb:.2f} KB")
    else:
        print(f"❌ Download failed: {response.status_code}")
        try:
            error = response.json()
            print(f"   Error: {error.get('error')}")
            print(f"   Code: {error.get('error_code')}")
        except:
            pass


def download_document(filename):
    """
    Download a generated document by full filename (legacy method)
    
    Args:
        filename (str): Name of the file to download
    """
    print(f"\n📥 Downloading: {filename}")
    
    response = requests.get(f"{BASE_URL}/api/download/{filename}")
    
    if response.status_code == 200:
        # Save file locally
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded to: {filename}")
    else:
        print(f"❌ Download failed: {response.status_code}")


# Example usage
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎓 AI Blackbook Generator - Example Usage")
    print("="*60)
    
    # Example 1: Generate a document
    topic1 = "The Impact of Artificial Intelligence on Modern Education"
    result1 = generate_blackbook(topic1)
    
    # Example 2: Another topic
    topic2 = "Quantum Computing: Principles and Applications"
    result2 = generate_blackbook(topic2)
    
    # Example 3: Download by file ID (recommended)
    if result1:
        print("\n" + "="*60)
        print("📥 Download Examples")
        print("="*60)
        
        # Method 1: Download by file ID (recommended)
        download_document_by_id(result1['file_id'])
        
        # Method 2: Download by full filename (legacy)
        # download_document(result1['filename'])
    
    print("\n" + "="*60)
    print("✅ Examples completed!")
    print("="*60 + "\n")
