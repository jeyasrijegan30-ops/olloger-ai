import streamlit as st
import ollama

client = ollama.Client()

st.title("🤖 Olloger – AI Assistant")
st.write("Ask any question (Maths, GK, Coding, Anything)")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question:
        response = client.generate(model="llama2", prompt=question)
        st.write("Answer:")
        st.write(response)
