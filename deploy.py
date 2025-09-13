#!/usr/bin/env python3
"""
Deployment verification script
Run this to verify everything is ready for deployment
"""

import os
import sys
import requests
import base64
from datetime import datetime as dt

def check_files():
    """Check if all required files exist."""
    required_files = [
        'main_app.py',
        'assets/style.css',
        'requirements.txt',
        'README.md',
        'app.py'
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def check_github_integration():
    """Test GitHub integration."""
    print("\n🔍 Testing GitHub integration...")
    
    GITHUB_TOKEN = "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"
    REPO_OWNER = "AbhinavGangwar12"
    REPO_NAME = "users"
    
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("✅ GitHub repository accessible")
            return True
        else:
            print(f"❌ GitHub repository not accessible. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ GitHub integration error: {e}")
        return False

def check_requirements():
    """Check if requirements.txt has all dependencies."""
    print("\n🔍 Checking requirements.txt...")
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        required_deps = ['streamlit', 'requests']
        missing_deps = []
        
        for dep in required_deps:
            if dep in content:
                print(f"✅ {dep}")
            else:
                print(f"❌ {dep} - MISSING")
                missing_deps.append(dep)
        
        if missing_deps:
            print(f"\n⚠️  Missing dependencies: {', '.join(missing_deps)}")
            return False
        
        print("✅ All dependencies present")
        return True
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def main():
    """Main deployment check."""
    print("🚀 Deployment Readiness Check")
    print("=" * 50)
    
    checks = [
        check_files(),
        check_github_integration(),
        check_requirements()
    ]
    
    print("\n" + "=" * 50)
    
    if all(checks):
        print("🎉 ALL CHECKS PASSED!")
        print("\nYour app is ready for deployment!")
        print("\nNext steps:")
        print("1. Choose your deployment platform:")
        print("   - Hugging Face Spaces (Recommended)")
        print("   - Streamlit Cloud")
        print("   - VPS/Cloud Server")
        print("2. Follow the DEPLOYMENT_GUIDE.md")
        print("3. Set GITHUB_TOKEN environment variable")
        print("4. Deploy!")
        return True
    else:
        print("❌ SOME CHECKS FAILED!")
        print("\nPlease fix the issues above before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
