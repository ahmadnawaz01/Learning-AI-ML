import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


Config={'configurable':{'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

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
        part["text"]
        for chunk, _ in chatbot.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config=Config,
            stream_mode="messages",
        )
        for part in chunk.content
        if part.get("type") == "text"
    )

    st.session_state["message_history"].append(
    {"role": "assistant", "content": ai_message}
        )


