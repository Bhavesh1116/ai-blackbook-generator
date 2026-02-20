# AI Blackbook Generator - Architecture

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         CLIENT                              │
│  (Browser, Python, cURL, Postman, etc.)                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ POST /generate
                     │ {"topic": "..."}
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    FLASK SERVER (app.py)                    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  /generate Endpoint                                  │  │
│  │  • Validate input                                    │  │
│  │  • Orchestrate AI + Document generation             │  │
│  │  • Return response with download link               │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────┬───────────────────┘
             │                            │
             │ Step 1                     │ Step 2
             │ Generate Content           │ Create Document
             │                            │
             ▼                            ▼
┌─────────────────────────┐  ┌──────────────────────────────┐
│  AI CLIENT              │  │  DOCUMENT GENERATOR          │
│  (services/ai_client.py)│  │  (services/doc_generator.py) │
│                         │  │                              │
│  • Connect to Gemini    │  │  • Create Word document      │
│  • Generate academic    │  │  • Apply formatting          │
│    content              │  │  • Save to outputs/          │
│  • Parse sections       │  │  • Return file info          │
└────────┬────────────────┘  └──────────────┬───────────────┘
         │                                  │
         │ API Call                         │ File I/O
         │                                  │
         ▼                                  ▼
┌─────────────────────────┐  ┌──────────────────────────────┐
│  GOOGLE GEMINI API      │  │  FILE SYSTEM                 │
│  (External Service)     │  │  outputs/*.docx              │
│                         │  │                              │
│  • gemini-pro model     │  │  • UUID-based filenames      │
│  • Generate text        │  │  • .docx format              │
│  • Return content       │  │  • Professional formatting   │
└─────────────────────────┘  └──────────────────────────────┘
```

## 📦 Component Breakdown

### 1. Flask Server (`app.py`)
**Responsibility:** HTTP request handling and orchestration

**Key Functions:**
- `@app.route('/generate')` - Main endpoint
- Input validation
- Error handling
- Response formatting

**Dependencies:**
- Flask, Flask-CORS
- services.ai_client
- services.doc_generator

### 2. AI Client (`services/ai_client.py`)
**Responsibility:** AI content generation

**Key Class:** `GeminiAIClient`

**Key Methods:**
- `generate_academic_content(topic)` - Main generation
- `_create_academic_prompt(topic)` - Prompt engineering
- `_parse_academic_content(raw)` - Section parsing

**Output Structure:**
```python
{
    "success": True,
    "topic": "...",
    "content": {
        "abstract": "...",
        "introduction": "...",
        "literature_review": "...",
        "methodology": "...",
        "results": "...",
        "conclusion": "..."
    },
    "metadata": {
        "model": "gemini-pro",
        "word_count": 1500,
        "character_count": 9500
    }
}
```

### 3. Document Generator (`services/doc_generator.py`)
**Responsibility:** Word document creation

**Key Class:** `DocumentGenerator`

**Key Methods:**
- `create_blackbook(title, sections)` - Main creation
- `_setup_document_styles(doc)` - Styling
- `_add_title_page(doc, title)` - Title page
- `_add_sections(doc, sections)` - Content sections
- `_generate_filename(title)` - UUID naming

**Output Structure:**
```python
{
    "success": True,
    "filepath": "outputs/...",
    "filename": "..._uuid.docx",
    "title": "...",
    "sections_count": 6,
    "file_size": 45678
}
```

### 4. Utilities (`utils/`)

**helpers.py:**
- `format_response()` - Consistent API responses
- `get_timestamp()` - ISO timestamps
- `save_json()` / `load_json()` - JSON handling
- `sanitize_filename()` - Safe filenames

**logger.py:**
- `Logger` class - Structured logging
- `info()`, `warning()`, `error()`, `success()` methods

## 🔄 Request Flow

### Successful Request

```
1. Client sends POST /generate
   └─> {"topic": "AI in Healthcare"}

2. Flask validates input
   ├─> Check topic exists
   ├─> Check topic length
   └─> Check API configured

3. AI Client generates content
   ├─> Create academic prompt
   ├─> Call Gemini API
   ├─> Parse response into sections
   └─> Return structured content

4. Document Generator creates file
   ├─> Initialize Word document
   ├─> Add title page
   ├─> Add page break
   ├─> Add each section with formatting
   ├─> Generate UUID filename
   └─> Save to outputs/

5. Flask returns response
   └─> {
         "success": true,
         "file_id": "a1b2c3d4",
         "filename": "...",
         "download_link": "/api/download/...",
         ...
       }

6. Client downloads document
   └─> GET /api/download/<filename>
```

### Error Handling Flow

```
1. Error occurs at any step
   └─> Exception caught

2. Error categorized
   ├─> Validation error (400)
   ├─> API error (500)
   └─> Server error (500)

3. Error response formatted
   └─> {
         "success": false,
         "error": "Description",
         "error_code": "CODE",
         "topic": "..."
       }

4. Client receives error
   └─> Handle based on error_code
```

## 🗂️ File Structure

```
ai-blackbook-generator/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
│
├── services/                   # Business logic
│   ├── __init__.py
│   ├── ai_client.py           # Gemini AI integration
│   ├── doc_generator.py       # Word document creation
│   └── blackbook_generator.py # Legacy service
│
├── utils/                      # Utilities
│   ├── __init__.py
│   ├── helpers.py             # Helper functions
│   └── logger.py              # Logging utility
│
├── outputs/                    # Generated documents
│   ├── .gitkeep
│   └── *.docx                 # Generated files
│
├── test_api.py                # Full test suite
├── test_generate.py           # Quick endpoint test
├── example_usage.py           # Usage examples
│
├── README.md                  # Main documentation
├── API_GUIDE.md              # API documentation
└── ARCHITECTURE.md           # This file
```

## 🔐 Security Architecture

### Environment Variables
```
.env file (not committed)
├── GEMINI_API_KEY=xxx
├── FLASK_ENV=development
└── SECRET_KEY=xxx
```

### Data Flow Security
```
1. API Key stored in environment
2. Never exposed in responses
3. Used only for Gemini API calls
4. Files saved locally (not uploaded)
5. CORS enabled for API access
```

## 📊 Data Models

### Request Model
```python
{
    "topic": str  # Required, min 3 chars
}
```

### AI Content Model
```python
{
    "success": bool,
    "topic": str,
    "content": {
        "abstract": str,
        "introduction": str,
        "literature_review": str,
        "methodology": str,
        "results": str,
        "conclusion": str
    },
    "metadata": {
        "model": str,
        "word_count": int,
        "character_count": int
    }
}
```

### Document Model
```python
{
    "success": bool,
    "filepath": str,
    "filename": str,
    "title": str,
    "sections_count": int,
    "file_size": int
}
```

### Response Model
```python
{
    "success": bool,
    "message": str,
    "topic": str,
    "file_id": str,
    "filename": str,
    "download_link": str,
    "download_url": str,
    "document_info": {
        "file_size": int,
        "file_size_kb": float,
        "sections_count": int,
        "sections": list[str]
    },
    "ai_metadata": {
        "model": str,
        "word_count": int,
        "character_count": int
    }
}
```

## 🚀 Deployment Considerations

### Development
- Debug mode enabled
- Detailed error messages
- Hot reload on code changes
- Local file storage

### Production (Future)
- Debug mode disabled
- Generic error messages
- WSGI server (Gunicorn/uWSGI)
- Cloud storage (S3/GCS)
- Rate limiting
- Authentication
- HTTPS only

## 📈 Performance

### Typical Response Times
- Input validation: < 1ms
- AI generation: 5-15 seconds
- Document creation: 1-2 seconds
- Total: 6-17 seconds

### Optimization Opportunities
1. Cache common topics
2. Async AI generation
3. Background document creation
4. CDN for downloads
5. Database for metadata

## 🔧 Configuration

### Flask Configuration
```python
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
```

### Gemini Configuration
```python
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
```

### Document Configuration
```python
font_name = 'Times New Roman'
font_size = Pt(12)
line_spacing = WD_LINE_SPACING.ONE_POINT_FIVE
```

## 🎯 Design Principles

1. **Separation of Concerns**
   - Flask handles HTTP
   - AI Client handles generation
   - Doc Generator handles formatting

2. **Single Responsibility**
   - Each module has one job
   - Clear interfaces between components

3. **Error Handling**
   - Errors caught at every level
   - Meaningful error messages
   - Proper HTTP status codes

4. **Extensibility**
   - Easy to add new endpoints
   - Easy to swap AI providers
   - Easy to add new document formats

5. **Testability**
   - Each component testable independently
   - Test scripts provided
   - Example usage documented

---

**Last Updated:** 2026-02-20
**Version:** 1.0.0
