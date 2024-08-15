import streamlit as st 
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.google_gemini import GoogleGemini
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
#set up gemini llm 
# create an LLM by instantiating OpenAI object, and passing API token
llm = GoogleGemini(api_key=api_key)

# create PandasAI object, passing the LLM


st.title("Prompt-driven data analysis with PandasAI")

#file handling

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    sdf = SmartDataframe(df, config={"llm": llm})
    st.write(df.head(3))
    prompt = st.text_area("Enter your prompt:")
    
#query handling

    # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(sdf.chat(prompt))
        else:
            st.warning("Please enter a prompt.")