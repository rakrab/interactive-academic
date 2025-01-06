from openai import OpenAI
import streamlit as st
from libs.auth import lock_page
from libs.process import process_topics
from streamlit_extras.bottom_container import bottom 

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
avatars =  {"user":":material/person:", "assistant":":material/robot_2:"}

###############################################
## Helper Functions
###############################################


###############################################
## Post Authentication
###############################################

def chat_tab():

    chat = st.container(height=350, border=False)
    prompt_space, settings_space = st.columns([12,1])
    with prompt_space:
        prompt = st.chat_input("Send a message!")
    with settings_space:  
        settings_popover = st.popover("", icon=":material/settings:")

    with chat:
        # Display the chat history
        for message in st.session_state.get("messages", []):
            with st.chat_message(message["role"], avatar=avatars[message["role"]]):
                st.markdown(message["content"])  
        # Handle user input and generate assistant response
        if prompt:
            with st.chat_message("user", avatar=avatars["user"]):
                st.write(prompt)

            with st.chat_message("assistant", avatar=avatars["assistant"]):
                full_prompt = (
                    f"You are an AI which is designed to advise students."
                    f"You are specialized in {process_topics()}\n\n"
                    f"The current content of the student's academic notes is as follows: {st.session_state['notepad']}\n\n"
                    f"Your prompt is as follows: \n\n{prompt}"
                    )
                full_message = [
                    {"role": "user", "content": full_prompt}
                ]
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages] + full_message,
                    stream=True,
                )
                response = st.write_stream(stream)  # Assuming write_stream handles output correctly
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    with settings_popover:
        # st.warning("Topics to specialize in are not fully implemented yet!", icon=":material/warning:")

        new_model = st.toggle(":material/bolt: Use newer model", help="Slower, but smarter. Useful for programming- and math-related tasks.")

        if new_model:
            st.session_state["openai_model"] = "o1-mini"
        else:
            st.session_state["openai_model"] = "gpt-4o"

        topics = st.pills(":material/target: Topics to specialize in", 
            options=[":material/history_edu: History", 
            ":material/science: Science", ":material/calculate: Mathematics",
            ":material/auto_stories: Literature", ":material/public: Geography", 
            ":material/manufacturing: Technology"], 
            selection_mode="multi")
        
        st.session_state["topics"] = topics
