import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid

def generate_thread_id():
    return str(uuid.uuid4())

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def resetchat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(thread_id)
    st.session_state['message_history']=[]


def load_conversation(thread_id):
    state = chatbot.get_state(
        config={"configurable": {"thread_id": thread_id}}
    )
    return state.values.get("messages", [])


if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=[]


add_thread(st.session_state['thread_id'])




st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    resetchat()

st.sidebar.header("My Conversations")


for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(
    f"Chat {thread_id[:8]}",
    key=thread_id):
        st.session_state['thread_id']=thread_id
        messages=load_conversation(thread_id)

        temp_messages=[]
        for mess in messages:
            if isinstance(mess, HumanMessage):
                temp_messages.append({'role':'user','content':mess.content})
            else:
                temp_messages.append({'role':'assistant','content':mess.content[0]['text']})


        st.session_state['message_history']=temp_messages









Config={'configurable':{'thread_id':st.session_state['thread_id']}}




for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input=st.chat_input("type here")

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)


    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            (
                part["text"]
                for chunk, _ in chatbot.stream(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=Config,
                    stream_mode="messages",
                )
                for part in chunk.content
                if part.get("type") == "text"
            )
        )


    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message}
    )


