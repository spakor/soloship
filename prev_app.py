# NOTE:
# !!!!!!!THIS FILE WILL BE DEPRECATED!!!!
import requests
import os
import streamlit as st
from openai import OpenAI


from prompts.context import LIST_OF_QUESTIONS, MULTI_SYS_PROMPT, SYSTEM_CONTEXT


# Constants
BASE_URL = "https://api.upstage.ai/v1/"
CHAT_URL = BASE_URL + "solar"
OCR_URL = BASE_URL + "document-ai/ocr"
SOLAR_MODEL = "solar-1-mini-chat"

# Environment Variables
UPSTAGE_API_TOKEN = os.getenv("UPSTAGE_API_TOKEN")

# OpenAI Client Initialization
client = OpenAI(api_key=UPSTAGE_API_TOKEN, base_url=CHAT_URL)

p1 = st.Page("page1.py", title="Home", icon=":material/rocket_launch:")
pages = st.navigation([p1])
pages.run()

# Streamlit app
st.title("Soloship :rocket:")


# Function to create a chat stream
def create_chat_stream(messages: list[dict], model: str = SOLAR_MODEL):
    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


# Function to extract text from an uploaded document using OCR
def extract_document_ocr(uploaded_file):
    headers = {"Authorization": f"Bearer {UPSTAGE_API_TOKEN}"}
    files = {"document": uploaded_file}
    print("sending a request to the OCR ....")
    response = requests.post(OCR_URL, headers=headers, files=files)
    response_json = response.json()
    return response_json.get("text")


# Function to convert a response dictionary to a formatted string
def convert_response_to_string(response):
    return "\n".join(f"{k}: {v}" for k, v in response.items())


# Function to reset responses
def reset_responses():
    st.session_state.step = 0
    st.session_state.responses = [""] * len(LIST_OF_QUESTIONS)
    st.session_state.document_ocr = None
    st.session_state.document_ocr_processing = False
    st.session_state.response_chunks = []
    st.session_state.response_text = ""


# Function to display the questions one by one
def display_questions():
    questions = LIST_OF_QUESTIONS

    # Initialize session state variables
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "responses" not in st.session_state:
        st.session_state.responses = [""] * len(questions)
    if "document_ocr" not in st.session_state:
        st.session_state.document_ocr = None
    if "document_ocr_processing" not in st.session_state:
        st.session_state.document_ocr_processing = False
    if "response_chunks" not in st.session_state:
        st.session_state.response_chunks = []

    # Display progress bar
    progress = (st.session_state.step + 1) / len(questions)
    st.progress(progress)

    # Display current question
    st.markdown(
        f"<div style='word-wrap: break-word;'>{questions[st.session_state.step]}</div>",
        unsafe_allow_html=True,
    )
    # st.text(questions[st.session_state.step])
    st.session_state.responses[st.session_state.step] = st.text_area(
        f"Question {st.session_state.step + 1} / {len(questions)}",
        value=st.session_state.responses[st.session_state.step],
        key=f"answer_{st.session_state.step}",
    )

    col1, _, col3 = st.columns([1, 6, 1])

    # File uploader for optional CV upload
    uploaded_file = st.file_uploader(
        "Upload your CV (optional)",
        help="This can help the AI have more information on your experience.",
    )
    if (
        uploaded_file is not None
        and st.session_state.document_ocr is None
        and not st.session_state.document_ocr_processing
    ):
        st.session_state.document_ocr_processing = True
        with st.spinner("Uploading your CV..."):
            st.session_state.document_ocr = extract_document_ocr(uploaded_file)
        st.session_state.document_ocr_processing = False

    # "Previous" button
    prev_disabled = st.session_state.step == 0
    if col1.button("←", disabled=prev_disabled):
        st.session_state.step -= 1
        st.rerun()

    # Next Button or Submit Button
    if st.session_state.step < len(questions) - 1:
        if col3.button("→"):
            st.session_state.step += 1
            st.rerun()
    else:
        col4, _, col6 = st.columns([1, 6, 1])
        if col6.button("Submit") and st.session_state.responses:
            with st.spinner("Loading..."):
                responses_dict = {
                    questions[i]: st.session_state.responses[i]
                    for i in range(len(questions))
                }
                string_result = convert_response_to_string(responses_dict)
                system_prompt = {
                    "role": "system",
                    "content": SYSTEM_CONTEXT,
                }
                user_prompt = {
                    "role": "user",
                    "content": f"Here is an overview of my professional experience: {string_result}",
                }

                messages = [user_prompt]

                if st.session_state.document_ocr:
                    messages.append(
                        {
                            "role": "user",
                            "content": f"Here is a document I uploaded, going over my professional experience: {st.session_state.document_ocr}.",
                        }
                    )
                for prompt in MULTI_SYS_PROMPT:
                    prompt_type, i = prompt
                    multi_system_prompt = {
                        "role": "user",
                        "content": i,
                    }
                    updated_messages = [system_prompt, *messages, multi_system_prompt]

                    # Function to yield and accumulate chunks
                    def stream_chunks():
                        for chunk in create_chat_stream(updated_messages):
                            st.session_state.response_chunks.append(chunk)
                            yield chunk

                    st.write(prompt_type)
                    st.write_stream(stream_chunks)

                    response_text = "".join(st.session_state.response_chunks)
                    st.session_state.response_text = response_text


display_questions()
if "response_text" in st.session_state and st.session_state.response_text:
    st.download_button(
        label="Download Response",
        data=st.session_state.response_text,
        file_name="response.txt",
        mime="text/plain",
        on_click=reset_responses,  # Call reset_responses after download
    )
