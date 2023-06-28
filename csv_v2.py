import os
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import pandas as pd


# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

# Create Streamlit app
st.title("CSV Agent with Langchain")
st.write("Upload your CSV file and ask questions about the data!")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("File Uploaded Successfully!")
    st.write(df.head())
    
    # Create CSV Agent
    agent = create_csv_agent(OpenAI(temperature=0), uploaded_file.name, verbose=True)
    
    # Ask questions
    question = st.text_input("Ask a question about the data:")
    
    if st.button("Ask"):
        response = agent.run(question)
        st.write("Question:", question)
        st.write("Answer:", response)
