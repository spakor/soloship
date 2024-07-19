import streamlit as st
from streamlit_extras.app_logo import add_logo


# -- Page setup --
st.set_page_config(page_icon="assets/2.png")

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
