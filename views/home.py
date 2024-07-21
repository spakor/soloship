import requests
import streamlit as st
from streamlit_extras.colored_header import colored_header

from llm.helper import OCR_URL, UPSTAGE_API_TOKEN, handle_questionnaire
from prompts.context import LIST_OF_QUESTIONS

# --- Module vars ---
TOTAL_QUESTIONS = len(LIST_OF_QUESTIONS)

# -- Hero Secion --
col1, _ = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/soloship.png")


st.subheader(
    "Your :violet[brilliant] idea deserves a business. Let's get started!",
    anchor=False,
)


if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "step" not in st.session_state:
    st.session_state.step = 0
if "responses" not in st.session_state:
    st.session_state.responses = [""] * TOTAL_QUESTIONS
if "response_chunks" not in st.session_state:
    st.session_state.response_chunks = []
if "response_dict" not in st.session_state:
    st.session_state.response_dict = {}
if "regenerated " not in st.session_state:
    st.session_state.regenerated = False
if "document_ocr" not in st.session_state:
    st.session_state.document_ocr = None
if "document_ocr_processing" not in st.session_state:
    st.session_state.document_ocr_processing = False


# -- Questionnaire Dialog--
@st.experimental_fragment
def show_questionnaire():
    last_question_index = TOTAL_QUESTIONS - 1

    if not st.session_state.submitted == True:
        # --- Session related to the questionnaire ---
        if "step" not in st.session_state:
            st.session_state.step = 0
        if "responses" not in st.session_state:
            st.session_state.responses = [""] * TOTAL_QUESTIONS

        # --- Setting the progress bar ---
        progress = (st.session_state.step + 1) / TOTAL_QUESTIONS
        st.progress(progress)

        # --- Setting the Questions and setting the Answer ---
        # Writes the question according to the step (index) the user is currently on
        st.write(LIST_OF_QUESTIONS[st.session_state.step])
        # Sets the answer accordining to the step the user is currently on
        st.session_state.responses[st.session_state.step] = st.text_area(
            f"Question {st.session_state.step + 1} / {TOTAL_QUESTIONS}",
            key=f"question_{st.session_state.step}",
            # If a value has already been given for the question prior to submission it will be retrieved.
            value=st.session_state.responses[st.session_state.step],
        )

        # --- Creating the back & next buttons ---

        back, _, next = st.columns(3, gap="large")

        prev_disabled = st.session_state.step == 0
        if st.session_state.step != 0:
            if back.button(
                "back",
                type="primary",
                disabled=prev_disabled,
                use_container_width=True,
                key="back-button",
            ):
                st.session_state.step -= 1
                st.rerun()

        if st.session_state.step < last_question_index:
            if next.button(
                "next", type="primary", use_container_width=True, key="next-button"
            ):
                st.session_state.step += 1
                st.rerun()

        # --- Setting the submit button ---
        if st.session_state.step == last_question_index:
            if any(response != "" for response in st.session_state.responses):
                if next.button(
                    "submit",
                    type="primary",
                    use_container_width=True,
                ):
                    st.session_state.submitted = True
                    st.rerun()

            if all(response == "" for response in st.session_state.responses):
                if next.button("submit", type="primary", use_container_width=True):
                    st.error(
                        "Please answer at least one question.",
                        icon=":material/warning:",
                    )


# --- Send Responses to LLM --- #
# def send_to_llm():
#     if len(st.session_state.response_chunks) == 0 or st.session_state.regenerated:
#         with st.spinner("Loading..."):
#             responses_dict = {
#                 LIST_OF_QUESTIONS[i]: st.session_state.responses[i]
#                 for i in range(TOTAL_QUESTIONS)
#             }
#             handle_questionnaire(responses_dict)
#             col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")

#             with col1:
#                 show_start_over_button()
#             with col4:
#                 show_re_gen_button()


# def show_existing_response():
#     if len(st.session_state.response_chunks) > 0:
#         # response_text = "".join(st.session_state.response_chunks)
#         for prompt, text in st.session_state.response_dict.items():
#             st.write(prompt)
#             st.write(text)
#         col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")

#         with col1:
#             show_start_over_button()
#         with col4:
#             show_re_gen_button()


def show_existing_response():
    placeholder = st.empty()
    with placeholder.container(height=700, border=False):
        if len(st.session_state.response_dict) > 0 and not st.session_state.regenerated:
            with st.container():
                for prompt, text in st.session_state.response_dict.items():
                    st.subheader(f":violet[{prompt}]")
                    st.write(text)
                    st.divider()

    col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")
    with col1:
        show_start_over_button()
    with col4:
        show_regenerate_button()


def send_to_llm():
    placeholder = st.empty()
    with placeholder.container(height=700, border=False):
        if st.session_state.regenerated:
            # need to reset
            st.session_state.regenerated = False
        st.session_state.response_chunks = []  # Clear previous chunks
        with st.spinner("Loading..."):
            responses_dict = {
                LIST_OF_QUESTIONS[i]: st.session_state.responses[i]
                for i in range(TOTAL_QUESTIONS)
            }
            handle_questionnaire(responses_dict)
        st.session_state.submitted = False

    # TODO: Have a way we can regenerate the button at the bottom, cause after the second regnerate
    # they don't clear until code reaches here and w don't want to re-run the whole page just for it.
    button_placeholder = st.empty()
    with button_placeholder.container():
        col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")
        with col1:
            show_start_over_button()
        with col4:
            show_regenerate_button()


@st.experimental_fragment
def show_regenerate_button():
    if st.button("Regenerate", type="primary"):
        st.session_state.response_chunks = []
        st.session_state.regenerated = True
        st.session_state.submitted = True
        st.rerun()


@st.experimental_fragment
def show_start_over_button():
    if st.button("Start Over", type="primary"):
        st.session_state.clear()
        st.rerun()


# --- DOCUMENT LOADER
# Function to extract text from an uploaded document using OCR
def extract_document_ocr(uploaded_file):
    headers = {"Authorization": f"Bearer {UPSTAGE_API_TOKEN}"}
    files = {"document": uploaded_file}
    print("sending a request to the OCR ....")
    response = requests.post(OCR_URL, headers=headers, files=files)
    response_json = response.json()
    return response_json.get("text")


@st.experimental_fragment
def show_document_upload():
    with st.expander("Document Upload (Optional)"):
        uploaded_file = st.file_uploader(
            "You can upload a document such as a CV or a business proposal (optional)",
            help="This can help the AI have more information on your experience.",
            type=["JPEG", "PNG", "BMP", "PDF", "TIFF", "HEIC"],
            accept_multiple_files=False,
        )
        if (
            uploaded_file is not None
            and st.session_state.document_ocr is None
            and not st.session_state.document_ocr_processing
        ):
            st.session_state.document_ocr_processing = True
            with st.spinner("Uploading your document..."):
                st.session_state.document_ocr = extract_document_ocr(uploaded_file)
            st.session_state.document_ocr_processing = False


# --- Questionnaire ---
if not st.session_state.submitted and len(st.session_state.response_dict) == 0:
    show_questionnaire()
    show_document_upload()

# --- Handle Responses ---
if st.session_state.submitted or st.session_state.regenerated:
    send_to_llm()

else:
    show_existing_response()
