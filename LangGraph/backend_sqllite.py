from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage , HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import uuid
from dotenv import load_dotenv
import sqlite3

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def chat_node(state: ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {'messages':[response]}


conn=sqlite3.connect(database="chatbot.db" , check_same_thread=False )

checkpointer=SqliteSaver(conn=conn)
config = {"configurable": {"thread_id": "thread-1"}}

graph=StateGraph(ChatState)

graph.add_node('chatnode',chat_node)
graph.add_edge(START,'chatnode')
graph.add_edge("chatnode",END)


chatbot=graph.compile(checkpointer=checkpointer)

# for chunk, _ in chatbot.stream(
#     {"messages": [HumanMessage(content="give me recepes for a cake with chocoalte")]},
#     config=config,
#     stream_mode="messages",
# ):
#     for part in chunk.content:
#         print(part.get("text", ""), end="", flush=True)

def ret_all_thread():
    all_threads=set()

    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)