import streamlit as st
import os
from dotenv import load_dotenv

from rag_pipeline import build_rag_chain

# Load environment variables
load_dotenv()

st.set_page_config(page_title="YouTube RAG Chatbot", layout="centered", page_icon="📺")
st.title("📺 YouTube Video RAG Chatbot")

# --- CACHING THE PIPELINE ---
# Caching prevents Streamlit from rebuilding the FAISS index on every chat submission
@st.cache_resource(show_spinner=False)
def get_chain(url):
    return build_rag_chain(url)

# --- SIDEBAR: Video Processing ---
with st.sidebar:
    st.header("1. Input Video")
    youtube_url = st.text_input("Enter YouTube Video URL:")
    process_button = st.button("Process Video")

    if process_button and youtube_url:
        with st.spinner("Downloading transcript and building vector store..."):
            chain, status_msg = get_chain(youtube_url)
            
            if chain:
                st.session_state.video_processed = True
                st.session_state.current_url = youtube_url
                # Reset chat history for a new video
                st.session_state.messages = [] 
                st.success("Video processed! You can now chat.")
            else:
                st.error(status_msg)

    st.write("---")
    
    if st.button("Clear App Cache"):
        st.cache_resource.clear()
        st.success("Cache cleared!")

# Initialize Session State variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

# --- MAIN AREA: Chat Interface ---
st.header("2. Chat with the Video")

# Render previous messages from state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input block
if not st.session_state.video_processed:
    st.info("👈 Please process a YouTube video in the sidebar to start chatting.")
else:
    # Accept user input
    if prompt := st.chat_input("Ask a question about the video..."):
        # Display user message in chat container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Fetch cached chain and generate response
        chain, _ = get_chain(st.session_state.current_url)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = chain.invoke(prompt)
                    st.markdown(response)
                    # Add AI response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")




def format_docs(retrieved_docs):
    """Joins the content of retrieved LangChain documents."""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)