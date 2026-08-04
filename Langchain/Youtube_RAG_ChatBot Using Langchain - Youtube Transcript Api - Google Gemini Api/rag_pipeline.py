import os
import requests
import http.cookiejar
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from utils import get_video_id, format_docs

def build_rag_chain(video_url: str):
    video_id = get_video_id(video_url)
    if not video_id:
        return None, "Invalid YouTube URL."

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_data = ytt_api.fetch(video_id, languages=['en', 'en-US'])
        full_text = " ".join(item.text for item in transcript_data)
        
        if not full_text.strip():
            return None, "Retrieved transcript is empty."
            
        docs = [Document(page_content=full_text)]
            
    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video."
    except Exception as e:
        error_msg = str(e)
        if "IP" in error_msg or "blocked" in error_msg or "RequestBlocked" in error_msg:
            return None, (
                "YouTube has blocked requests from this IP address.\n\n"
                "### How to fix this:\n"
                "5. Try processing the video again!\n\n"
                "*(Alternatively, try connecting to a VPN or using a different network connection)*"
            )
        return None, f"Error fetching transcript: {error_msg}"


    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2')
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(model='gemini-3.6-flash', temperature=0.2)
    prompt = PromptTemplate(
        template="""
          You are a helpful assistant.
          Answer ONLY from the provided transcript context.
          If the context is insufficient, just say you don't know.

          {context}
          Question: {question}
        """,
        input_variables=['context', 'question']
    )

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })
    
    main_chain = parallel_chain | prompt | llm | StrOutputParser()

    return main_chain, "Success"