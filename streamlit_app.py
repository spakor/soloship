import json
import os
import streamlit as st

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables from .envrc file or .env file
load_dotenv()


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


# Set up the sidebar
with st.sidebar.expander("Contact Us", icon=":material/mail:"):
    # Add a form for email and feedback
    st.title("Email and Feedback")
    st.write("We value your feedback! Please leave your email and comments below.")

    with st.form(key="feedback_form", border=False):
        email = st.text_input("Enter your email address", placeholder="you@example.com")
        feedback = st.text_area(
            "Enter your feedback", placeholder="Your feedback here..."
        )
        submit_button = st.form_submit_button(
            label="Submit", use_container_width=True, type="primary"
        )

        if submit_button:
            if email and feedback:
                try:
                    # Use the credentials to create a client to interact with the Google Drive API
                    scope = ["https://www.googleapis.com/auth/spreadsheets"]
                    # Load credentials from the environment variable
                    creds_json = os.getenv("GOOGLE_API_KEY")
                    sheets_id = os.getenv("GOOGLE_SHEET_ID")
                    creds_dict = json.loads(creds_json)
                    creds = ServiceAccountCredentials.from_json_keyfile_dict(
                        creds_dict, scope
                    )
                    client = gspread.authorize(creds)

                    # Find a workbook by name and open the first sheet
                    # Make sure you use the right name here.
                    sheet = client.open_by_key(sheets_id).sheet1

                    # Append the data
                    sheet.append_row([email, feedback])

                    st.sidebar.success("Thank you for your feedback!")
                except Exception as e:
                    st.sidebar.error(f"Failed to submit feedback. Error: {str(e)}")
            else:
                st.sidebar.error("Please enter a valid email address and feedback.")
