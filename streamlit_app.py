import streamlit as st
import re
from sheets.google_client import emails_worksheet

# -- Page setup --
st.set_page_config(page_icon="assets/2.png")


home_page = st.Page(
    page="views/home.py", title="Home", icon=":material/cottage:", default=True
)
how_it_works_page = st.Page(
    page="views/how_it_works.py", title="How It Works", icon=":material/neurology:"
)
our_story_page = st.Page(
    page="views/our_story.py", title="Our Story", icon=":material/groups:"
)
faq_page = st.Page(page="views/faq.py", title="FAQ", icon=":material/quiz:")

# --- Navigation ---
pg = st.navigation(pages=[home_page, how_it_works_page, our_story_page, faq_page])


# --- Run Navigation
pg.run()

# --- shared on all pages --
st.logo("assets/2.png")

st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
            height: 7.5rem;
}
</style>
""",
    unsafe_allow_html=True,
)


def submit_feedback(email, feedback_type, feedback):
    try:
        emails_worksheet.append_row([email, feedback_type, feedback])
        return True
    except Exception as e:
        st.sidebar.error(f"An error occurred: {str(e)}")
        return False


def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# Set up the sidebar
with st.sidebar.expander("💌 We'd Love to Hear from You!", expanded=True):
    # Add a form for email and feedback
    st.markdown("### Your Thoughts Matter!")
    st.write("Help us improve SoloShip and shape the future of entrepreneurship.")

    with st.form(key="feedback_form", border=False):
        email = st.text_input("Email Address", placeholder="you@example.com")
        feedback_type = st.selectbox(
            "Type of Feedback",
            options=[
                "General Feedback",
                "Feature Request",
                "Bug Report",
                "Success Story",
            ],
        )
        feedback = st.text_area(
            "Your Message",
            placeholder="Share your experience, ideas, or concerns...",
        )
        agree = st.checkbox("I agree to be contacted about my feedback")
        submit_button = st.form_submit_button(
            label="Send Feedback", use_container_width=True, type="primary"
        )

        if submit_button:
            if email and is_valid_email(email) and feedback and agree:
                if submit_feedback(email, feedback_type, feedback):
                    st.success(
                        "Thank you for your valuable feedback! We appreciate your input."
                    )
                    st.balloons()
            else:
                if not email or not is_valid_email(email):
                    st.warning("Please enter a valid email address.")
                if not feedback:
                    st.warning("Please provide some feedback.")
                if not agree:
                    st.warning("Please agree to be contacted about your feedback.")
