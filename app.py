import streamlit as st
import requests
import time
import re

# Backend server endpoint (replace with your backend's actual URL)
BACKEND_URL = "http://127.0.0.1:8000"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "username" not in st.session_state:
    st.session_state.username = None

# Function to detect and convert URLs in text to hyperlinks
def convert_urls_to_links(text):
    url_regex = r'(https?://\S+)'
    return re.sub(url_regex, r'<a href="\1" target="_blank">\1</a>', text)

# Prompt user to log in with a username
if not st.session_state.username:
    st.session_state.username = st.text_input("Enter your username to join the chat:")

if st.session_state.username:
    # Display chat title
    st.markdown(
        f"<h1 style='text-align: center;'>Live Chat Room</h1>",
        unsafe_allow_html=True,
    )

    # Fetch messages from backend
    def fetch_messages():
        try:
            response = requests.get(f"{BACKEND_URL}/messages/fetch")
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            st.error(f"Error fetching messages: {e}")
        return []

    # Send message to backend
    def send_message(username, content):
        try:
            payload = {"role": username, "content": content}
            requests.post(f"{BACKEND_URL}/messages/send", json=payload)
        except Exception as e:
            st.error(f"Error sending message: {e}")

    # Display new chat messages with styled bubbles
    def display_new_messages(new_messages):
        for message in new_messages:
            formatted_content = convert_urls_to_links(message['content'])
            if message["role"] == st.session_state.username:
                # User's own message (right-aligned)
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: flex-end; align-items: center; margin: 10px 0;">
                        <div style="max-width: 70%; background-color: #DCF8C6; border-radius: 15px; padding: 10px; text-align: left;">
                            {formatted_content}
                        </div>
                        <img src="https://via.placeholder.com/40" alt="Profile" style="border-radius: 50%; margin-left: 10px;">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                # Other user's message (left-aligned)
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: flex-start; align-items: center; margin: 10px 0;">
                        <img src="https://via.placeholder.com/40" alt="Profile" style="border-radius: 50%; margin-right: 10px;">
                        <div style="max-width: 70%; background-color: #E5E5EA; border-radius: 15px; padding: 10px; text-align: left;">
                            {formatted_content}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # Poll for new messages and update the chat history
    def update_chat():
        new_messages = fetch_messages()
        if len(new_messages) > len(st.session_state.messages):
            # Determine only the truly new messages
            start_index = len(st.session_state.messages)
            st.session_state.messages = new_messages
            display_new_messages(new_messages[start_index:])

    # Initial display of chat history
    display_new_messages(st.session_state.messages)

    # Input for sending new messages
    if prompt := st.chat_input("Type your message and press Enter:"):
        # Convert URLs in the input message to clickable links
        formatted_prompt = convert_urls_to_links(prompt)
        
        # Display the user's message immediately
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end; align-items: center; margin: 10px 0;">
                <div style="max-width: 70%; background-color: #DCF8C6; border-radius: 15px; padding: 10px; text-align: left;">
                    {formatted_prompt}
                </div>
                <img src="https://via.placeholder.com/40" alt="Profile" style="border-radius: 50%; margin-left: 10px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.session_state.messages.append({"role": st.session_state.username, "content": prompt})
        send_message(st.session_state.username, prompt)

    
    # Polling for updates every second
    while True:
        time.sleep(1)  # Adjust as needed for faster/slower updates
        update_chat()
