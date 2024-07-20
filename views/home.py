import streamlit as st
from streamlit_extras.colored_header import colored_header

from llm import helper as llm_helper
from prompts.context import LIST_OF_QUESTIONS

# --- Module vars ---
TOTAL_QUESTIONS = len(LIST_OF_QUESTIONS)

# --- Setting Session State


def generate_session_state():
    if "document_ocr" not in st.session_state:
        st.session_state.document_ocr = None
    if "document_ocr_processing" not in st.session_state:
        st.session_state.document_ocr_processing = False
    if "get_started" not in st.session_state:
        st.session_state.get_started = False
    if "questionnaire_loaded" not in st.session_state:
        st.session_state.questionnaire_loaded = False
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "user_input" not in st.session_state:
        st.session_state.user_input = [""] * TOTAL_QUESTIONS
    if "llm_response_chunks" not in st.session_state:
        st.session_state.llm_response_chunks = []
    if "llm_response_text" not in st.session_state:
        st.session_state.llm_response_text = ""
    if "llm_prompt_dict" not in st.session_state:
        st.session_state.llm_prompt_dict = {}
    if "llm_response_generated" not in st.session_state:
        st.session_state.llm_response_generated = False
    if "response_container" not in st.session_state:
        st.session_state.response_container = st.empty()
    if "response_container_new" not in st.session_state:
        st.session_state.response_container_new = st.empty()


# -- Hero Section --
@st.experimental_fragment
def load_hero_section():
    with st.container():
        col1, _ = st.columns(2, gap="small", vertical_alignment="center")

        with col1:
            st.image("./assets/soloship.png")

        st.subheader(
            "Your :violet[brilliant] idea deserves a business.",
            anchor=False,
        )


@st.experimental_fragment
def load_get_started_button():
    if st.session_state.submitted == False and st.session_state.get_started == False:
        _, col2 = st.columns(2, gap="small", vertical_alignment="bottom")
        with col2:
            if col2.button(
                "Get Started",
                type="primary",
            ):
                st.session_state.get_started = True
                st.rerun()


def optional_ending_buttons():
    restart, _, _, re_generate = st.columns(4, gap="large", vertical_alignment="center")

    if restart.button(
        "Restart", type="primary", use_container_width=True, key="restart_button"
    ):
        st.session_state.clear()
        # st.rerun()

    if re_generate.button(
        "Re-generate",
        type="primary",
        use_container_width=True,
        key="regenerate_button",
    ):
        # re-setting all LLM state sessions
        st.session_state.llm_response_generated = False
        st.session_state.llm_response_chunks = []
        st.session_state.llm_response_text = ""
        st.session_state.llm_prompt_dict = {}
        send_to_llm()
        # st.rerun()


# -- Questionnaire Dialog--
@st.experimental_fragment
def show_questionnaire():
    last_question_index = TOTAL_QUESTIONS - 1
    with st.container(border=True):
        if not st.session_state.submitted == True:

            # --- Setting the progress bar ---
            progress = (st.session_state.step + 1) / TOTAL_QUESTIONS
            st.progress(progress)

            # --- Setting the Questions and setting the Answer ---
            # Writes the question according to the step (index) the user is currently on
            st.write(LIST_OF_QUESTIONS[st.session_state.step])
            # Sets the answer accordining to the step the user is currently on
            st.session_state.user_input[st.session_state.step] = st.text_area(
                f"Question {st.session_state.step + 1} / {TOTAL_QUESTIONS}",
                key=f"question_{st.session_state.step}",
                # If a value has already been given for the question prior to submission it will be retrieved.
                value=st.session_state.user_input[st.session_state.step],
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
                    "next",
                    type="primary",
                    use_container_width=True,
                    key="next-button",
                ):
                    st.session_state.step += 1
                    st.rerun()

            # --- Setting the submit button ---
            if st.session_state.step == last_question_index:
                if any(response != "" for response in st.session_state.user_input):
                    if next.button(
                        "submit",
                        type="primary",
                        use_container_width=True,
                    ):
                        st.session_state.submitted = True
                        st.rerun()

                if all(response == "" for response in st.session_state.user_input):
                    if next.button("submit", type="primary", use_container_width=True):
                        st.error(
                            "Please answer at least one question.",
                            icon=":material/warning:",
                        )
            st.session_state.questionnaire_loaded = True


# --- Upload document component ---
@st.experimental_fragment
def process_uploaded_document():
    st.write(
        "If you have a CV or a business propsal already written, you can upload it as well."
    )
    with st.popover("Upload", use_container_width=False):
        uploaded_file = st.file_uploader(
            label="Upload your document.",
            type=["jpg", "png", "bmp", "tiff", "heic"],
            accept_multiple_files=False,
        )

        if (
            uploaded_file is not None
            and st.session_state.document_ocr is None
            and not st.session_state.document_ocr_processing
        ):
            st.session_state.document_ocr_processing = True
            with st.spinner("Uploading your CV..."):
                st.session_state.document_ocr = uploaded_file
            st.session_state.document_ocr_processing = False


# --- Send Responses to LLM --- #
def send_to_llm():
    responses_dict = {
        LIST_OF_QUESTIONS[i]: st.session_state.user_input[i]
        for i in range(TOTAL_QUESTIONS)
    }
    llm_helper.handle_questionnaire(responses_dict)
    st.session_state.llm_response_generated = True


def load_llm_response():
    show_buttons = False
    placeholder = st.empty()
    with st.spinner("Launching your request to Star :star: Command..."):
        with placeholder.container():
            if st.session_state.llm_response_generated:
                for prompt_type, text in st.session_state.llm_prompt_dict.items():
                    placeholder.write(prompt_type)
                    placeholder.write(text)

                show_buttons = True

        placeholder.empty()
        send_to_llm()
        show_buttons = True

    if show_buttons:
        optional_ending_buttons()


generate_session_state()
load_hero_section()
load_get_started_button()
if st.session_state.get_started == True and st.session_state.submitted == False:
    show_questionnaire()
if st.session_state.submitted == True:
    load_llm_response()
