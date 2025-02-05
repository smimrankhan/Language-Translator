import os
from dotenv import load_dotenv

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# # LangSmith tracking
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACKING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT2"] = os.getenv("LANGCHAIN_PROJECT2")

# Prompt template for translation
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates text into different languages."),
        ("user", "Translate the following text to {target_language}: {text}")
    ]
)

# Streamlit framework setup
st.title("Language Translator.AI")
st.write("Translate text into different languages instantly using Ollama API.")

# User input fields
input_text = st.text_area("Enter text to translate:")
target_language = st.text_input("Enter the target language (e.g., French, Spanish, German):")

# OpenAI model initialization
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Translation logic
if st.button("Translate"):
    if input_text and target_language:
        with st.spinner("Translating..."):
            try:
                translation = chain.invoke({"text": input_text, "target_language": target_language})
                st.success("Translation completed!")
                st.text_area("Translated text:", translation, height=200)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please provide both the text to translate and the target language.")


# terminal input command ->
# streamlit run "d:/GENERATIVE AI/app using openai/language_translator.py"