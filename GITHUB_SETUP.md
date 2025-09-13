# GitHub Integration Setup Guide

## 🚀 How to Set Up GitHub-Based User Logging

### Step 1: Create a GitHub Personal Access Token

1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "User Logging Token"
4. Select these permissions:
   - `repo` (Full control of private repositories)
   - `public_repo` (Access public repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

### Step 2: Update the Code

In `main_app.py`, replace these lines with your actual GitHub details:

```python
REPO_OWNER = "AbhinavGangwar12"  # Replace with your GitHub username
REPO_NAME = "users"  # Replace with your repository name
```

### Step 3: Set Environment Variable

#### For Hugging Face Spaces:
1. Go to your Space settings
2. Add a new secret: `GITHUB_TOKEN`
3. Paste your token as the value

#### For Streamlit Cloud:
1. Go to your app settings
2. Add a new secret: `GITHUB_TOKEN`
3. Paste your token as the value

#### For Local Development:
Create a `.env` file in your project root:
```
GITHUB_TOKEN=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
```

### Step 4: Create the Log File

1. In your GitHub repository, create a file called `user_log.txt`
2. Leave it empty or add a header like:
```
# User Access Log
# Format: YYYY-MM-DD HH:MM:SS - Username
```

### Step 5: Deploy and Test

1. Deploy your app to Hugging Face Spaces or Streamlit Cloud
2. Test by logging in with different usernames
3. Check your GitHub repository - you should see commits updating `user_log.txt`
4. Access admin panel: `your-app-url.com?admin=true`

## ✅ Benefits of This Approach

- **Persistent Storage**: Data is saved in your GitHub repository
- **Version Control**: Every user login creates a commit
- **Accessible Anywhere**: View logs from any device
- **Backup**: GitHub automatically backs up your data
- **Free**: No additional costs for storage

## 🔍 How to View Logs

1. **GitHub Repository**: Check `user_log.txt` file
2. **Admin Panel**: Visit `your-app-url.com?admin=true`
3. **Git History**: See all commits in your repository

## 🛡️ Security Notes

- Keep your GitHub token secure
- Don't commit the token to your repository
- Use environment variables only
- The token has access to your repositories, so keep it private

## 📝 Example Log Format

```
2024-01-15 14:30:25 - JohnDoe
2024-01-15 14:32:10 - JaneSmith
2024-01-15 14:35:45 - BobWilson
```

