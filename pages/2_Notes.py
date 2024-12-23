from openai import OpenAI
import streamlit as st
import pyperclip

##### HELPER FUNCTIONS

@st.dialog("Upload a file (.txt)", width="small")
def uploadFileDialog():
    uploaded_file = st.file_uploader("Upload", type="txt", label_visibility="collapsed", accept_multiple_files=False)
    if uploaded_file is not None:
        try:
            st.session_state["notepad"] = uploaded_file.read().decode("utf-8")
            st.success("File loaded successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error loading file: {e}")

def reword(text, tone):
    full_prompt = (
        f"You are an AI which is designed to reword text in different tones for academic notes."
        f"The current content of the academic notes is as follows: {st.session_state['notepad']}\n\n"
        f"Use it as context. The text for you to reword is as follows: '{text}'"
        f"Please reword the text using {tone} language."
        f"It is crucial that you output only the rewritten version of the given sentence"
        f"with no changes to the meaning, and no content except the sentence"
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
    st.session_state["reword_output"] = output

@st.dialog("Reword", width="small")
def rewordDialog():
    input_text = st.text_area("Input")

    tone = st.radio("Tone",
    [":material/group: Casual", ":material/work: Formal", ":material/school: Consultative"],
    horizontal=True,
    label_visibility="collapsed")

    col1, col2 = st.columns([5,1])
    with col1:
        generate_button = st.button("Generate", icon=":material/autorenew:", use_container_width=True)
    with col2:
        copy_button = st.button("", icon=":material/content_copy:", use_container_width=True)
    
    if generate_button:
        reword(input_text, tone.split(":")[-1])

    if copy_button:
        pyperclip.copy(st.session_state["reword_output"])

    output_text = st.text_area("Output", disabled=True, value=st.session_state["reword_output"])

def insertAutocomplete():
    st.session_state["notepad"] += st.session_state["autocomplete_output"] + " "
    st.session_state["autocomplete_output"] = ""

def autocomplete():
    full_prompt = (
        f"You are an AI which is designed to autocomplete sentences for academic notes."
        f"The current content of the academic notes is as follows: {st.session_state['notepad']}\n\n"
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
    # st.rerun()

#####


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

notepad = st.text_area("Notepad", 
    height=420,
    value=st.session_state["notepad"],
    label_visibility="collapsed")

autocomplete_output_notif = st.empty()
if st.session_state["autocomplete_output"] != "":
    autocomplete_output_notif.info(st.session_state["autocomplete_output"], icon=":material/hotel_class:")

with st.sidebar:
    col1, col2 = st.columns([5,1])

    with col1:
        autocomplete_button = st.button("Autocomplete", icon=":material/hotel_class:", on_click=autocomplete, use_container_width=True)
    
    with col2:
        autocomplete_insert_button = st.button("", icon=":material/chevron_right:", on_click=insertAutocomplete, disabled=(st.session_state["autocomplete_output"] == ""))
        
    reword_button = st.button("Reword", icon=":material/history_edu:", on_click=rewordDialog, use_container_width=True)

    save_file_button = st.download_button("Save as file (.txt)", st.session_state["notepad"], icon=":material/save_as:", use_container_width=True)
    load_file_button = st.button("Load from file (.txt)", icon=":material/upload_file:", use_container_width=True)

    if load_file_button:
        uploadFileDialog()

if notepad != st.session_state["notepad"]:
    st.session_state["notepad"] = notepad