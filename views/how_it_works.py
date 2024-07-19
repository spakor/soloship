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
image, content = st.columns([2, 4])

with image:
    lottie_url = "https://lottie.host/33d5ba14-558e-4747-a6be-072a69930477/fBRqbghm00.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_1")

with content:
    st.subheader("1. We Get to Know You")
    st.write(
        """
        - Answer 10 simple questions about your skills, experiences, and goals
        - Upload your resume for even more personalized results (optional)
        - Share your risk tolerance and time availability
        - Don't worry if you don't have a clear business idea yet – we're here to help!
        """
    )

# Step 2: AI Analysis
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/f38aae55-bc9e-4d17-bb66-2a91beb45ce5/e9x20TdOID.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_2")

with content:
    st.subheader("2. Our AI Goes to Work")
    st.write(
        """
        - Advanced algorithms analyze your profile
        - We match your unique attributes with viable business ideas
        - Our AI considers market trends, profitability, and scalability
        - We focus on solo businesses that align with your goals and constraints
        """
    )

# Step 3: Comprehensive Data
image, content = st.columns([2, 4])

with image:
    lottie_url = "https://lottie.host/9e47a8b9-642c-4145-8300-65e0099528b9/97aSVxrmUF.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_3")

with content:
    st.subheader("3. Access to Rich, Up-to-Date Data")
    st.write(
        """
        - Our database is continuously updated with:
          • Latest business ideas and emerging markets
          • Current economic trends and industry insights
          • Real-world case studies of successful solopreneurs
        - We ensure you receive relevant and timely recommendations
        - All data is tailored to match your specific profile and aspirations
        """
    )

# Step 4: Instant, Actionable Results
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/a6423d63-610e-4bb2-8273-540a11a09a6e/5gHIsS9UqC.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_animation_4")

with content:
    st.subheader("4. Your Personalized Business Roadmap")
    st.write(
        """
        In seconds, you'll receive:
        - Top 5 tailored business ideas suited to your profile
        - Detailed breakdown of required skills and resources
        - Estimated startup costs and potential earnings
        - Curated list of learning resources to fill skill gaps
        - Step-by-step guide to launch each business idea

        Start exploring your entrepreneurial opportunities right away!
        """
    )

# Call to Action
st.write("---")
st.header("Ready to Start Your Entrepreneurial Journey?")
st.button("Find Your Perfect Business Idea Now", type="primary")