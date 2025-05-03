import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()

def get_qa_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def ask_question(chain, query):
    return chain.run(query)