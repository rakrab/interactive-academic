import streamlit as st

def about_tab():
    with st.sidebar:
        pass
    
    # st.info("Welcome! You authenticated succesfully!", icon=":material/celebration:")

    st.markdown("### About <span style='color:#526d89'>PEN</span>", unsafe_allow_html=True)

    what_is_pen = st.expander("What is PEN?", icon=":material/help:", expanded=False)

    with what_is_pen:
        st.markdown("""
        <span style='color:#526d89'>PEN</span> is an AI-assisted Notebook application aimed at students.
        It is intended to help students and anybody else who may need study notes write and understand them.
        Regardless of this, it can make mistakes and any important information should still be cross-referenced.
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

    # changelog = st.expander("Changelog", icon=":material/published_with_changes:", expanded=False)

    st.markdown("### Changelog :material/published_with_changes:")
    st.caption("Changes marked with :material/warning: are experimental")
    st.caption("Changes marked with :material/bug_report: are buggy")

    with st.expander("irel-03", icon=":material/radio_button_checked:"):
        st.markdown("""
        - **General**
            - Improved scaling :material/warning:
        - **Chat**
            - Added complexity
        """)

    with st.expander("irel-02", icon=":material/radio_button_unchecked:"):
        st.markdown("""
            - **General**
                - Improved authentication system
                - Added access tiers :material/warning:
                - Fixed persistence
                - Removed pages in favor of tabs
                - Removed sidebar
            - **Chat**
                - Moved settings into popover
                - Added full integration with notepad
            - **Notepad**
                - Improved reword QOL
                - Added word and character counts
        """)

    with st.expander("preview-01", icon=":material/unradio_button_checked:"):
        st.markdown("""
        - **General**
            - Added Home
            - Added Notepad
            - Added Chat
            - Added authentication system
        - **Home**
            - Added descriptions
        - **Notepad**
            - Added autocomplete
            - Added reword
            - Added saving and loading as .txt
        - **Chat**
            - Added toggle for models
            - Added topics :material/warning:
        """)