import os
import uuid
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv(
    "N8N_WEBHOOK_URL",
    "http://localhost:5678/webhook/765f700b-7da7-42f9-aa13-887c8f64a338"
)

st.set_page_config(
    page_title="Aura - AI Personal Assistant",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am **Aura**, your personal executive assistant. How can I help you manage your tasks, calendar, emails, or notes today?"}
    ]

with st.sidebar:
    st.title("⚡ Aura Control Panel")
    st.caption("Connected to n8n Multi-Agent Orchestrator")
    st.divider()
    
    st.markdown("### Connected Tools")
    st.markdown("""
    - 📝 **Google Tasks**
    - 📅 **Google Calendar**
    - 📧 **Gmail**
    - 📊 **Google Sheets (Expenses)**
    - 📄 **Google Docs (Notes)**
    - 🔍 **Google Search (SerpApi)**
    - 🧮 **Calculator**
    """)
    
    st.divider()
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat reset. How can I assist you?"}
        ]
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

st.title("⚡ Aura Personal Assistant")
st.caption("Powered by n8n, Gemini & Streamlit")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Aura to do something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Executing requested tools..."):
            try:
                payload = {
                    "name": prompt,
                    "sessionId": st.session_state.session_id
                }
                
                response = requests.post(
                    WEBHOOK_URL,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=90
                )
                
                if response.status_code == 200:
                    if response.text.strip():
                        try:
                            data = response.json()
                            if isinstance(data, dict) and "response" in data:
                                bot_response = data["response"]
                            elif isinstance(data, list) and len(data) > 0 and "output" in data[0]:
                                bot_response = data[0]["output"]
                            else:
                                bot_response = str(data)
                        except Exception:
                            bot_response = response.text
                    else:
                        bot_response = "⚠️ n8n processed the request but returned an empty response."
                        
                    st.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
                    
                else:
                    error_msg = f"⚠️ Server Error ({response.status_code}): {response.text}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    
            except requests.exceptions.Timeout:
                err_text = "⏱️ Request timed out. The agent took too long to run the tools."
                st.error(err_text)
                st.session_state.messages.append({"role": "assistant", "content": err_text})
            except Exception as e:
                err_text = f"❌ Connection Error: Ensure n8n is running. ({str(e)})"
                st.error(err_text)
                st.session_state.messages.append({"role": "assistant", "content": err_text})