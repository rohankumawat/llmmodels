import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# loading the secret key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]

# streamlit framework

st.title('LangChain Demo with OpenAI API')
input_text = st.text_input("Search about any Celebrity")

## initialise openai llm

llm = OpenAI(temperature=0.6)

if input_text:
    st.write(llm(input_text))