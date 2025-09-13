#!/usr/bin/env python3
"""
Test script to verify GitHub integration works
Run this to test if your GitHub token and repository setup is working
"""

import os
import requests
import base64
from datetime import datetime as dt

def test_github_connection():
    """Test GitHub API connection and file operations."""
    
    # Your GitHub details
    GITHUB_TOKEN = "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"
    REPO_OWNER = "AbhinavGangwar12"
    REPO_NAME = "users"
    FILE_PATH = "user_log.txt"
    
    print("🔍 Testing GitHub Integration...")
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print(f"File: {FILE_PATH}")
    print("-" * 50)
    
    # Test 1: Check if repository exists
    print("1. Testing repository access...")
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repo_data = response.json()
            print(f"✅ Repository found: {repo_data['full_name']}")
            print(f"   Description: {repo_data.get('description', 'No description')}")
        else:
            print(f"❌ Repository not found. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error accessing repository: {e}")
        return False
    
    # Test 2: Check if file exists
    print("\n2. Testing file access...")
    file_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    
    try:
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            file_data = response.json()
            content = base64.b64decode(file_data['content']).decode('utf-8')
            print(f"✅ File exists with {len(content.split())} lines")
            print("   Current content preview:")
            for line in content.split('\n')[:5]:  # Show first 5 lines
                if line.strip():
                    print(f"   {line}")
        elif response.status_code == 404:
            print("⚠️  File doesn't exist yet - this is normal for first run")
        else:
            print(f"❌ Error accessing file. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error accessing file: {e}")
        return False
    
    # Test 3: Try to create/update file
    print("\n3. Testing file update...")
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    test_entry = f"{timestamp} - TEST_USER\n"
    
    try:
        # Get current content
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            file_data = response.json()
            current_content = base64.b64decode(file_data['content']).decode('utf-8')
            new_content = current_content + test_entry
            sha = file_data['sha']
        else:
            # File doesn't exist, create new
            new_content = test_entry
            sha = None
        
        # Update file
        update_data = {
            "message": f"Test update - {timestamp}",
            "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
            "sha": sha
        }
        
        update_response = requests.put(file_url, headers=headers, json=update_data)
        
        if update_response.status_code == 200:
            print("✅ File update successful!")
            print(f"   Added test entry: {test_entry.strip()}")
        else:
            print(f"❌ File update failed. Status: {update_response.status_code}")
            print(f"   Response: {update_response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating file: {e}")
        return False
    
    print("\n🎉 All tests passed! GitHub integration is working correctly.")
    print("\nNext steps:")
    print("1. Set GITHUB_TOKEN as environment variable in your deployment platform")
    print("2. Deploy your app to Hugging Face Spaces or Streamlit Cloud")
    print("3. Test user login - it should update the GitHub file automatically")
    
    return True

if __name__ == "__main__":
    test_github_connection()
