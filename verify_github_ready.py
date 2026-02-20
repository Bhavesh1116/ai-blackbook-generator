"""
Verify that the project is ready to be pushed to GitHub
"""

import os
import sys

def check_file_exists(filepath, required=True):
    """Check if a file exists"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else ("❌" if required else "⚠️")
    print(f"{status} {filepath}")
    return exists

def check_file_not_exists(filepath):
    """Check that a file does NOT exist (good for security)"""
    exists = os.path.exists(filepath)
    status = "✅" if not exists else "❌"
    message = "Not found (good!)" if not exists else "FOUND (DANGER!)"
    print(f"{status} {filepath} - {message}")
    return not exists

def check_gitignore_contains(pattern):
    """Check if .gitignore contains a pattern"""
    try:
        with open('.gitignore', 'r') as f:
            content = f.read()
            contains = pattern in content
            status = "✅" if contains else "❌"
            print(f"{status} .gitignore contains '{pattern}'")
            return contains
    except:
        print(f"❌ Could not read .gitignore")
        return False

def main():
    print("=" * 60)
    print("🔍 GitHub Ready Verification")
    print("=" * 60)
    
    all_good = True
    
    # Check essential files exist
    print("\n📄 Essential Files:")
    all_good &= check_file_exists("README.md")
    all_good &= check_file_exists("LICENSE")
    all_good &= check_file_exists("CONTRIBUTING.md")
    all_good &= check_file_exists(".gitignore")
    all_good &= check_file_exists(".env.example")
    all_good &= check_file_exists("requirements.txt")
    all_good &= check_file_exists("app.py")
    
    # Check documentation
    print("\n📚 Documentation:")
    check_file_exists("API_GUIDE.md", required=False)
    check_file_exists("GITHUB_SETUP_HINDI.md", required=False)
    check_file_exists("GIT_COMMANDS_CHEATSHEET.md", required=False)
    check_file_exists("PRE_PUSH_CHECKLIST.md", required=False)
    check_file_exists("GITHUB_READY.md", required=False)
    
    # Check folders exist
    print("\n📁 Project Structure:")
    all_good &= check_file_exists("services/")
    all_good &= check_file_exists("utils/")
    all_good &= check_file_exists("templates/")
    all_good &= check_file_exists("static/")
    all_good &= check_file_exists("outputs/")
    
    # Check sensitive files DON'T exist or are ignored
    print("\n🔒 Security Check:")
    all_good &= check_file_not_exists(".env")
    
    # Check .gitignore
    print("\n📝 .gitignore Check:")
    all_good &= check_gitignore_contains(".env")
    all_good &= check_gitignore_contains("__pycache__")
    all_good &= check_gitignore_contains("*.pyc")
    all_good &= check_gitignore_contains("venv")
    
    # Check for common issues
    print("\n⚠️  Common Issues Check:")
    if os.path.exists(".env"):
        print("❌ WARNING: .env file exists!")
        print("   Make sure it's in .gitignore and won't be pushed!")
        all_good = False
    else:
        print("✅ No .env file found (good!)")
    
    if os.path.exists("venv/") or os.path.exists("env/"):
        print("⚠️  Virtual environment folder found")
        print("   Make sure it's in .gitignore")
    else:
        print("✅ No venv folder in project root")
    
    # Final verdict
    print("\n" + "=" * 60)
    if all_good:
        print("🎉 ALL CHECKS PASSED!")
        print("✅ Your project is ready to be pushed to GitHub!")
        print("\nNext steps:")
        print("1. Read GITHUB_READY.md for push instructions")
        print("2. Run: git init")
        print("3. Run: git add .")
        print("4. Run: git commit -m 'Initial commit'")
        print("5. Add remote and push!")
    else:
        print("❌ SOME CHECKS FAILED!")
        print("⚠️  Please fix the issues above before pushing")
        print("\nCheck:")
        print("- PRE_PUSH_CHECKLIST.md")
        print("- GITHUB_SETUP_HINDI.md")
    print("=" * 60)
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
