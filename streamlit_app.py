import streamlit as st

# -- Page setup --
home_page = st.Page(
    page="views/home.py", title="Home Page", icon=":material/cottage:", default=True
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
# Buttons Bar
st.markdown(
    """
    <style>
        button {
            background-color: rgb(128, 61, 245) !important;
            color: white !important;
            border: white !important;
        }
    </style>""",
    unsafe_allow_html=True,
)

# Progress Bar
st.markdown(
    """
<style>
    .stProgress > div > div > div > div {
        background-color: rgb(128, 61, 245) !important;
    }

    /* Style for the empty part of the progress bar */

</style>""",
    unsafe_allow_html=True,
)
