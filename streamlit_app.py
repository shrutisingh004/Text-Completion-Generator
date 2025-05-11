import streamlit as st
from completion import TextCompletionGenerator

st.title("Text Completion Generator")

prompt = st.text_input("Enter a sentence to complete:")
if 'generator' not in st.session_state:
    st.session_state.generator = TextCompletionGenerator()

if st.button("Generate"):
    result = st.session_state.generator.complete_text(prompt)
    st.write("**Completion:**")
    st.write(result)
