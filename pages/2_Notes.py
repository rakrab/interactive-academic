import streamlit as st

notepad = st.text_area("Notepad", height=500, label_visibility="collapsed")

with st.sidebar:
    autocomplete_expander = st.expander("Autocomplete", expanded=True, icon=":material/hotel_class:")
    save_file_expander = st.expander("Save as file (.txt)", icon=":material/save_as:")
    load_file_expander = st.expander("Load from file (.txt)", icon=":material/upload_file:")

    with autocomplete_expander:
        st.button("Generate", icon=":material/check:")

    with save_file_expander:
        st.download_button("Download", notepad, icon=":material/download:")

    with load_file_expander:
        st.file_uploader("Upload", type="txt", label_visibility="collapsed")