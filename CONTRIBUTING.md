# Contributing to AI Blackbook Generator

Thank you for your interest in contributing to AI Blackbook Generator! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please create an issue with:
- Clear description of the feature
- Use case and benefits
- Possible implementation approach (optional)

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/ai-blackbook-generator.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make your changes**
   - Follow the code style guidelines below
   - Add comments and docstrings
   - Test your changes thoroughly

4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Include screenshots for UI changes

## Code Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused
- Add comments for complex logic

Example:
```python
def generate_content(topic):
    """
    Generate academic content for a given topic.
    
    Args:
        topic (str): The academic topic to generate content about
        
    Returns:
        dict: Generated content with sections
    """
    # Implementation here
    pass
```

### JavaScript Code

- Use ES6+ features
- Use meaningful variable names
- Add comments for complex logic
- Follow consistent indentation (2 spaces)

### HTML/CSS

- Use semantic HTML5 elements
- Keep CSS organized and commented
- Use consistent naming conventions
- Ensure responsive design

## Testing

Before submitting a PR:

1. **Test your changes**
   ```bash
   python test_api.py
   python test_generate.py
   python test_download.py
   ```

2. **Test the UI**
   - Open http://localhost:5000
   - Test all features manually
   - Check on different browsers

3. **Check for errors**
   - No console errors
   - No Python exceptions
   - Proper error handling

## Project Structure

```
ai-blackbook-generator/
├── app.py                  # Main Flask app - add routes here
├── services/              # Business logic
│   ├── ai_client.py      # AI integration
│   ├── doc_generator.py  # Document generation
│   └── blackbook_generator.py
├── utils/                 # Utilities
│   ├── helpers.py        # Helper functions
│   └── logger.py         # Logging
├── templates/            # HTML templates
├── static/               # CSS, JS, images
└── outputs/              # Generated files
```

## Adding New Features

### Adding a New API Endpoint

1. Add route in `app.py`:
```python
@app.route('/api/your-endpoint', methods=['POST'])
def your_endpoint():
    """Your endpoint description"""
    # Implementation
    return jsonify({"success": True})
```

2. Add business logic in `services/`:
```python
# services/your_service.py
class YourService:
    def process(self, data):
        # Implementation
        return result
```

3. Add tests:
```python
# test_your_feature.py
def test_your_endpoint():
    response = requests.post('http://localhost:5000/api/your-endpoint')
    assert response.status_code == 200
```

### Adding UI Features

1. Update `templates/index.html`
2. Add styles in `static/style.css`
3. Add JavaScript in `static/script.js`
4. Test on multiple browsers

## Documentation

When adding features:
- Update README.md
- Add examples
- Update API documentation
- Add inline comments

## Questions?

Feel free to:
- Open an issue for questions
- Ask in pull request comments
- Check existing documentation

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on what's best for the project

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🙏
