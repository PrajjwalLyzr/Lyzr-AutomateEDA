import os
import lyzr
from PIL import Image
import streamlit as st

# Create a temporary directory if it doesn't exist
if not os.path.exists('tempDir'):
    os.makedirs('tempDir')

# Setup your config
st.set_page_config(
    page_title="LyzrVoice DocuFill",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png"
)

# # Setup your OpenAI API key
# os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

# Setup your OpenAI API key 
api_key = st.sidebar.text_input("API Key", type="password")
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
else:
    # Display a message to prompt user input if the API key is not provided
    st.sidebar.warning("Please enter your API key to proceed.")

# Function definitions (text_to_notes, transcribe, save_uploadedfile, etc.) go here...
st.text_area("Functions go here")
# def save_uploadedfile(uploaded_file):
#     with open(os.path.join('tempDir', uploaded_file.name), "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     return st.success(f"Saved File: {uploaded_file.name} to tempDir")

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply the styles
style_app()

# Load and display the logo
image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("App Title")
st.markdown("### Welcome to the App Title!")
st.markdown("Tiny intro on what the app does")

# Instruction for the users
st.markdown("#### (Start with an emoji here) Clear short instruction")
st.caption('Note:.')

# Start of the main container
with st.container():
    st.text_area("Codes go here")

# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Core to generate notes from transcribed audio. The audio transcription is powered by OpenAI's Whisper model. For any inquiries or issues, please contact Lyzr.
    
    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
    st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)