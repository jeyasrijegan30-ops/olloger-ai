import streamlit as st
import ollama
import re

st.set_page_config(page_title="🤖 Olloger – AI Assistant", layout="centered")

st.title("🤖 Olloger – AI Assistant")
st.write("Ask any question (Maths, GK, Coding, Anything)")

question = st.text_input("Enter your question here:")

if question:
    with st.spinner("Generating answer..."):
        try:
            response = ollama.chat(
                model="phi3",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Olloger AI.\n"
                            "Answer the question clearly.\n"
                            "STRICT FORMAT:\n"
                            "<answer>...</answer>\n"
                            "<explanation>...</explanation>"
                        ),
                    },
                    {"role": "user", "content": question},
                ],
            )

            content = response["message"]["content"]

            # Extract answer & explanation using regex
            answer_match = re.search(r"<answer>(.*?)</answer>", content, re.DOTALL)
            explanation_match = re.search(r"<explanation>(.*?)</explanation>", content, re.DOTALL)

            answer = answer_match.group(1).strip() if answer_match else "Not found"
            explanation = explanation_match.group(1).strip() if explanation_match else "Not found"

            st.subheader("Answer & Explanation")
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"**Explanation:** {explanation}")

        except Exception as e:
            st.error(f"Error: {e}")
