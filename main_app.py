# import streamlit as st
# import requests
# import random
# import os
# import time
# import datetime
# from datetime import datetime as dt
# import base64

# # --- Helper Functions ---

# def load_css(file_name):
#     """Function to load the custom pixel-style CSS."""
#     try:
#         with open(file_name) as f:
#             st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#     except FileNotFoundError:
#         st.warning(f"CSS file '{file_name}' not found. Default styling will be used.")

# def update_github_log(username):
#     """Update user log file on GitHub repository."""
#     GITHUB_TOKEN = None
    
#     # Handle secrets correctly for both local and deployed environments
#     try:
#         # This will work when deployed on Streamlit Community Cloud
#         GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
#     except (AttributeError, FileNotFoundError):
#         # This is the fallback for local development
#         GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', "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")

#     REPO_OWNER = "AbhinavGangwar12"
#     REPO_NAME = "users"
#     FILE_PATH = "user_log.txt"
    
#     if not GITHUB_TOKEN:
#         return  # Skip if no token is found

#     timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
#     new_entry = f"{timestamp} - {username}\n"
    
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
#     headers = {
#         "Authorization": f"token {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github.v3+json"
#     }
    
#     try:
#         response = requests.get(url, headers=headers)
#         sha = None
#         current_content = ""
#         if response.status_code == 200:
#             file_data = response.json()
#             current_content = base64.b64decode(file_data['content']).decode('utf-8')
#             sha = file_data.get('sha')
        
#         new_content = current_content + new_entry
#         encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
        
#         update_data = {
#             "message": f"User log: {username}",
#             "content": encoded_content,
#             "sha": sha
#         }
        
#         requests.put(url, headers=headers, json=update_data)
        
#     except Exception as e:
#         # Silently fail if logging to GitHub fails
#         pass

# def typing_animation(text):
#     """Function for the title's typing animation."""
#     for char in text:
#         yield char
#         time.sleep(0.05)

# @st.cache_data
# def get_translation(text: str) -> str:
#     """Calls the Hugging Face Space API to get the translation."""
#     API_URL = "https://abhinavGangwar-tiny-model-30m.hf.space/translate"
#     if not text.strip():
#         return ""
#     payload = {"inputs": text}
#     try:
#         response = requests.post(API_URL, json=payload, timeout=30)
#         response.raise_for_status()
#         result = response.json()
#         return result.get("translation", "Error: Could not parse translation.")
#     except requests.exceptions.RequestException as e:
#         return f"Error: Could not connect to the translation service. Details: {e}"

# # --- Page Configuration ---
# st.set_page_config(
#     page_title="Tiny Machine Translation",
#     page_icon="🎮",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Apply the custom CSS theme
# load_css('assets/style.css')

# # --- Session State Initialization ---
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = ''

# # --- UI Rendering ---

# # 1. LOGIN PAGE (if user is not logged in)
# if not st.session_state.logged_in:
#     st.write_stream(typing_animation("Tiny Machine Translation"))

#     col1, col2 = st.columns([1, 2])

#     with col1:
#         st.markdown('<div class="login-image-container">', unsafe_allow_html=True)
#         image_dir = 'assets/images'
#         if os.path.exists(image_dir) and os.listdir(image_dir):
#             random_image = random.choice([os.path.join(image_dir, f) for f in os.listdir(image_dir)])
#             st.image(random_image, use_container_width=True, caption="Melody")
#         else:
#             st.warning("No images found in 'assets/images'.")
#             st.image("https://placehold.co/400x400/2a2a2a/ffffff?text=Image+Not+Found", caption="Melody", use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="pixel-box">
#             <p class="pixel-text">🤖 ENTER YOUR NAME</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         username_input = st.text_input("Username", key="username_input", placeholder="Enter your name", label_visibility="collapsed")
        
#         if st.button("Enter", type="primary"):
#             if username_input:
#                 st.session_state.username = username_input
#                 st.session_state.logged_in = True
#                 update_github_log(username_input)
#                 st.rerun()
#             else:
#                 st.error("Please enter a username.")

# # 2. TRANSLATION PAGE (for all logged-in users)
# else:
#     st.write_stream(typing_animation("Tiny Machine Translation"))
#     st.markdown(f"Welcome, **{st.session_state.username}**!")

#     if 'input_text' not in st.session_state:
#         st.session_state.input_text = ""
#     if 'translated_text' not in st.session_state:
#         st.session_state.translated_text = ""

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="pixel-box" style="border-color: #ff8c42;">
#             <p class="pixel-text" style="color: #ff8c42;">📝 INPUT TEXT</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.session_state.input_text = st.text_area(
#             "English Entry Option",
#             value=st.session_state.input_text,
#             height=200,
#             placeholder="Enter English text here...",
#             label_visibility="collapsed"
#         )

#     with col2:
#         st.markdown("""
#         <div class="pixel-box" style="border-color: #90EE90;">
#             <p class="pixel-text" style="color: #90EE90;">🌍 TRANSLATED TEXT</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.text_area(
#             "Translated Text",
#             value=st.session_state.translated_text,
#             height=200,
#             disabled=True,
#             label_visibility="collapsed"
#         )

#     btn_col1, btn_col2, _ = st.columns([1, 1, 4])

#     with btn_col1:
#         if st.button("Translate", type="primary"):
#             if st.session_state.input_text:
#                 # --- FIX: Restore the custom multi-step progress bar ---
#                 st.markdown("""
#                 <div class="pixel-box" style="margin-top: 10px;">
#                     <p class="pixel-text" style="color: #ff8c42; text-align: center;">
#                         🔄 TRANSLATION IN PROGRESS
#                     </p>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#                 progress_bar = st.progress(0)
#                 status_text = st.empty()
                
#                 loading_steps = [
#                     ("🔄 INITIALIZING...", 10),
#                     ("🔄 PROCESSING TEXT...", 25),
#                     ("🔄 CONNECTING TO MODEL...", 50),
#                     ("🔄 GENERATING TRANSLATION...", 75),
#                     ("🔄 FINALIZING RESULT...", 95)
#                 ]
                
#                 for message, progress in loading_steps:
#                     status_text.markdown(f"""
#                     <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
#                                 font-size: 10px; color: #FFFFFF; text-shadow: 2px 2px 0px #000000;">
#                         {message}
#                     </div>
#                     """, unsafe_allow_html=True)
#                     progress_bar.progress(progress)
#                     time.sleep(0.3)
                
#                 translation_result = get_translation(st.session_state.input_text)
#                 st.session_state.translated_text = translation_result
                
#                 status_text.markdown("""
#                 <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
#                              font-size: 10px; color: #4CAF50; text-shadow: 2px 2px 0px #000000;">
#                     ✅ TRANSLATION COMPLETE!
#                 </div>
#                 """, unsafe_allow_html=True)
#                 progress_bar.progress(100)
#                 time.sleep(0.5)
                
#                 progress_bar.empty()
#                 status_text.empty()
                
#                 st.rerun()
#             else:
#                 st.warning("Please enter some text to translate.")
    
#     with btn_col2:
#         if st.button("Log Out"):
#             for key in list(st.session_state.keys()):
#                 del st.session_state[key]
#             st.rerun()
    
#     st.markdown("""
#     <div class="pixel-box" style="margin-top: 30px;">
#         <p class="pixel-text" style="font-size: 8px; color: #ffcccb; text-align: center;">
#             ⚠️ DISCLAIMER: This model may produce inaccurate or incorrect translations. 
#             Please verify important translations with reliable sources.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st
# import requests
# import random
# import os
# import time
# import datetime
# from datetime import datetime as dt
# import base64

# # --- Helper Functions ---

# def load_css(file_name):
#     """Function to load the custom pixel-style CSS."""
#     try:
#         with open(file_name) as f:
#             st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#     except FileNotFoundError:
#         st.warning(f"CSS file '{file_name}' not found. Default styling will be used.")

# def update_github_log(username):
#     """Update user log file on GitHub repository with proper error handling."""
#     GITHUB_TOKEN = None
    
#     # --- This logic securely gets your token for local use or when deployed ---
#     try:
#         # For deployed apps on Streamlit Community Cloud, use st.secrets
#         GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
#     except (AttributeError, FileNotFoundError):
#         # For local development, use an environment variable or a hardcoded token
#         # IMPORTANT: Replace the placeholder token with your new, valid GitHub token
#         GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', "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") # <--- REPLACE THIS TOKEN

#     REPO_OWNER = "AbhinavGangwar12"
#     REPO_NAME = "users"
#     FILE_PATH = "user_log.txt"
    
#     if not GITHUB_TOKEN or "YOUR_NEW_TOKEN" in GITHUB_TOKEN:
#         st.warning("GitHub token not found. User log will not be updated.")
#         return

#     timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
#     new_entry = f"{timestamp} - {username}\n"
    
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
#     headers = {
#         "Authorization": f"token {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github.v3+json"
#     }
    
#     try:
#         # First, try to get the existing file to get its SHA hash
#         response = requests.get(url, headers=headers)
#         sha = None
#         current_content = ""
#         if response.status_code == 200:
#             file_data = response.json()
#             current_content = base64.b64decode(file_data['content']).decode('utf-8')
#             sha = file_data.get('sha')
        
#         # Prepare the new content
#         new_content = current_content + new_entry
#         encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
        
#         update_data = {
#             "message": f"User log: {username}",
#             "content": encoded_content,
#             "sha": sha  # Include SHA if the file already exists
#         }
        
#         # Make the PUT request to update the file
#         put_response = requests.put(url, headers=headers, json=update_data)
        
#         # --- FIX: Add error handling to show what's wrong ---
#         if put_response.status_code not in [200, 201]:
#             st.error(f"Failed to update GitHub log. Status: {put_response.status_code}, Response: {put_response.json().get('message', 'No message')}")
        
#     except Exception as e:
#         st.error(f"An exception occurred while updating GitHub log: {e}")


# def typing_animation(text):
#     """Function for the title's typing animation."""
#     for char in text:
#         yield char
#         time.sleep(0.05)

# @st.cache_data
# def get_translation(text: str) -> str:
#     """Calls the Hugging Face Space API to get the translation."""
#     API_URL = "https://abhinavGangwar-tiny-model-30m.hf.space/translate"
#     if not text.strip():
#         return ""
#     payload = {"inputs": text}
#     try:
#         response = requests.post(API_URL, json=payload, timeout=30)
#         response.raise_for_status()
#         result = response.json()
#         return result.get("translation", "Error: Could not parse translation.")
#     except requests.exceptions.RequestException as e:
#         return f"Error: Could not connect to the translation service. Details: {e}"

# # --- Page Configuration ---
# st.set_page_config(
#     page_title="Tiny Machine Translation",
#     page_icon="🎮",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Apply the custom CSS theme
# load_css('assets/style.css')

# # --- Session State Initialization ---
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = ''

# # --- UI Rendering ---

# # 1. LOGIN PAGE (if user is not logged in)
# if not st.session_state.logged_in:
#     st.write_stream(typing_animation("Tiny Machine Translation"))

#     col1, col2 = st.columns([1, 2])

#     with col1:
#         st.markdown('<div class="login-image-container">', unsafe_allow_html=True)
#         image_dir = 'assets/images'
#         if os.path.exists(image_dir) and os.listdir(image_dir):
#             random_image = random.choice([os.path.join(image_dir, f) for f in os.listdir(image_dir)])
#             st.image(random_image, use_container_width=True, caption="Melody")
#         else:
#             st.warning("No images found in 'assets/images'.")
#             st.image("https://placehold.co/400x400/2a2a2a/ffffff?text=Image+Not+Found", caption="Melody", use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="pixel-box">
#             <p class="pixel-text">🤖 ENTER YOUR NAME</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         username_input = st.text_input("Username", key="username_input", placeholder="Enter your name", label_visibility="collapsed")
        
#         if st.button("Enter", type="primary"):
#             if username_input:
#                 st.session_state.username = username_input
#                 st.session_state.logged_in = True
#                 update_github_log(username_input)
#                 st.rerun()
#             else:
#                 st.error("Please enter a username.")

# # 2. TRANSLATION PAGE (for all logged-in users)
# else:
#     st.write_stream(typing_animation("Tiny Machine Translation"))
#     st.markdown(f"Welcome, **{st.session_state.username}**!")

#     if 'input_text' not in st.session_state:
#         st.session_state.input_text = ""
#     if 'translated_text' not in st.session_state:
#         st.session_state.translated_text = ""

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="pixel-box" style="border-color: #ff8c42;">
#             <p class="pixel-text" style="color: #ff8c42;">📝 INPUT TEXT</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.session_state.input_text = st.text_area(
#             "English Entry Option",
#             value=st.session_state.input_text,
#             height=200,
#             placeholder="Enter English text here...",
#             label_visibility="collapsed"
#         )

#     with col2:
#         st.markdown("""
#         <div class="pixel-box" style="border-color: #90EE90;">
#             <p class="pixel-text" style="color: #90EE90;">🌍 TRANSLATED TEXT</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.text_area(
#             "Translated Text",
#             value=st.session_state.translated_text,
#             height=200,
#             disabled=True,
#             label_visibility="collapsed"
#         )

#     btn_col1, btn_col2, _ = st.columns([1, 1, 4])

#     with btn_col1:
#         if st.button("Translate", type="primary"):
#             if st.session_state.input_text:
#                 st.markdown("""
#                 <div class="pixel-box" style="margin-top: 10px;">
#                     <p class="pixel-text" style="color: #ff8c42; text-align: center;">
#                         🔄 TRANSLATION IN PROGRESS
#                     </p>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#                 progress_bar = st.progress(0)
#                 status_text = st.empty()
                
#                 loading_steps = [
#                     ("🔄 INITIALIZING...", 10),
#                     ("🔄 PROCESSING TEXT...", 25),
#                     ("🔄 CONNECTING TO MODEL...", 50),
#                     ("🔄 GENERATING TRANSLATION...", 75),
#                     ("🔄 FINALIZING RESULT...", 95)
#                 ]
                
#                 for message, progress in loading_steps:
#                     status_text.markdown(f"""
#                     <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
#                                 font-size: 10px; color: #FFFFFF; text-shadow: 2px 2px 0px #000000;">
#                         {message}
#                     </div>
#                     """, unsafe_allow_html=True)
#                     progress_bar.progress(progress)
#                     time.sleep(0.3)
                
#                 translation_result = get_translation(st.session_state.input_text)
#                 st.session_state.translated_text = translation_result
                
#                 status_text.markdown("""
#                 <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
#                              font-size: 10px; color: #4CAF50; text-shadow: 2px 2px 0px #000000;">
#                     ✅ TRANSLATION COMPLETE!
#                 </div>
#                 """, unsafe_allow_html=True)
#                 progress_bar.progress(100)
#                 time.sleep(0.5)
                
#                 progress_bar.empty()
#                 status_text.empty()
                
#                 st.rerun()
#             else:
#                 st.warning("Please enter some text to translate.")
    
#     with btn_col2:
#         if st.button("Log Out"):
#             for key in list(st.session_state.keys()):
#                 del st.session_state[key]
#             st.rerun()
    
#     st.markdown("""
#     <div class="pixel-box" style="margin-top: 30px;">
#         <p class="pixel-text" style="font-size: 8px; color: #ffcccb; text-align: center;">
#             ⚠️ DISCLAIMER: This model may produce inaccurate or incorrect translations. 
#             Please verify important translations with reliable sources.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st
import requests
import random
import os
import time
import datetime
from datetime import datetime as dt
import base64

# --- Helper Functions ---

def load_css(file_name):
    """Function to load the custom pixel-style CSS."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # This is fine for deployment if assets aren't included
        pass

def update_github_log(username):
    """Update user log file on GitHub repository with explicit error reporting."""
    GITHUB_TOKEN = None
    
    # Attempt to get the token from Streamlit's secret management
    try:
        GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    except (AttributeError, FileNotFoundError, KeyError):
        st.error("Fatal Error: Could not find GITHUB_TOKEN in Streamlit secrets. Please verify it was saved correctly.")
        return

    # --- Double-check these values are exactly correct (case-sensitive) ---
    REPO_OWNER = "AbhinavGangwar12"
    REPO_NAME = "users"
    FILE_PATH = "user_log.txt"
    
    if not GITHUB_TOKEN:
        st.warning("GitHub token is empty. User log will not be updated.")
        return

    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = f"{timestamp} - {username}\n"
    
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # --- MODIFICATION: Replaced 'pass' with detailed error reporting ---
    try:
        # Step 1: Get the existing file to find its SHA
        response = requests.get(url, headers=headers)
        response.raise_for_status() # This will raise an error for bad status codes (like 401, 404)
        
        sha = None
        current_content = ""
        # The file exists, so we decode it
        file_data = response.json()
        current_content = base64.b64decode(file_data['content']).decode('utf-8')
        sha = file_data.get('sha')
        
        # Step 2: Prepare the new content
        new_content = current_content + new_entry
        encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
        
        update_data = {
            "message": f"User log: {username}",
            "content": encoded_content,
            "sha": sha
        }
        
        # Step 3: Make the PUT request to update the file
        put_response = requests.put(url, headers=headers, json=update_data)
        put_response.raise_for_status() # Raise an error if the PUT request fails

    except requests.exceptions.HTTPError as http_err:
        # This will catch errors like "401 Client Error: Bad credentials" or "404 Not Found"
        st.error(f"HTTP Error from GitHub: {http_err}")
        st.error(f"Response Body: {http_err.response.text}")
    except Exception as e:
        # This will catch any other unexpected errors
        st.error(f"An unexpected error occurred: {e}")


def typing_animation(text):
    """Function for the title's typing animation."""
    for char in text:
        yield char
        time.sleep(0.05)

@st.cache_data
def get_translation(text: str) -> str:
    """Calls the Hugging Face Space API to get the translation."""
    API_URL = "https://abhinavGangwar-tiny-model-30m.hf.space/translate"
    if not text.strip():
        return ""
    payload = {"inputs": text}
    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get("translation", "Error: Could not parse translation.")
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to the translation service. Details: {e}"

# --- Page Configuration ---
st.set_page_config(
    page_title="Tiny Machine Translation",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the custom CSS theme
load_css('assets/style.css')

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

# --- UI Rendering ---

# 1. LOGIN PAGE (if user is not logged in)
if not st.session_state.logged_in:
    st.write_stream(typing_animation("Tiny Machine Translation"))

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="login-image-container">', unsafe_allow_html=True)
        image_dir = 'assets/images'
        if os.path.exists(image_dir) and os.listdir(image_dir):
            random_image = random.choice([os.path.join(image_dir, f) for f in os.listdir(image_dir)])
            st.image(random_image, use_container_width=True, caption="Melody")
        else:
            st.image("https://placehold.co/400x400/2a2a2a/ffffff?text=Image+Not+Found", use_container_width=True, caption="Melody")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="pixel-box">
            <p class="pixel-text">🤖 ENTER YOUR NAME</p>
        </div>
        """, unsafe_allow_html=True)
        
        username_input = st.text_input("Username", key="username_input", placeholder="Enter your name", label_visibility="collapsed")
        
        if st.button("Enter", type="primary"):
            if username_input:
                st.session_state.username = username_input
                st.session_state.logged_in = True
                update_github_log(username_input)
                st.rerun()
            else:
                st.error("Please enter a username.")

# 2. TRANSLATION PAGE (for all logged-in users)
else:
    st.write_stream(typing_animation("Tiny Machine Translation"))
    st.markdown(f"Welcome, **{st.session_state.username}**!")

    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = ""

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="pixel-box" style="border-color: #ff8c42;">
            <p class="pixel-text" style="color: #ff8c42;">📝 INPUT TEXT</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.input_text = st.text_area(
            "English Entry Option",
            value=st.session_state.input_text,
            height=200,
            placeholder="Enter English text here...",
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("""
        <div class="pixel-box" style="border-color: #90EE90;">
            <p class="pixel-text" style="color: #90EE90;">🌍 TRANSLATED TEXT</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_area(
            "Translated Text",
            value=st.session_state.translated_text,
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )

    btn_col1, btn_col2, _ = st.columns([1, 1, 4])

    with btn_col1:
        if st.button("Translate", type="primary"):
            if st.session_state.input_text:
                st.markdown("""
                <div class="pixel-box" style="margin-top: 10px;">
                    <p class="pixel-text" style="color: #ff8c42; text-align: center;">
                        🔄 TRANSLATION IN PROGRESS
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                loading_steps = [
                    ("🔄 INITIALIZING...", 10),
                    ("🔄 PROCESSING TEXT...", 25),
                    ("🔄 CONNECTING TO MODEL...", 50),
                    ("🔄 GENERATING TRANSLATION...", 75),
                    ("🔄 FINALIZING RESULT...", 95)
                ]
                
                for message, progress in loading_steps:
                    status_text.markdown(f"""
                    <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
                                font-size: 10px; color: #FFFFFF; text-shadow: 2px 2px 0px #000000;">
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
                    progress_bar.progress(progress)
                    time.sleep(0.3)
                
                translation_result = get_translation(st.session_state.input_text)
                st.session_state.translated_text = translation_result
                
                status_text.markdown("""
                <div style="text-align: center; font-family: 'Press Start 2P', monospace; 
                             font-size: 10px; color: #4CAF50; text-shadow: 2px 2px 0px #000000;">
                    ✅ TRANSLATION COMPLETE!
                </div>
                """, unsafe_allow_html=True)
                progress_bar.progress(100)
                time.sleep(0.5)
                
                progress_bar.empty()
                status_text.empty()
                
                st.rerun()
            else:
                st.warning("Please enter some text to translate.")
    
    with btn_col2:
        if st.button("Log Out"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown("""
    <div class="pixel-box" style="margin-top: 30px;">
        <p class="pixel-text" style="font-size: 8px; color: #ffcccb; text-align: center;">
            ⚠️ DISCLAIMER: This model may produce inaccurate or incorrect translations. 
            Please verify important translations with reliable sources.
        </p>
    </div>
    """, unsafe_allow_html=True)


