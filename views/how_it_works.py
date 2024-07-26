import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

st.title("Embark on Your SoloShip Journey")

# Step 1: Understand Your Profile
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/33d5ba14-558e-4747-a6be-072a69930477/fBRqbghm00.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_1")

with content:
    st.subheader("1. We Decode Your Entrepreneurial DNA")
    st.write(
        """
        - Share your journey through 5 insightful questions
        - Enhance results with your resume (optional but recommended)
        - No solid business idea? No problem – we'll spark your inspiration
        """
    )

# Step 2: AI Analysis
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/f38aae55-bc9e-4d17-bb66-2a91beb45ce5/e9x20TdOID.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_2")

with content:
    st.subheader("2. AI-Powered Business Matchmaking")
    st.write(
        """
        - Our AI analyzes your unique profile
        - We align your strengths with promising solo business directions
        - Discover opportunities tailored to your goals and lifestyle
        """
    )

# Step 3: Personalized Results
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/a6423d63-610e-4bb2-8273-540a11a09a6e/5gHIsS9UqC.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_4")

with content:
    st.subheader("3. Your Roadmap to Solopreneur Success")
    st.write(
        """
        In moments, you'll unlock:
        - Insights into your entrepreneurial superpowers
        - 3 tailored solo business directions to explore
        - LinkedIn content strategies to build your authority

        Launch your solo business adventure with confidence!
        """
    )

# Call to Action
st.write("---")
st.header("Ready to Chart Your Course to Success?")
_, col, _ = st.columns(3)
with col:
    if st.button("Discover Your Perfect Business Direction", type="primary"):
        st.switch_page("views/home.py")