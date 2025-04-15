

from langchain_core.prompts import ChatPromptTemplate
# if you want to get output or default output we will use "StrOutputParser"
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
#from dotenv import load_dotenv
import streamlit as st
import os
#load_dotenv()

#os.environ["LANCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt= ChatPromptTemplate.from_messages([
    ("system","can you please ask your queation"),
    ("user","Question:{question}")
])
st.title("Ask Any Question:")
text=st.text_input("Please enter you Question below:")

llm=Ollama(model="llama3.2:1b")
outputparser=StrOutputParser()
chain=prompt|llm|outputparser

if text:
    st.write(chain.invoke({"question":text}))


