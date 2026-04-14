import streamlit as st
from rag import ask_question

st.set_page_config(
    page_title="Enterprise Knowledge Base",
    page_icon="📚"
)

st.title("Enterprise Knowledge Base Q&A")

query = st.text_input("Ask your question")

if st.button("Ask"):

    if query:
        with st.spinner("Generating answer..."):
            answer = ask_question(query)

        st.success("Answer")
        st.write(answer)