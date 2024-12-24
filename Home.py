import streamlit as st
from libs.auth import lock_page

st.set_page_config(page_title="PEN", layout="wide")
avatars = {"user":":material/person:", "assistant":":material/robot_2:"}

if "avatars" not in st.session_state:
    st.session_state["avatars"] = avatars

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

###############################################
## Pre Authentication
###############################################

lock_page()

###############################################
## Post Authentication
###############################################
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"
    # st.session_state["openai_model"] = "o1-mini"

if "notepad" not in st.session_state:
    st.session_state["notepad"] = ""

if "new_model_state" not in st.session_state:
    st.session_state["new_model_state"] = False  # Default to the older model

if "topics_state" not in st.session_state:
    st.session_state["topics_state"] = []  # Default to no specialization

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "autocomplete_output" not in st.session_state:
    st.session_state["autocomplete_output"] = ""

if "reword_output" not in st.session_state:
    st.session_state["reword_output"] = ""

st.success("Welcome! You authenticated succesfully!", icon=":material/celebration:")
# st.warning(st.session_state["openai_model"])
# st.warning(st.session_state["notepad"])