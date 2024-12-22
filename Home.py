import streamlit as st

st.set_page_config(page_title="Home", layout="wide")
avatars = {"user":":material/person:", "assistant":":material/robot_2:"}

if "avatars" not in st.session_state:
    st.session_state["avatars"] = avatars

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"
    # st.session_state["openai_model"] = "o1-mini"

if "notepad" not in st.session_state:
    st.session_state["notepad"] = ""

# Initialize session state for the toggle if it doesn't exist yet
if "new_model_state" not in st.session_state:
    st.session_state["new_model_state"] = False  # Default to the older model

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "autocomplete_output" not in st.session_state:
    st.session_state["autocomplete_output"] = ""

st.warning(st.session_state["openai_model"])
st.warning(st.session_state["notepad"])