import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

st.title("Our Story: From Frustration to Innovation")

# The Entrepreneurial Maze
image, content = st.columns([2, 4])

with image:
    lottie_url = "https://lottie.host/80e390c5-f0ee-442e-a1c5-137471aea907/lBE7D0tlCK.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_maze")

with content:
    st.subheader("The Entrepreneurial Maze")
    st.write("""
    Have you ever felt lost in the labyrinth of starting a business? You're not alone. We've been there – bright ideas dimmed by the overwhelming task of finding the right information. It's like a never-ending scavenger hunt, right?

    As aspiring entrepreneurs ourselves, we (Seongwon, Gabriel, Yongwoo, and Minji) kept hitting the same wall. We thought, "If we're struggling this much, how many brilliant ideas are dying before they even start?"
    """)

# A Wake-Up Call
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/cc805b18-718a-497b-88e3-b0d0327cf0a9/cpDkfiJTdr.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_wakeup")

with content:
    st.subheader("A Wake-Up Call")
    st.write("""
    Then came the wave of layoffs. Suddenly, job security felt like a myth. We saw talented people, full of potential, hesitating to start their own ventures. Not because they lacked ideas or skills, but because the path seemed too daunting.

    It hit us hard. People weren't just losing jobs; they were losing dreams. And that? That was something we couldn't accept.
    """)

# The 'What If' Moment
image, content = st.columns([2, 4])

with image:
    lottie_url = "https://lottie.host/bf75cde5-f4b3-4a81-ad99-9acb43e7c21c/PsrabhRvNp.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_whatif")

with content:
    st.subheader("The 'What If' Moment")
    st.write("""
    It started with a casual conversation. Two of us, venting about the scattered nature of business information, when suddenly:

    "What if we could build a one-stop shop for aspiring entrepreneurs?"

    That simple question was our eureka moment. It wasn't just about making information accessible; it was about igniting dreams and empowering talent.
    """)

# From Idea to Action
content, image = st.columns([4, 2])

with image:
    lottie_url = "https://lottie.host/1983dc18-e205-4e80-9467-74e6d2783c6f/dJTJVEaQFY.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_action")

with content:
    st.subheader("From Idea to Action")
    st.write("""
    Energized by this vision, we dove headfirst into a hackathon hosted by Upstage.ai. Our mission? To create a tool that could guide anyone from 'I have an idea' to 'I'm starting my business' – seamlessly and confidently.
    """)

# SoloShip: Your Entrepreneurial Compass
image, content = st.columns([2, 4])

with image:
    lottie_url = "https://lottie.host/5dfe71c7-853c-4769-831a-b23d5140a8ab/cci7JPulcf.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, key="lottie_soloship")

with content:
    st.subheader("SoloShip: Your Entrepreneurial Compass")
    st.write("""
    That's how SoloShip was born. We're not just a platform; we're your co-navigators in the entrepreneurial journey. We believe that with the right guidance, anyone can transform their skills and passions into a thriving business.

    Our goal? To make starting a business as exciting as imagining it. No more scattered information, no more overwhelm. Just clear, personalized pathways to turn your dreams into reality.
    """)

st.subheader("Join the Journey")
st.write("""
Are you ready to chart your own course in the business world? With SoloShip, you're not just starting a business; you're embarking on an adventure. And we're here to ensure you have everything you need for the voyage.

Let's set sail on your entrepreneurial journey together!
""")

if st.button("Start Your Business Adventure Now"):
    st.switch_page("views/home.py")
