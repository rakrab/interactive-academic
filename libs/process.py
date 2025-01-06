import streamlit as st

def process_topics():
    topics = st.session_state["topics"]
    output = [topic.split(":")[-1].strip() for topic in topics]
    return ", ".join(output) if topics else 'general assistance'