from langchain_openai import ChatOpenAI
# if you want to build a chatbot application ChatPromptTemplate is required
from langchain_core.prompts import ChatPromptTemplate
# if you want to get output or default output we will use "StrOutputParser"
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
key="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"
os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["LANCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt= ChatPromptTemplate.from_messages([
    ("system","can you please ask your queation"),
    ("user","Question:{question}")
])
st.title("Ask Any Question:")
text=st.text_input("ask question:")


llm =ChatOpenAI(model="gpt-3.5-turbo",api_key=key)
outputparser=StrOutputParser()
chain=prompt|llm|outputparser

if text:
    st.write(chain.invoke({"question":text}))


