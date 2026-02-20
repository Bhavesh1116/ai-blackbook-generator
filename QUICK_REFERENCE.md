# Quick Reference Guide - AI Blackbook Generator

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key
echo "GEMINI_API_KEY=your-key-here" > .env

# 3. Start server
python app.py

# 4. Test
python test_complete_workflow.py
```

## 📡 API Endpoints

### Generate Document
```bash
POST /generate
Body: {"topic": "Your Topic"}
```

### Download by ID
```bash
GET /download/<file_id>
```

### Health Check
```bash
GET /health
```

## 💻 Code Examples

### Using the Logger
```python
from utils.logger import logger

logger.info("Starting process...")
logger.success("Done!")
logger.warning("Be careful")
logger.error("Something failed")
```

### Using Helpers
```python
from utils.helpers import validate_topic, format_api_response

# Validate input
is_valid, error, code = validate_topic(topic)

# Format response
response = format_api_response(
    success=True,
    data={"result": "ok"}
)
```

### Creating Documents
```python
from services.doc_generator import document_generator

result = document_generator.create_blackbook(
    title="My Paper",
    sections_dict={
        "abstract": "...",
        "introduction": "..."
    }
)
```

## 📁 Project Structure

```
├── app.py                    # Main Flask application
├── requirements.txt          # Dependencies
├── .env                      # Environment variables
│
├── services/                 # Business logic
│   ├── ai_client.py         # Gemini AI integration
│   └── doc_generator.py     # Document creation
│
├── utils/                    # Utilities
│   ├── helpers.py           # Helper functions
│   └── logger.py            # Logging system
│
├── outputs/                  # Generated documents
│
└── tests/                    # Test scripts
    ├── test_complete_workflow.py
    ├── test_download.py
    └── test_generate.py
```

## 🎨 Code Style

### Function Names
```python
# ✅ Good
def generate_blackbook(topic):
    pass

# ❌ Bad
def gen(t):
    pass
```

### Comments
```python
# ✅ Good - Explains WHY
# Validate topic to prevent empty content generation
if not topic:
    return error

# ❌ Bad - States the obvious
# Check if topic is not empty
if not topic:
    return error
```

### Docstrings
```python
# ✅ Good
def validate_topic(topic):
    """
    Validate a topic string for content generation
    
    Args:
        topic (str): The topic to validate
    
    Returns:
        tuple: (is_valid, error_message, error_code)
    """
    pass
```

## 🔧 Common Tasks

### Add New Endpoint
```python
# In app.py
@app.route('/your-endpoint', methods=['POST'])
def your_function():
    """
    Brief description
    
    Returns:
        JSON: Response data
    """
    # Your code here
    return jsonify(result)
```

### Add Helper Function
```python
# In utils/helpers.py
def your_helper(param):
    """
    What this function does
    
    Args:
        param: Description
    
    Returns:
        type: Description
    """
    # Your code here
    return result
```

### Add Logging
```python
from utils.logger import logger

logger.info("Starting operation...")
# Do something
logger.success("Operation completed!")
```

## 🐛 Debugging

### Check Logs
```python
# Add logging to see what's happening
logger.info(f"Variable value: {variable}")
```

### Test Endpoints
```bash
# Use curl to test
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Test"}'
```

### Check Server Status
```bash
curl http://localhost:5000/health
```

## 📚 Documentation

- `README.md` - Getting started
- `API_GUIDE.md` - API reference
- `REFACTORING_NOTES.md` - Code explanations
- `ARCHITECTURE.md` - System design

## 🧪 Testing

```bash
# Quick test
python test_generate.py

# Download test
python test_download.py

# Complete workflow
python test_complete_workflow.py

# Full test suite
python test_api.py
```

## ⚡ Performance Tips

1. **Cache results** - Store frequently requested content
2. **Async processing** - Use background tasks for slow operations
3. **Rate limiting** - Prevent API abuse
4. **Compression** - Enable gzip for responses

## 🔒 Security

1. **Environment variables** - Never commit `.env`
2. **Input validation** - Always validate user input
3. **Error messages** - Don't expose sensitive info
4. **HTTPS** - Use in production

## 📞 Getting Help

1. Check error code in response
2. Review documentation
3. Check server logs
4. Run test scripts
5. Verify configuration

## 🎯 Best Practices

1. **Follow existing patterns** - Consistency matters
2. **Add comments** - Explain complex logic
3. **Write tests** - Verify your changes
4. **Update docs** - Keep documentation current
5. **Use the logger** - Track what's happening

---

**Quick Reference Version:** 1.0.0
**Last Updated:** 2026-02-20
