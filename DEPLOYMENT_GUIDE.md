# 🚀 Complete Deployment Guide

## Option 1: Hugging Face Spaces (Recommended)

### Step 1: Create Space
1. Go to [Hugging Face Spaces](https://huggingface.co/new-space)
2. Choose **Streamlit** as the SDK
3. Name your space: `tiny-machine-translation`
4. Set visibility to **Public**
5. Click **Create Space**

### Step 2: Upload Files
1. Upload all files from this repository to your Space
2. Make sure these files are included:
   - `main_app.py`
   - `assets/style.css`
   - `requirements.txt`
   - `README.md`

### Step 3: Set Environment Variable
1. Go to your Space → **Settings** → **Variables and secrets**
2. Click **New secret**
3. Name: `GITHUB_TOKEN`
4. Value: `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`
5. Click **Save**

### Step 4: Deploy
1. Your Space will automatically build and deploy
2. Wait for the build to complete (2-3 minutes)
3. Your app will be live at: `https://huggingface.co/spaces/your-username/tiny-machine-translation`

---

## Option 2: Streamlit Cloud

### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Upload all files to the repository
3. Make sure the repository is public

### Step 2: Deploy on Streamlit Cloud
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **New app**
3. Connect your GitHub repository
4. Set the main file path to `main_app.py`

### Step 3: Set Environment Variable
1. In the deployment settings, go to **Secrets**
2. Add: `GITHUB_TOKEN` = `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`
3. Click **Save**

### Step 4: Deploy
1. Click **Deploy**
2. Wait for deployment to complete
3. Your app will be live at: `https://your-app-name.streamlit.app`

---

## Option 3: VPS/Cloud Server

### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install git
sudo apt install git -y
```

### Step 2: Clone Repository
```bash
# Clone your repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Install dependencies
pip3 install -r requirements.txt
```

### Step 3: Set Environment Variable
```bash
# Set environment variable
export GITHUB_TOKEN="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"

# Add to .bashrc for persistence
echo 'export GITHUB_TOKEN="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"' >> ~/.bashrc
```

### Step 4: Run Application
```bash
# Run the app
streamlit run main_app.py --server.port 8501 --server.address 0.0.0.0
```

### Step 5: Set Up Reverse Proxy (Optional)
```bash
# Install nginx
sudo apt install nginx -y

# Configure nginx
sudo nano /etc/nginx/sites-available/streamlit
```

Add this configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/streamlit /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🔧 Testing Your Deployment

### 1. Test User Login
1. Visit your deployed app
2. Enter a username and click "Enter"
3. Check if you can access the translation page

### 2. Test GitHub Logging
1. Go to your GitHub repository: `https://github.com/AbhinavGangwar12/users`
2. Check the `user_log.txt` file
3. You should see new entries with timestamps

### 3. Test Admin Panel
1. Visit: `your-app-url.com?admin=true`
2. You should see the user log from GitHub
3. Test the refresh functionality

---

## 🛠️ Troubleshooting

### Common Issues:

#### 1. "GITHUB_TOKEN not found"
- **Solution**: Make sure the environment variable is set correctly
- **Check**: Verify in your deployment platform's settings

#### 2. "Repository not found"
- **Solution**: Check the repository name and owner in the code
- **Verify**: `REPO_OWNER = "AbhinavGangwar12"` and `REPO_NAME = "users"`

#### 3. "File not found"
- **Solution**: Create `user_log.txt` in your GitHub repository
- **Action**: Add an empty file or with a header comment

#### 4. App not loading
- **Solution**: Check the requirements.txt file
- **Verify**: All dependencies are installed

### Debug Steps:
1. Check the deployment logs
2. Verify environment variables are set
3. Test the GitHub integration manually
4. Check the admin panel for errors

---

## 📊 Monitoring

### View User Logs:
1. **GitHub Repository**: `https://github.com/AbhinavGangwar12/users/blob/main/user_log.txt`
2. **Admin Panel**: `your-app-url.com?admin=true`
3. **Git History**: See all commits in your repository

### Monitor Usage:
- Check GitHub repository for new commits
- Use the admin panel to view current session logs
- Monitor your deployment platform's analytics

---

## 🎉 Success!

Once deployed, your app will:
- ✅ Have a beautiful retro pixel theme
- ✅ Translate text using your machine learning model
- ✅ Automatically log users to GitHub
- ✅ Work on all devices
- ✅ Be accessible worldwide

**Your Tiny Machine Translation app is now live!** 🚀
