import streamlit as st
from libs.auth import lock_page
from tabs.Notes import notes_tab
from tabs.Chat import chat_tab
from tabs.About import about_tab

st.set_page_config(page_title="PEN", layout="wide")

avatars = {"user":":material/person:", "assistant":":material/robot_2:"}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

###############################################
## Pre Authentication
###############################################

lock_page()

st.markdown("""
<style>

        /* Remove blank space at top and bottom */ 
        .block-container {
            padding-top: 2rem;
            padding-bottom: 1rem;
        }
        
        /* Make the toolbar transparent and the content below it clickable */ 
        .st-emotion-cache-18ni7ap {
            pointer-events: none;
            background: rgb(255 255 255 / 0%)
            }
        .st-emotion-cache-zq5wmm {
            pointer-events: auto;
            background: rgb(255 255 255);
            border-radius: 5px;
            }

        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            padding-top: 1.4em;
            padding-bottom: 1em;
            margin-left: 0.3em;
            margin-right: 0.3em;
            font-weight: bold;
            font-size: 1.3rem;
        }
</style>
""", unsafe_allow_html=True)

###############################################
## Post Authentication - Initialization
###############################################

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"
    # st.session_state["openai_model"] = "o1-mini"

if "notepad" not in st.session_state:
    st.session_state["notepad"] = ""

if "topics" not in st.session_state:
    st.session_state["topics"] = []  # Default to no specialization

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "autocomplete_output" not in st.session_state:
    st.session_state["autocomplete_output"] = ""

if "reword_output" not in st.session_state:
    st.session_state["reword_output"] = ""

###############################################
## Post Authentication - Interface
###############################################

home, notes, chat, about = st.tabs(["🏠 Home", "🗒️ Notes", "💬 Chat", "❔ About"])
with home:
    st.header("Hi :)")
    st.markdown("Please click the tabs at the top to use PEN, the landing page isnt done yet :material/favorite:")
with notes:
    notes_tab()
with chat:
    chat_tab()
with about:
    about_tab()

