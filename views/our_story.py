import streamlit as st
from streamlit_lottie import st_lottie
import requests


def load_lottie_url(url: str):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


st.title("Our Story: How SoloShip Set Sail")

# The Entrepreneurial Maze
content, image = st.columns([4, 2])
with image:
    st_lottie(
        load_lottie_url(
            "https://lottie.host/80e390c5-f0ee-442e-a1c5-137471aea907/lBE7D0tlCK.json"
        ),
        key="lottie_maze",
    )
with content:
    st.subheader("Where do we even begin?")
    st.write(
        """
    Ever had a great idea but felt totally lost when thinking about starting a business? 

    Starting a business is a whole different ball game. Where do you even begin? 
    Not knowing where to start is often the biggest hurdle to getting your business off the ground.

    Better stick to our day jobs, right? 
    """
    )

# A Wake-Up Call
content, image = st.columns([4, 2])
with image:
    st_lottie(
        load_lottie_url(
            "https://lottie.host/cc805b18-718a-497b-88e3-b0d0327cf0a9/cpDkfiJTdr.json"
        ),
        key="lottie_wakeup",
    )
with content:
    st.subheader("Not so safe after all")
    st.write(
        """
    Then boom! Layoffs everywhere. 
    Suddenly, that "safe" job doesn't feel so secure anymore.
    Every quarter you lose another work buddy, and you start to wonder, 'Could I be next?' 

    Maybe it got you thinking about starting your own gig. 
    Oh, some kid's making bank dropshipping. Oh, college students are raking it in selling website templates. 

    And you're left wondering, 'Is it just me who can't figure out how to start my own business?'
    """
    )

content, image = st.columns([4, 2])
with image:
    st_lottie(
        load_lottie_url(
            "https://lottie.host/2de96823-d004-4fb8-82eb-dd5896c24b39/dN9fSPXRrI.json"
        ),
        key="lottie_whatif",
    )
with content:
    st.subheader("It's better to travel with a map")
    st.write(
        """
    Listen up, because here's the real deal:

    To run your own business, you need to find a direction you feel like yourself – one where you're ready to push through the tough times. 
    
    You've got talent. You've got valuable skills to offer the world. You've got what it takes to build a business. 
    But what you haven't found yet is the right direction for YOU. 
    
    """
    )

# SoloShip: Your Entrepreneurial Compass
content, image = st.columns([4, 2])
with image:
    st_lottie(
        load_lottie_url(
            "https://lottie.host/1983dc18-e205-4e80-9467-74e6d2783c6f/dJTJVEaQFY.json"
        ),
        key="lottie_letsgo",
    )
with content:
    st.subheader("Say Hello to SoloShip!")
    st.write(
        """
    SoloShip was created to help you get started on the right foot. 
    We believe that the first step in business is knowing what you can offer the world. 
    
    Here's the kicker: you might not even recognize your own value yet. 

    That's why we created SoloShip – to help you identify what you already have. Your skills, experience, and interests are the compass that'll guide you to where people need your services.
    """
    )

content, image = st.columns([4, 2])

with image:
    st_lottie(
        load_lottie_url(
            "https://lottie.host/5dfe71c7-853c-4769-831a-b23d5140a8ab/cci7JPulcf.json"
        ),
        key="lottie_soloship",
    )
    
with content:
    st.subheader("Start Today!")
    st.write(
        """
    To kickstart your entrepreneurial journey, we're giving you something you can dive into right away. 

    Based on the direction that's right for you, we've crafted content strategies for LinkedIn so you can start taking action today. 
    Share your knowledge and insights – let the world see how amazing you are!

    So, what do you say? Ready to set sail on your business adventure?
"""
    )
_, col, _ = st.columns(3)
with col:
    if st.button("Launch Your Business Journey Now!", type="primary"):
        st.switch_page("views/home.py")
