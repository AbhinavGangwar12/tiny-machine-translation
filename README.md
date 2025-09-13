# Tiny Machine Translation - Pixel Theme App

A retro pixel-themed machine translation app with GitHub-based user logging.

## 🚀 Quick Deploy

### For Hugging Face Spaces:

1. **Create a new Space** on Hugging Face
2. **Upload all files** from this repository
3. **Set Environment Variable**:
   - Go to Space Settings → Secrets
   - Add: `GITHUB_TOKEN` = `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`
4. **Deploy** - Your app will be live!

### For Streamlit Cloud:

1. **Connect your GitHub repository**
2. **Set Environment Variable**:
   - Go to App Settings → Secrets
   - Add: `GITHUB_TOKEN` = `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`
3. **Deploy** - Your app will be live!

## 📁 Files Included

- `main_app.py` - Main Streamlit application
- `assets/style.css` - Pixel theme styling
- `requirements.txt` - Python dependencies
- `GITHUB_SETUP.md` - Detailed setup instructions
- `test_github_integration.py` - Test script for GitHub integration

## 🎮 Features

- **Retro Pixel Theme** - Classic arcade game styling
- **Machine Translation** - English to other languages
- **User Logging** - Automatically logs users to GitHub
- **Admin Panel** - View logs at `?admin=true`
- **Responsive Design** - Works on all devices

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable (Windows)
set GITHUB_TOKEN=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

# Run locally
streamlit run main_app.py
```

## 📊 User Logging

- User names are automatically saved to GitHub repository
- View logs at: `https://github.com/AbhinavGangwar12/users/blob/main/user_log.txt`
- Admin panel: `your-app-url.com?admin=true`

## 🎨 Customization

- Edit `assets/style.css` for styling changes
- Modify `main_app.py` for functionality changes
- Update GitHub repository details in the code

## 🛡️ Security

- GitHub token is stored as environment variable
- User logging is completely hidden from users
- No sensitive data is exposed in the UI

## 📝 Log Format

```
2024-01-15 14:30:25 - JohnDoe
2024-01-15 14:32:10 - JaneSmith
2024-01-15 14:35:45 - BobWilson
```

## 🚀 Deployment URLs

After deployment, your app will be available at:
- **Hugging Face**: `https://huggingface.co/spaces/your-username/your-space-name`
- **Streamlit Cloud**: `https://your-app-name.streamlit.app`

## 📞 Support

If you encounter any issues:
1. Check the GitHub repository for user logs
2. Verify the `GITHUB_TOKEN` environment variable is set
3. Check the admin panel at `?admin=true`
