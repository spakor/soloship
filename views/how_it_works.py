import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

st.title("How SoloShip Works")

# Step 1: Understand Your Profile
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/33d5ba14-558e-4747-a6be-072a69930477/fBRqbghm00.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_1")

with content:
    st.subheader("1. We Get to Know You")
    st.write(
        """
        - Answer 5 questions about your skills, experiences, and goals
        - Upload your resume for more personalized results (optional)
        - No clear business idea yet? Don't worry – we're here to help
        """
    )

# Step 2: AI Analysis
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/f38aae55-bc9e-4d17-bb66-2a91beb45ce5/e9x20TdOID.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_2")

with content:
    st.subheader("2. Our AI Analyzes Your Profile")
    st.write(
        """
        - Advanced AI processes your information
        - We match your attributes with potential business ideas
        - Focus on solo businesses aligned with your goals and constraints
        """
    )

# Step 3: Personalized Results
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/a6423d63-610e-4bb2-8273-540a11a09a6e/5gHIsS9UqC.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_4")

with content:
    st.subheader("3. Your Personalized Business Insights")
    st.write(
        """
        In just moments, you'll receive:
        - Key insights about your entrepreneurial potential
        - 3 tailored business directions to explore
        - Curated resources to support your entrepreneurial journey

        Start exploring your business opportunities right away
        """
    )

# Call to Action
st.write("---")
st.header("Ready to Explore Your Business Potential?")
_, col, _ = st.columns(3)
with col:
    if st.button("Find Your Business Direction", type="primary"):
        st.switch_page("views/home.py")