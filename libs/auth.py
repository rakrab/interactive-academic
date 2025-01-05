import streamlit as st
import json
import bcrypt

accounts_json = st.secrets.AUTH.ACCOUNTS
accounts = json.loads(accounts_json)

def lock_page():
    if st.session_state["authenticated"] == False:
        err = st.empty()
        err.error("You are not authenticated", icon=":material/lock:")
        username = st.text_input("Username", label_visibility="collapsed", placeholder="Username")
        col1, col2 = st.columns([13,1])
        with col1:
            access_token = st.text_input("Access Token", label_visibility="collapsed", placeholder="Access Token", type="password")
        with col2:
            login_button = st.button("", icon=":material/login:", use_container_width=True)

        if login_button:
            if username in accounts:
                user = accounts[username];
                if bcrypt.checkpw(access_token.encode('utf-8'), user['access_token'].encode('utf-8')):
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    err.error("Invalid Username or Access Token", icon=":material/cancel:")
            else:
                err.error("Invalid Username or Access Token", icon=":material/cancel:")

        st.stop()

