from openai import OpenAI
import streamlit as st
from libs.auth import lock_page

avatars = st.session_state["avatars"]

###############################################
## Pre Authentication
###############################################

lock_page()

###############################################
## Post Authentication
###############################################

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.warning("Topics to specialize in are not fully implemented yet!", icon=":material/warning:")

# Display the chat history
for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"], avatar=avatars[message["role"]]):
        st.markdown(message["content"])

# Sidebar settings
with st.sidebar:
    settings_expander = st.expander("Settings", icon=":material/settings:", expanded=True)

    with settings_expander:
        new_model = st.toggle(":material/bolt: Use newer model", value=st.session_state["new_model_state"], help="Slower, but smarter. Useful for programming- and math-related tasks.")

        # Sync new_model to session_state
        if new_model != st.session_state["new_model_state"]:
            st.session_state["new_model_state"] = new_model

        if new_model:
            st.session_state["openai_model"] = "o1-mini"
        else:
            st.session_state["openai_model"] = "gpt-4o"

        topics = st.pills(":material/target: Topics to specialize in", 
            options=[":material/history_edu: History", 
            ":material/science: Science", ":material/calculate: Mathematics",
            ":material/auto_stories: Literature", ":material/public: Geography", 
            ":material/manufacturing: Technology"], 
            selection_mode="multi", default=st.session_state["topics_state"])

        if topics != st.session_state["topics_state"]:
            st.session_state["topics_state"] = topics

# Handle user input and generate assistant response
if prompt := st.chat_input("Send a message!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=avatars["user"]):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=avatars["assistant"]):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )
        response = st.write_stream(stream)  # Assuming write_stream handles output correctly
    st.session_state.messages.append({"role": "assistant", "content": response})

