import streamlit as st
import bcrypt

usernames = st.secrets.AUTH.USERNAMES
access_tokens = st.secrets.AUTH.ACCESS_TOKENS

def lock_page():
    if st.session_state["authenticated"] == False:

        st.error("You are not authenticated", icon=":material/lock:")
        username = st.text_input("Username", label_visibility="collapsed", placeholder="Username")
        col1, col2 = st.columns([13,1])
        with col1:
            access_token = st.text_input("Access Token", label_visibility="collapsed", placeholder="Access Token", type="password")
        with col2:
            login_button = st.button("", icon=":material/login:", use_container_width=True)

        if login_button and username in usernames:
            idx = usernames.index(username)
            if bcrypt.checkpw(access_token.encode('utf-8'), access_tokens[idx].encode('utf-8')):
                st.session_state["authenticated"] = True
                st.rerun()

        st.stop()

