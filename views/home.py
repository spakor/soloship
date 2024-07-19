import streamlit as st
from streamlit_extras.colored_header import colored_header

from llm.helper import handle_questionnaire
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
# @st.experimental_fragment
def send_to_llm():
    with st.spinner("Loading..."):
        responses_dict = {
            LIST_OF_QUESTIONS[i]: st.session_state.responses[i]
            for i in range(TOTAL_QUESTIONS)
        }
        handle_questionnaire(responses_dict)


def show_start_over_button():
    if st.button("Start Over", type="primary"):
        st.session_state.clear()
        st.rerun()


# --- Questionnaire ---
if st.session_state.submitted == False:
    show_questionnaire()
else:
    if len(st.session_state.response_chunks) > 0:
        response_text = "".join(st.session_state.response_chunks)
        st.write(response_text)
        show_start_over_button()
    else:
        send_to_llm()
        show_start_over_button()
