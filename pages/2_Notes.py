from openai import OpenAI
import streamlit as st

def insertAutocomplete():
    st.session_state["notepad"] += st.session_state["autocomplete_output"] + " "

def autocomplete(output_ph, insert_ph):
    full_prompt = (
        f"You are an AI which is designed to autocomplete sentences for notes."
        f"The current content of the notes is as follows: {st.session_state['notepad']}\n\n"
        f"It is crucial that you output only the completion of the last sentence, or"
        f"if the last sentence is finished, it is crucial that you continue the content with only one new sentence."
    )
    try:
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
    except Exception as e:
        st.error(f"Error communicating with OpenAI API: {e}")
        return
    output = response.choices[0].message.content
    st.session_state["autocomplete_output"] = output
    output_ph.info(output, icon=":material/hotel_class:")
    insert_ph.button("", icon=":material/chevron_right:", on_click=insertAutocomplete)


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

notepad = st.text_area("Notepad", 
    height=420,
    value=st.session_state["notepad"],
    label_visibility="collapsed")

autocomplete_output_notif = st.empty()

with st.sidebar:
    col1, col2 = st.columns([5,1])

    with col1:
        autocomplete_button = st.button("Autocomplete", icon=":material/hotel_class:")
    
    with col2:
        autocomplete_insert_button = st.empty()
    
    if autocomplete_button:
        autocomplete(autocomplete_output_notif, autocomplete_insert_button)

    save_file_button = st.download_button("Save as file (.txt)", st.session_state["notepad"], icon=":material/save_as:")
    load_file_expander = st.expander("Load from file (.txt)", icon=":material/upload_file:")

    with load_file_expander:
        uploaded_file = st.file_uploader("Upload", type="txt", label_visibility="collapsed", accept_multiple_files=False)
        if uploaded_file is not None:
                try:
                    st.session_state['notepad'] = uploaded_file.read().decode("utf-8")
                    st.success("File loaded successfully!")
                except Exception as e:
                    st.error(f"Error loading file: {e}")

if notepad != st.session_state["notepad"]:
    st.session_state["notepad"] = notepad