from openai import OpenAI
import streamlit as st
from Home import setOpenaiModel

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Display the chat history
for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Sidebar settings to control the toggle
with st.sidebar:
    settings_expander = st.expander("Settings", icon=":material/settings:", expanded=True)

    with settings_expander:
        new_model = st.toggle(":material/bolt: Use newer model", value=st.session_state["new_model_state"])

        if new_model != st.session_state["new_model_state"]:
            st.session_state["new_model_state"] = new_model
            if new_model:
                setOpenaiModel("o1-mini")
            else:
                setOpenaiModel("gpt-4o")

st.warning(st.session_state.get("openai_model", "No model selected"))

# Handle user input and generate assistant response
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )
        response = st.write_stream(stream)  # Assuming write_stream handles output correctly
    st.session_state.messages.append({"role": "assistant", "content": response})

