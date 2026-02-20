# API Key Setup Guide - IMPORTANT! ⚠️

## 🔑 Gemini API Key Kaise Lagayen

### Current Status:
❌ API key invalid hai - AI content generate nahi ho raha

### Solution (5 Minutes):

## Step 1: API Key Banao

### Option A: Google AI Studio (Recommended)
1. **Browser mein ye link kholo:**
   ```
   https://aistudio.google.com/app/apikey
   ```

2. **Google account se login karo**
   - Koi bhi Google account use kar sakte ho
   - Gmail account chahiye

3. **"Create API Key" button dhundo aur click karo**

4. **Project select karo:**
   - Agar pehle se project hai to select karo
   - Ya "Create new project" click karo

5. **API Key copy karo**
   - Ye kuch aisa dikhega: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
   - Pura key copy karo (40-45 characters)

### Option B: Google Cloud Console
1. Jao: https://console.cloud.google.com/
2. New project banao
3. "APIs & Services" > "Credentials" pe jao
4. "Create Credentials" > "API Key"
5. Key copy karo

## Step 2: .env File Mein Paste Karo

### Method 1: Text Editor Se (Easy)

1. **`.env` file kholo** (project folder mein hai)

2. **Ye line dhundo:**
   ```
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   ```

3. **`YOUR_API_KEY_HERE` ko replace karo apni key se:**
   ```
   GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
   (Apni actual key paste karo)

4. **File save karo** (Ctrl+S)

### Method 2: Command Line Se

```bash
# Windows PowerShell:
(Get-Content .env) -replace 'YOUR_API_KEY_HERE', 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' | Set-Content .env

# Replace 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' with your actual key
```

## Step 3: Server Restart Karo

### Terminal/CMD mein:

1. **Current server stop karo:**
   - `Ctrl + C` press karo

2. **Server dobara start karo:**
   ```bash
   python app.py
   ```

3. **Ye message dikhna chahiye:**
   ```
   ✅ Gemini AI Client initialized successfully
   ```

## Step 4: Test Karo

### Browser mein test:

1. **Kholo:**
   ```
   http://localhost:5000
   ```

2. **Topic enter karo:**
   ```
   Artificial Intelligence in Healthcare
   ```

3. **"Generate Blackbook" click karo**

4. **Wait karo 5-15 seconds**

5. **Success! Document download karo**

### Command line se test:

```bash
curl -X POST http://localhost:5000/generate ^
  -H "Content-Type: application/json" ^
  -d "{\"topic\":\"Test Topic\"}"
```

## ✅ Verification

### Agar Sab Theek Hai:
- ✅ Server start hoga bina error ke
- ✅ "Gemini AI Client initialized successfully" dikhega
- ✅ UI mein generate button kaam karega
- ✅ Document download hoga

### Agar Abhi Bhi Problem Hai:

#### Error: "API key not valid"
**Solution:**
- Check karo key correctly copy hui hai
- Spaces ya extra characters nahi hone chahiye
- Key 40-45 characters ki honi chahiye
- Quotes (" ") nahi lagane hai

#### Error: "API not configured"
**Solution:**
- .env file save kiya hai?
- File name exactly `.env` hai? (dot se shuru)
- Server restart kiya hai?

#### Error: "Module not found"
**Solution:**
```bash
pip install google-generativeai --upgrade
```

## 🎯 Quick Checklist

- [ ] API key banaya (https://aistudio.google.com/app/apikey)
- [ ] Key copy kiya (40-45 characters)
- [ ] .env file khola
- [ ] `YOUR_API_KEY_HERE` replace kiya
- [ ] File save kiya
- [ ] Server restart kiya (Ctrl+C then python app.py)
- [ ] Browser mein test kiya (http://localhost:5000)

## 💡 Pro Tips

### Free Tier Limits:
- **60 requests per minute**
- **1500 requests per day**
- Ye normal use ke liye kaafi hai

### API Key Security:
- ✅ .env file mein rakho (safe)
- ❌ Code mein directly mat likho
- ❌ GitHub pe upload mat karo
- ❌ Kisi ko share mat karo

### Backup:
- API key ko safe jagah save karo
- Agar key lost ho jaye to naya bana sakte ho

## 🆘 Still Not Working?

### Check Karo:

1. **Internet connection:**
   ```bash
   ping google.com
   ```

2. **API key format:**
   - Starts with: `AIza`
   - Length: 39-45 characters
   - No spaces, no quotes

3. **File location:**
   ```
   project_folder/
   ├── .env          ← Ye file
   ├── app.py
   └── ...
   ```

4. **Server logs:**
   - Terminal mein error messages dekho
   - "API key not valid" ya "initialized successfully"

## 📞 Need Help?

### Common Issues:

**Q: API key kahan se milega?**
A: https://aistudio.google.com/app/apikey

**Q: Free hai ya paid?**
A: Free tier available hai (1500 requests/day)

**Q: Kitni baar restart karna padega?**
A: Sirf ek baar, jab .env file change karo

**Q: Bina API key ke kaam karega?**
A: Haan, but AI content nahi banega. Custom content se documents bana sakte ho.

## ✨ Summary

1. **Get API Key:** https://aistudio.google.com/app/apikey
2. **Update .env:** Replace `YOUR_API_KEY_HERE` with your key
3. **Restart Server:** Ctrl+C then `python app.py`
4. **Test:** http://localhost:5000

**5 minutes mein ho jayega!** 🚀

---

**Current .env file location:** `C:\Users\bhave\OneDrive\Desktop\startup\.env`

**Edit karo aur server restart karo!**
