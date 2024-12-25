import streamlit as st
from libs.auth import lock_page

st.set_page_config(page_title="PEN", layout="wide")
st.markdown('<link rel="stylesheet" href="libs/styles.css"', unsafe_allow_html=True)

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
## Post Authentication - Initialization
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

###############################################
## Post Authentication - Interface
###############################################

st.info("Welcome! You authenticated succesfully!", icon=":material/celebration:")

st.markdown("# <span style='color:#526d89'>P</span>redictive <span style='color:#526d89'>E</span>ducational <span style='color:#526d89'>N</span>otebook", unsafe_allow_html=True)

what_is_pen = st.expander("What is PEN?", icon=":material/help:", expanded=False)

with what_is_pen:
    st.markdown("""
    <span style='color:#526d89'>PEN</span> is an AI-assisted Notebook application aimed at students.
    It is intended to help students and anybody else who may need study notes write and understand them.
    While PEN's assistant <span style='color:#526d89'>i-a</span> is capable of problem-solving, especially using the newer model available in settings,
    this is not its intended use case, and as such any important information should be cross-referenced.
    """, unsafe_allow_html=True)

how_was_pen_made = st.expander("How was it made?", icon=":material/code:", expanded=False)

with how_was_pen_made:
    st.markdown("""
    The program you are using right now is made using [Python 3.10](https://www.python.org/).<br>
    The user interface is built on [Streamlit](https://streamlit.io/).<br>
    For all AI features, we use the [OpenAI API](https://openai.com/api/) with models `gpt-4o`
    and `o1` used in conjunction.
    """, unsafe_allow_html=True)

what_are_the_advantages = st.expander("What are the advantages of using it?", icon=":material/trophy:", expanded=False)

with what_are_the_advantages:
    st.markdown("""
    <span style='color:#526d89'>PEN</span> uses the OpenAI API, meaning it has the ChatGPT you know and love
    as its base. The difference lies in the following aspects:
    - Lax limits on usage<br>
        - There are no usage limits for the `gpt-4o` model on <span style='color:#526d89'>PEN</span>.<br>
        - Every user has access to `o1` on <span style='color:#526d89'>PEN</span>, limits depend on your access key.
    <br><br>
    - Easier-to-use AI<br>
        - The assistant will keep information in mind across the two different pages.<br>
        - The assistant will also keep information in mind across the two different models.<br> 
        - Instead of writing out a long prompt, common use-cases are triggered with the press of a button.
    <br><br>
    - Integrated Notes<br>
        - No need to switch tabs or applications to your notes!<br>
        - No need to copy and paste your notes, the assistant uses them as context by default.<br>
    """, unsafe_allow_html=True)

st.divider()

changelog = st.expander("Changelog", icon=":material/published_with_changes:", expanded=False)

with changelog:
    st.markdown("Changelog")