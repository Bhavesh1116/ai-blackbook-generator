# 📚 AI Blackbook Generator

> Generate professional academic blackbooks instantly using AI - Complete with table of contents, page numbers, and academic formatting!

A powerful Flask-based web application that uses Google Gemini AI to generate comprehensive academic documents (blackbooks) on any topic. Perfect for students, researchers, and educators who need well-structured academic content quickly.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

- 🤖 **AI-Powered Content Generation** - Uses Google Gemini 2.5 Flash for high-quality academic content
- 📄 **Professional Document Formatting** - Automatic table of contents, page numbers, and academic layout
- 🎨 **Beautiful Web UI** - Modern, responsive interface for easy document generation
- 📊 **Structured Sections** - Abstract, Introduction, Literature Review, Methodology, Results, Conclusion
- ⚡ **Fast Generation** - Creates complete documents in 15-20 seconds
- 💾 **Automatic Download** - Generated documents download automatically
- 🔒 **Secure** - API key management with environment variables
- 📱 **Mobile Friendly** - Responsive design works on all devices

## 🎬 Demo

![AI Blackbook Generator Demo](https://via.placeholder.com/800x400?text=Add+Your+Screenshot+Here)

## 🚀 Quick Start

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key ([Get it free here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-blackbook-generator.git
   cd ai-blackbook-generator
   ```
   
   Replace `YOUR-USERNAME` with your GitHub username.

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   # Windows
   copy .env.example .env
   
   # Mac/Linux
   cp .env.example .env
   ```
   
   Edit `.env` file and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your-actual-api-key-here
   ```
   
   ⚠️ **Important**: Remove any quotes around the API key!

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   ```
   http://localhost:5000
   ```

That's it! 🎉 You're ready to generate blackbooks!

## 📖 Usage

### Web Interface (Easiest)

1. Open `http://localhost:5000` in your browser
2. Enter your topic (e.g., "Artificial Intelligence in Education")
3. Click "Generate Blackbook"
4. Wait 15-20 seconds
5. Your document will download automatically!

### API Usage

**Generate a blackbook:**
```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Machine Learning in Healthcare"}'
```

**Download by file ID:**
```bash
curl -O http://localhost:5000/download/a1b2c3d4
```

### Python Usage

```python
import requests

# Generate blackbook
response = requests.post('http://localhost:5000/generate', 
    json={'topic': 'Quantum Computing'})

result = response.json()
file_id = result['file_id']

# Download file
download_url = f'http://localhost:5000/download/{file_id}'
print(f"Download from: {download_url}")
```

## 📁 Project Structure

```
ai-blackbook-generator/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
│
├── services/                  # Business logic
│   ├── ai_client.py          # Google Gemini AI integration
│   ├── doc_generator.py      # Word document generation
│   └── blackbook_generator.py # Main generation logic
│
├── utils/                     # Utility functions
│   ├── helpers.py            # Helper functions
│   └── logger.py             # Logging utilities
│
├── templates/                 # HTML templates
│   └── index.html            # Web UI
│
├── static/                    # Static files
│   ├── style.css             # Styles
│   └── script.js             # Frontend JavaScript
│
├── outputs/                   # Generated documents
│   └── .gitkeep
│
└── tests/                     # Test scripts
    ├── test_api.py
    ├── test_generate.py
    └── test_download.py
```

## 📡 API Documentation

### Main Endpoint

#### Generate Blackbook
```http
POST /generate
```

**Request:**
```json
{
  "topic": "Artificial Intelligence in Healthcare"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Document generated successfully",
  "topic": "Artificial Intelligence in Healthcare",
  "file_id": "a1b2c3d4",
  "filename": "Artificial_Intelligence_in_Healthcare_a1b2c3d4.docx",
  "download_link": "/download/a1b2c3d4",
  "document_info": {
    "file_size_kb": 44.61,
    "sections_count": 6,
    "sections": ["abstract", "introduction", "literature_review", "methodology", "results", "conclusion"]
  },
  "ai_metadata": {
    "model": "gemini-2.5-flash",
    "word_count": 1847
  }
}
```

#### Download Document
```http
GET /download/<file_id>
```

Returns the generated Word document file.

### Additional Endpoints

- `GET /` - Home page (Web UI)
- `GET /health` - Health check
- `POST /api/generate` - Generate AI content only
- `POST /api/create-document` - Create document from custom content

For complete API documentation, see [API_GUIDE.md](API_GUIDE.md)

## 🎨 Document Features

Generated blackbooks include:

- ✅ **Professional Title Page** - Centered, formatted title
- ✅ **Table of Contents** - Automatic TOC with page numbers
- ✅ **Page Numbers** - Centered in footer
- ✅ **Academic Sections**:
  - Abstract (150-200 words)
  - Introduction (300-400 words)
  - Literature Review (400-500 words)
  - Methodology (250-300 words)
  - Results (300-400 words)
  - Conclusion (250-300 words)
- ✅ **Professional Formatting** - Times New Roman, proper margins, heading hierarchy
- ✅ **1.5 Line Spacing** - Standard academic format
- ✅ **1-inch Margins** - All sides

## 🧪 Testing

Run the test suite:

```bash
# Test API endpoints
python test_api.py

# Test generation
python test_generate.py

# Test download functionality
python test_download.py

# Test complete workflow
python test_complete_workflow.py
```

## 🛠️ Configuration

Edit `.env` file to configure:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Google Gemini API
GEMINI_API_KEY=your-api-key-here

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

## 📚 Documentation

- [Quick Start Guide (Hindi)](QUICK_START_HINDI.md)
- [API Guide](API_GUIDE.md)
- [API Key Setup](API_KEY_SETUP.md)
- [UI Guide](UI_GUIDE.md)
- [Formatting Guide](FORMATTING_GUIDE.md)
- [Download Guide](DOWNLOAD_GUIDE.md)
- [Architecture](ARCHITECTURE.md)

## 🐛 Troubleshooting

**Server won't start:**
```bash
# Check if port 5000 is already in use
# Kill the process or change port in .env
```

**API key error:**
```bash
# Make sure API key is in .env without quotes
# Example: GEMINI_API_KEY=AIzaSyAbc123...
```

**Generation fails:**
```bash
# Check internet connection
# Verify API key is valid
# Check server logs for details
```

**Module not found:**
```bash
# Activate virtual environment
# Reinstall dependencies
pip install -r requirements.txt
```

For more help, see [API_KEY_SETUP.md](API_KEY_SETUP.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📦 Dependencies

- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **google-generativeai** - Google Gemini AI integration
- **python-docx** - Word document generation
- **python-dotenv** - Environment variable management

See [requirements.txt](requirements.txt) for complete list.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powerful content generation
- Flask community for excellent web framework
- python-docx for document generation capabilities

## 📞 Support

If you encounter any issues or have questions:

1. Check the [documentation](API_GUIDE.md)
2. Look at [troubleshooting guide](API_KEY_SETUP.md)
3. Open an issue on GitHub

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ for students and researchers**

**Happy Generating! 🚀**
