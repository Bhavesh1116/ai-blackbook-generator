# File Download System - Complete Guide

## 📥 Overview

The AI Blackbook Generator provides two methods for downloading generated documents:

1. **By File ID** (Recommended) - `/download/<file_id>`
2. **By Filename** (Legacy) - `/api/download/<filename>`

## 🎯 Recommended: Download by File ID

### Endpoint

```
GET /download/<file_id>
```

### Why Use File ID?

✅ **Shorter URLs** - Just the UUID, no full filename needed
✅ **Cleaner** - Easy to remember and share
✅ **Flexible** - Works even if filename changes
✅ **RESTful** - Follows REST API best practices

### Example

```bash
# After generating a document, you get:
{
  "file_id": "a1b2c3d4",
  "download_link": "/download/a1b2c3d4"
}

# Download using:
GET http://localhost:5000/download/a1b2c3d4
```

### Response

**Success (200 OK):**
- Binary file data (Word document)
- Headers:
  ```
  Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
  Content-Disposition: attachment; filename="Topic_Name_a1b2c3d4.docx"
  Content-Length: 45678
  ```

**File Not Found (404):**
```json
{
  "success": false,
  "error": "No document found with file ID: a1b2c3d4",
  "error_code": "FILE_NOT_FOUND",
  "file_id": "a1b2c3d4"
}
```

**Invalid Format (400):**
```json
{
  "success": false,
  "error": "Invalid file ID format",
  "error_code": "INVALID_FILE_ID"
}
```

## 📄 Alternative: Download by Filename

### Endpoint

```
GET /api/download/<filename>
```

### Example

```bash
GET http://localhost:5000/api/download/Machine_Learning_a1b2c3d4.docx
```

### Response

**Success (200 OK):**
- Binary file data (Word document)
- Same headers as file ID method

**File Not Found (404):**
```json
{
  "success": false,
  "error": "File not found: Machine_Learning_a1b2c3d4.docx",
  "error_code": "FILE_NOT_FOUND",
  "filename": "Machine_Learning_a1b2c3d4.docx"
}
```

**Invalid Filename (400):**
```json
{
  "success": false,
  "error": "Invalid filename. Must be a .docx file",
  "error_code": "INVALID_FILENAME"
}
```

## 💻 Usage Examples

### Python (requests)

```python
import requests

# Method 1: Download by file ID (recommended)
file_id = "a1b2c3d4"
response = requests.get(f"http://localhost:5000/download/{file_id}")

if response.status_code == 200:
    with open(f"document_{file_id}.docx", 'wb') as f:
        f.write(response.content)
    print("Downloaded successfully!")
else:
    error = response.json()
    print(f"Error: {error['error']}")

# Method 2: Download by filename
filename = "Machine_Learning_a1b2c3d4.docx"
response = requests.get(f"http://localhost:5000/api/download/{filename}")

if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
```

### cURL

```bash
# Download by file ID
curl -O -J http://localhost:5000/download/a1b2c3d4

# Download by filename
curl -O http://localhost:5000/api/download/Machine_Learning_a1b2c3d4.docx
```

### JavaScript (fetch)

```javascript
// Download by file ID
const fileId = 'a1b2c3d4';

fetch(`http://localhost:5000/download/${fileId}`)
  .then(response => {
    if (response.ok) {
      return response.blob();
    }
    throw new Error('Download failed');
  })
  .then(blob => {
    // Create download link
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `document_${fileId}.docx`;
    a.click();
  })
  .catch(error => console.error('Error:', error));
```

### HTML Direct Link

```html
<!-- Download by file ID -->
<a href="http://localhost:5000/download/a1b2c3d4" download>
  Download Document
</a>

<!-- Download by filename -->
<a href="http://localhost:5000/api/download/Machine_Learning_a1b2c3d4.docx" download>
  Download Document
</a>
```

## 🔒 Security Features

### Input Validation

✅ **File ID Validation**
- Only alphanumeric characters and hyphens allowed
- Prevents directory traversal attacks

✅ **Filename Sanitization**
- Uses `os.path.basename()` to prevent path traversal
- Only allows `.docx` files
- Validates file exists and is a regular file

### Error Handling

✅ **Proper HTTP Status Codes**
- 200: Success
- 400: Invalid input
- 404: File not found
- 500: Server error

✅ **Detailed Error Messages**
- Clear error descriptions
- Error codes for programmatic handling
- No sensitive information leaked

## 📊 Error Codes Reference

| Code | HTTP Status | Description | Solution |
|------|-------------|-------------|----------|
| `FILE_NOT_FOUND` | 404 | File doesn't exist | Check file ID/name |
| `INVALID_FILE_ID` | 400 | Invalid ID format | Use valid UUID format |
| `INVALID_FILENAME` | 400 | Not a .docx file | Use .docx extension |
| `INVALID_PATH` | 400 | Path is not a file | Contact support |
| `DOWNLOAD_ERROR` | 500 | Server error | Check logs, retry |

## 🧪 Testing

### Test Script

```bash
python test_download.py
```

This tests:
1. ✅ Download by file ID
2. ✅ Download by filename
3. ✅ Invalid file ID (404)
4. ✅ Invalid filename (404)
5. ✅ Invalid file format (400)

### Manual Testing

```bash
# 1. Generate a document
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Test Topic"}'

# 2. Extract file_id from response
# Example: "file_id": "a1b2c3d4"

# 3. Download by file ID
curl -O -J http://localhost:5000/download/a1b2c3d4

# 4. Verify file downloaded
ls -lh document_*.docx
```

## 📁 File Storage

### Location
```
outputs/
├── Topic_Name_uuid1.docx
├── Another_Topic_uuid2.docx
└── ...
```

### Naming Convention
```
<Sanitized_Topic>_<UUID>.docx

Examples:
- Machine_Learning_in_Healthcare_a1b2c3d4.docx
- Quantum_Computing_Applications_x7y8z9.docx
```

### File Properties
- Format: `.docx` (Microsoft Word)
- MIME Type: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- Typical Size: 30-50 KB
- Encoding: UTF-8

## 🎨 Document Content

Downloaded documents include:

### Structure
1. **Title Page** - Centered, with date
2. **Page Break**
3. **Abstract** - 150-200 words
4. **Introduction** - 300-400 words
5. **Literature Review** - 400-500 words
6. **Methodology** - 250-300 words
7. **Results** - 300-400 words
8. **Conclusion** - 250-300 words

### Formatting
- **Font:** Times New Roman, 12pt
- **Headings:** Times New Roman, 14pt, Bold
- **Title:** Times New Roman, 18pt, Bold, Centered
- **Line Spacing:** 1.5
- **Alignment:** Justified
- **Margins:** Default Word margins

## 🔄 Complete Workflow

```
1. Generate Document
   POST /generate
   {"topic": "Your Topic"}
   
   ↓
   
2. Receive Response
   {
     "file_id": "a1b2c3d4",
     "download_link": "/download/a1b2c3d4"
   }
   
   ↓
   
3. Download File
   GET /download/a1b2c3d4
   
   ↓
   
4. Save Locally
   document_a1b2c3d4.docx
```

## 💡 Best Practices

### For Developers

1. **Always check response status**
   ```python
   if response.status_code == 200:
       # Success
   else:
       # Handle error
   ```

2. **Use file ID method**
   - Cleaner URLs
   - Better UX
   - More maintainable

3. **Handle errors gracefully**
   ```python
   try:
       response = requests.get(url)
       response.raise_for_status()
   except requests.exceptions.HTTPError as e:
       print(f"Download failed: {e}")
   ```

4. **Save with proper extension**
   ```python
   filename = f"document_{file_id}.docx"
   ```

### For Users

1. **Save file immediately** after generation
2. **Use the file ID** from the response
3. **Check file size** to verify download
4. **Open in Word** or compatible software

## 🐛 Troubleshooting

### Issue: 404 File Not Found

**Possible Causes:**
- File was deleted
- Wrong file ID
- File never generated

**Solution:**
- Verify file ID is correct
- Check `outputs/` folder
- Regenerate document if needed

### Issue: 400 Invalid File ID

**Possible Causes:**
- Special characters in ID
- Malformed ID

**Solution:**
- Use only the UUID part
- Don't include `.docx` extension
- Copy ID exactly from response

### Issue: Download starts but file is corrupted

**Possible Causes:**
- Incomplete download
- Network interruption

**Solution:**
- Retry download
- Check file size matches
- Verify Content-Length header

## 📞 Support

For issues:
1. Check error code in response
2. Review this guide
3. Check server logs
4. Verify file exists in `outputs/`

---

**Last Updated:** 2026-02-20
**Version:** 1.0.0
