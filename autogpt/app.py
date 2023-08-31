import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ["OPENAI_API_KEY"]

# app framework
st.title('🦜️🔗 YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['title'],
    template = 'Write me a Youtube Video title about {title}'
)

script_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a Youtube Video Script for the title: {topic}'
)

# llms
llm = OpenAI(temperature=0.6)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)

# show stuff to the screen if there's a prompt
if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)