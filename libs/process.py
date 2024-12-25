import streamlit as st

def process_topics(topics):
    output = [topic.split(":")[-1].strip() for topic in topics]
    return ", ".join(output)