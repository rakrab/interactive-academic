import streamlit as st

st.set_page_config(page_title="Home", page_icon=":material/home:")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"
    # st.session_state["openai_model"] = "o1-mini"

# Initialize session state for the toggle if it doesn't exist yet
if "new_model_state" not in st.session_state:
    st.session_state["new_model_state"] = False  # Default to the older model

if "messages" not in st.session_state:
    st.session_state.messages = []

def setOpenaiModel(model):
    st.session_state["openai_model"] = model;

st.warning(st.session_state["openai_model"])