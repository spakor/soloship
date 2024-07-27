# import contextlib
# import random
# import re
# import time
# import requests
# import streamlit as st
# from streamlit_lottie import st_lottie
# from collections import OrderedDict


# from llm.helper import OCR_URL, UPSTAGE_API_TOKEN, handle_questionnaire
# from prompts.context import LIST_OF_QUESTIONS

# # --- Module vars ---
# TOTAL_QUESTIONS = len(LIST_OF_QUESTIONS)

# # -- Hero Secion --
# col1, _ = st.columns(2, gap="small", vertical_alignment="center")

# with col1:
#     st.image("./assets/soloship.png")


# st.subheader(
#     "Ready, Set, :violet[Solopreneur]: Your Adventure Begins Now!",
#     anchor=False,
# )


# if "submitted" not in st.session_state:
#     st.session_state.submitted = False
# if "step" not in st.session_state:
#     st.session_state.step = 0
# if "responses" not in st.session_state:
#     st.session_state.responses = [""] * TOTAL_QUESTIONS
# if "response_chunks" not in st.session_state:
#     st.session_state.response_chunks = []
# if "response_dict" not in st.session_state:
#     st.session_state.response_dict = OrderedDict()
# if "regenerated " not in st.session_state:
#     st.session_state.regenerated = False
# if "startover_button " not in st.session_state:
#     st.session_state.startover_button = False
# if "document_ocr" not in st.session_state:
#     st.session_state.document_ocr = None
# if "document_ocr_processing" not in st.session_state:
#     st.session_state.document_ocr_processing = False
# if "lottie_shown" not in st.session_state:
#     st.session_state.lottie_shown = False


# # TODO: Turn this into a helper function
# def load_lottie_url(url: str):
#     response = requests.get(url)
#     if response.status_code != 200:
#         return None
#     return response.json()


# # -- Questionnaire Dialog--
# @st.experimental_fragment
# def show_questionnaire():
#     last_question_index = TOTAL_QUESTIONS - 1

#     placeholder = st.empty()
#     with placeholder.container(border=True):
#         if not st.session_state.submitted == True:
#             # --- Session related to the questionnaire ---
#             if "step" not in st.session_state:
#                 st.session_state.step = 0
#             if "responses" not in st.session_state:
#                 st.session_state.responses = [""] * TOTAL_QUESTIONS

#             # --- Setting the progress bar ---
#             progress = (st.session_state.step + 1) / TOTAL_QUESTIONS
#             st.progress(progress)

#             # --- Setting the Questions and setting the Answer ---
#             # Writes the question according to the step (index) the user is currently on
#             st.write(LIST_OF_QUESTIONS[st.session_state.step])
#             # Sets the answer accordining to the step the user is currently on
#             st.session_state.responses[st.session_state.step] = st.text_area(
#                 f"Question {st.session_state.step + 1} / {TOTAL_QUESTIONS}",
#                 key=f"question_{st.session_state.step}",
#                 # If a value has already been given for the question prior to submission it will be retrieved.
#                 value=st.session_state.responses[st.session_state.step],
#             )

#             # --- Creating the back & next buttons ---

#             back, _, next = st.columns(3, gap="large")

#             prev_disabled = st.session_state.step == 0
#             if st.session_state.step != 0:
#                 if back.button(
#                     "back",
#                     type="primary",
#                     disabled=prev_disabled,
#                     use_container_width=True,
#                     key="back-button",
#                 ):
#                     st.session_state.step -= 1
#                     st.rerun()

#             if st.session_state.step < last_question_index:
#                 if next.button(
#                     "next", type="primary", use_container_width=True, key="next-button"
#                 ):
#                     st.session_state.step += 1
#                     st.rerun()

#             # --- Setting the submit button ---
#             if st.session_state.step == last_question_index:
#                 if any(response != "" for response in st.session_state.responses):
#                     if next.button(
#                         "submit",
#                         type="primary",
#                         use_container_width=True,
#                     ):
#                         st.session_state.submitted = True
#                         st.rerun()

#                 if all(response == "" for response in st.session_state.responses):
#                     if next.button("submit", type="primary", use_container_width=True):
#                         st.error(
#                             "Please answer at least one question.",
#                             icon=":material/warning:",
#                         )

#         show_document_upload()


# # --- Handle LLM Responses --- #
# def show_existing_response():
#     placeholder = st.empty()
#     with placeholder.container(height=700, border=False):
#         if len(st.session_state.response_dict) > 0 and not st.session_state.regenerated:
#             with st.container():
#                 for prompt, text in st.session_state.response_dict.items():
#                     st.subheader(f":violet[{prompt}]")
#                     text = re.sub(r"(?<! )#", "\n #", text, count=1)
#                     st.markdown(text)
#                     # st.markdown()
#                     st.divider()

#     col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")
#     with col4:
#         show_start_over_button()
#     # with col4:
#     #     show_regenerate_button()


# @contextlib.contextmanager
# def lottie_animation():
#     placeholder = st.empty()
#     lottie_url = (
#         "https://lottie.host/5dfe71c7-853c-4769-831a-b23d5140a8ab/cci7JPulcf.json"
#     )
#     lottie_json = load_lottie_url(lottie_url)

#     with placeholder.container():
#         st_lottie(lottie_json, key="lottie")

#     try:
#         yield
#     finally:
#         placeholder.empty()


# @st.experimental_fragment
# def send_to_llm():
#     responses_dict = {
#         LIST_OF_QUESTIONS[i]: st.session_state.responses[i]
#         for i in range(TOTAL_QUESTIONS)
#     }

#     with lottie_animation():
#         handle_questionnaire(responses_dict)

#     for prompt_type, response_text in st.session_state.response_dict.items():
#         st.subheader(f":violet[{prompt_type}]")
#         st.write(response_text)

#     st.session_state.submitted = False

#     col1, _, _, col4 = st.columns(4, gap="large", vertical_alignment="bottom")
#     with col4:
#         show_start_over_button()

#     # with col4:
#     #     show_regenerate_button()


# @st.experimental_fragment
# def show_regenerate_button():
#     if not st.session_state.submitted or st.session_state.regenerated:
#         if st.button("Regenerate", type="primary"):
#             st.session_state.response_chunks = []
#             st.session_state.regenerated = True
#             st.session_state.submitted = True
#             st.rerun()


# @st.experimental_fragment
# def show_start_over_button():
#     if len(st.session_state.response_dict.values()) > 0:
#         if st.button("Start Over", type="primary"):
#             st.session_state.clear()
#             st.session_state.startover_button = False
#             st.rerun()


# # --- DOCUMENT LOADER
# # Function to extract text from an uploaded document using OCR
# def extract_document_ocr(uploaded_file):
#     headers = {"Authorization": f"Bearer {UPSTAGE_API_TOKEN}"}
#     files = {"document": uploaded_file}
#     print("sending a request to the OCR ....")
#     response = requests.post(OCR_URL, headers=headers, files=files)
#     response_json = response.json()
#     return response_json.get("text")


# def show_document_upload():
#     with st.expander("Document Upload (Optional)"):
#         uploaded_file = st.file_uploader(
#             "You can upload a document such as a CV or a business proposal (optional)",
#             help="This can help the AI have more information on your experience.",
#             type=["JPEG", "PNG", "BMP", "PDF", "TIFF", "HEIC"],
#             accept_multiple_files=False,
#         )
#         if (
#             uploaded_file is not None
#             and st.session_state.document_ocr is None
#             and not st.session_state.document_ocr_processing
#         ):
#             st.session_state.document_ocr_processing = True
#             with st.spinner("Uploading your document..."):
#                 st.session_state.document_ocr = extract_document_ocr(uploaded_file)
#             st.session_state.document_ocr_processing = False


# # Function to display a random quote
# def display_random_quote():
#     # List of inspiring quotes
#     quotes = [
#         "The way to get started is to quit talking and begin doing. – Walt Disney",
#         "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. – Steve Jobs",
#         "People who are crazy enough to think they can change the world, are the ones who do. – Rob Siltanen",
#         "Entrepreneurs are great at dealing with uncertainty and also very good at minimizing risk. That's the classic entrepreneur. – Mohnish Pabrai",
#         "The only way to do great work is to love what you do. – Steve Jobs",
#         "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
#         "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
#         "If you really look closely, most overnight successes took a long time. – Steve Jobs",
#         "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
#         "The key to success is to focus on goals, not obstacles. – Albert Einstein",
#     ]

#     random_quote = random.choice(quotes)

#     parts = random_quote.split(" – ")
#     quote = parts[0].strip()
#     quotee = parts[1].strip()

#     st.markdown("<br>", unsafe_allow_html=True)
#     st.markdown(
#         f"<h4 style='font-style: italic; 'text-align: center'>{quote}</h4><p style='text-align: center; margin: 0;'>- {quotee}</p>",
#         unsafe_allow_html=True,
#     )


# def footer_lottie():
#     lottie_url = (
#         "https://lottie.host/ef6cd628-8137-40a6-be2c-279de3d91267/1EZz63i0sB.json"
#     )
#     lottie_json = load_lottie_url(lottie_url)

#     _, image = st.columns([2, 3])
#     # Render the Lottie animation in the container
#     with image:
#         st_lottie(lottie_json, key="side_bar", width=150, height=150)


# # --- Questionnaire ---
# if not st.session_state.submitted and len(st.session_state.response_dict) == 0:
#     show_questionnaire()

# # --- Handle Responses ---
# if st.session_state.submitted and not st.session_state.startover_button:
#     send_to_llm()

#     ### -- Footer ---
#     # URL for the Lottie animation
#     display_random_quote()
#     footer_lottie()

# else:

#     st.session_state.submitted = False
#     st.session_state.response_dict = {}

import contextlib
import random
import re
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from collections import OrderedDict

from llm.helper import OCR_URL, UPSTAGE_API_TOKEN, handle_questionnaire
from prompts.context import LIST_OF_QUESTIONS

# --- Module vars ---
TOTAL_QUESTIONS = len(LIST_OF_QUESTIONS)

# -- Hero Section --
col1, _ = st.columns([1, 3])

with col1:
    st.image("./assets/soloship.png")

st.subheader(
    "Ready, Set, :violet[Solopreneur]: Your Adventure Begins Now!",
    anchor=False,
)

# Initialize session state variables
session_vars = {
    "submitted": False,
    "step": 0,
    "responses": [""] * TOTAL_QUESTIONS,
    "response_chunks": [],
    "response_dict": OrderedDict(),
    "regenerated": False,
    "startover_button": False,
    "document_ocr": None,
    "document_ocr_processing": False,
    "lottie_shown": False,
}

for var, default in session_vars.items():
    if var not in st.session_state:
        st.session_state[var] = default


def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


@st.experimental_fragment
def show_questionnaire():
    last_question_index = TOTAL_QUESTIONS - 1
    placeholder = st.empty()
    with placeholder.container():
        if not st.session_state.submitted:
            progress = (st.session_state.step + 1) / TOTAL_QUESTIONS
            st.progress(progress)

            st.write(LIST_OF_QUESTIONS[st.session_state.step])
            st.session_state.responses[st.session_state.step] = st.text_area(
                f"Question {st.session_state.step + 1} / {TOTAL_QUESTIONS}",
                key=f"question_{st.session_state.step}",
                value=st.session_state.responses[st.session_state.step],
            )

            back, _, next = st.columns([1, 2, 1])

            if st.session_state.step > 0:
                if back.button(
                    "Back",
                    type="primary",
                    use_container_width=True,
                    key="back-button",
                ):
                    st.session_state.step -= 1
                    st.rerun()

            if st.session_state.step < last_question_index:
                if next.button(
                    "Next", type="primary", use_container_width=True, key="next-button"
                ):
                    st.session_state.step += 1
                    st.rerun()

            if st.session_state.step == last_question_index:
                if any(response != "" for response in st.session_state.responses):
                    if next.button(
                        "Submit",
                        type="primary",
                        use_container_width=True,
                    ):
                        st.session_state.submitted = True
                        st.rerun()
                else:
                    if next.button("Submit", type="primary", use_container_width=True):
                        st.error(
                            "Please answer at least one question.",
                            icon=":material/warning:",
                        )
        show_document_upload()


def show_existing_response():
    placeholder = st.empty()
    with placeholder.container():
        if st.session_state.response_dict and not st.session_state.regenerated:
            for prompt, text in st.session_state.response_dict.items():
                st.subheader(f":violet[{prompt}]")
                text = re.sub(r"(?<! )#", "\n #", text, count=1)
                st.markdown(text)
                st.divider()

    col1, _, _, col4 = st.columns([1, 1, 1, 1])
    with col4:
        show_start_over_button()


@contextlib.contextmanager
def lottie_animation():
    placeholder = st.empty()
    lottie_url = (
        "https://lottie.host/5dfe71c7-853c-4769-831a-b23d5140a8ab/cci7JPulcf.json"
    )
    lottie_json = load_lottie_url(lottie_url)

    with placeholder.container():
        st_lottie(lottie_json, key="lottie")

    try:
        yield
    finally:
        placeholder.empty()


@st.experimental_fragment
def send_to_llm():
    responses_dict = {
        LIST_OF_QUESTIONS[i]: st.session_state.responses[i]
        for i in range(TOTAL_QUESTIONS)
    }

    with lottie_animation():
        handle_questionnaire(responses_dict)

    for prompt_type, response_text in st.session_state.response_dict.items():
        st.subheader(f":violet[{prompt_type}]")
        st.write(response_text)

    st.session_state.submitted = False

    col1, _, _, col4 = st.columns([1, 1, 1, 1])
    with col4:
        show_start_over_button()


@st.experimental_fragment
def show_regenerate_button():
    if not st.session_state.submitted or st.session_state.regenerated:
        if st.button("Regenerate", type="primary"):
            st.session_state.response_chunks = []
            st.session_state.regenerated = True
            st.session_state.submitted = True
            st.rerun()


@st.experimental_fragment
def show_start_over_button():
    if st.session_state.response_dict:
        if st.button("Start Over", type="primary"):
            st.session_state.clear()
            st.session_state.startover_button = False
            st.rerun()


def extract_document_ocr(uploaded_file):
    headers = {"Authorization": f"Bearer {UPSTAGE_API_TOKEN}"}
    files = {"document": uploaded_file}
    response = requests.post(OCR_URL, headers=headers, files=files)
    response_json = response.json()
    return response_json.get("text")


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


def display_random_quote():
    quotes = [
        "The way to get started is to quit talking and begin doing. – Walt Disney",
        "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. – Steve Jobs",
        "People who are crazy enough to think they can change the world, are the ones who do. – Rob Siltanen",
        "Entrepreneurs are great at dealing with uncertainty and also very good at minimizing risk. That's the classic entrepreneur. – Mohnish Pabrai",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
        "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
        "If you really look closely, most overnight successes took a long time. – Steve Jobs",
        "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
        "The key to success is to focus on goals, not obstacles. – Albert Einstein",
    ]

    random_quote = random.choice(quotes)
    quote, quotee = random_quote.split(" – ")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<h4 style='font-style: italic; text-align: center'>{quote.strip()}</h4>"
        f"<p style='text-align: center; margin: 0;'>- {quotee.strip()}</p>",
        unsafe_allow_html=True,
    )


def footer_lottie():
    lottie_url = (
        "https://lottie.host/ef6cd628-8137-40a6-be2c-279de3d91267/1EZz63i0sB.json"
    )
    lottie_json = load_lottie_url(lottie_url)

    _, image = st.columns([2, 3])
    with image:
        st_lottie(lottie_json, key="home_lottie", width=150, height=150)


if not st.session_state.submitted and not st.session_state.response_dict:
    show_questionnaire()
elif st.session_state.submitted and not st.session_state.startover_button:
    send_to_llm()
    display_random_quote()
    footer_lottie()
else:
    st.session_state.submitted = False
    st.session_state.response_dict = {}
