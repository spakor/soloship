import streamlit as st
from streamlit_extras.colored_header import colored_header

from prompts.context import LIST_OF_QUESTIONS

# -- Hero Secion --
st.title(body="Soloship :rocket:", anchor=False)
st.subheader(
    "Your :violet[brilliant] idea deserves a business.",
    anchor=False,
)

st.divider()


# -- Questionnaire Dialog--
@st.experimental_dialog("Questionnaire")
def show_dialog():
    answers = []
    with st.form("Answer the questions to get started", border=False):
        for index, question in enumerate(LIST_OF_QUESTIONS):
            if answer := st.text_input(question, key=f"question_{index}"):
                answers.append(answer)
        submit = st.form_submit_button("Submit", type="primary")
    if answers and submit:
        st.rerun()
    if not answers and submit:
        st.warning("Please answer at least one question.", icon=":material/warning:")


@st.experimental_fragment
def show_questionnaire():
    total_questions = len(LIST_OF_QUESTIONS)
    last_question_index = total_questions - 1

    # --- Session related to the questionnaire ---
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "responses" not in st.session_state:
        st.session_state.responses = [""] * total_questions

    st.subheader("Answer the questions to get started", anchor=False)

    # --- Setting the progress bar ---
    progress = (st.session_state.step + 1) / total_questions
    st.progress(progress)

    # --- Setting the Questions and setting the Answer ---
    # Writes the question according to the step (index) the user is currently on
    st.write(LIST_OF_QUESTIONS[st.session_state.step])
    # Sets the answer accordining to the step the user is currently on
    st.session_state.responses[st.session_state.step] = st.text_area(
        f"Question {st.session_state.step + 1} / {total_questions}",
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
            if next.button(":submit", type="primary", use_container_width=True):
                st.rerun()

        if all(response == "" for response in st.session_state.responses):
            if next.button("submit", type="primary", use_container_width=True):
                st.error(
                    "Please answer at least one question.", icon=":material/warning:"
                )
            # st.rerun()


show_questionnaire()
