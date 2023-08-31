import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from tempfile import NamedTemporaryFile

def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV :chart:")
    st.header("Ask your CSV :chart:")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        with NamedTemporaryFile(mode='w+b', suffix=".csv") as f:
            f.write(user_csv.getvalue())
            f.flush()
            user_question = st.text_input("Ask a question about your CSV: ")

            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, f.name, verbose=True)

            if user_question is not None and user_question != "":
                response = agent.run(user_question)
                st.write(response)

if __name__ == "__main__":
    main()