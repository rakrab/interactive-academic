import streamlit as st

def lock_page():
    if st.session_state["authenticated"] == False:
        st.error("You are not authenticated", icon=":material/lock:")
        col1, col2 = st.columns([13,1])
        with col1:
            access_token = st.text_input("Access Token", label_visibility="collapsed", placeholder="Access Token", type="password")
        with col2:
            login_button = st.button("", icon=":material/login:")

        if login_button:
            if access_token in st.secrets.AUTH.ACCESS_TOKENS:
                st.session_state["authenticated"] = True
                st.rerun()

        st.stop()