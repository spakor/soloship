import streamlit as st

st.title("FAQs")

### ABOUT 
st.subheader("About Soloship", divider="violet")

with st.expander("What is SoloShip and how does it work?"):
    st.write('''
        SoloShip is an AI-powered platform designed to help aspiring entrepreneurs explore solo business opportunities. 
        We use advanced AI to match your skills, experiences, and goals with potential business directions. 
        Simply answer our 5-question survey, and we'll provide you with personalized business insights and directions to explore.
    ''')

with st.expander("Is SoloShip really free? Are there any hidden costs?"):
    st.write('''
        Yes, SoloShip is completely free! We're committed to helping entrepreneurs start their journey without financial barriers.
        There are no hidden costs or premium features - all our current offerings are available to everyone at no charge.
    ''')

### Business Process
st.subheader("The Process", divider="violet")

with st.expander("What kind of questions will I be asked?"):
    st.write('''
        Our questionnaire covers key areas including your professional experience, skills, personal interests, and entrepreneurial goals.
        This approach allows us to provide business directions that align with your background and aspirations.
    ''')

with st.expander("Can I change my answers after submitting them?"):
    st.write('''
        Absolutely! You can easily restart the process and provide new answers at any time to receive fresh, updated recommendations.
    ''')

with st.expander("What if I don't have a resume to upload?"):
    st.write('''
        No worries! While uploading a resume can provide additional insights, it's completely optional.
        Our questionnaire is designed to gather all the essential information we need to offer you great business directions.
    ''')

with st.expander("How long does it take to get results after answering the questions?"):
    st.write('''
        You'll receive your results in just moments! Our AI processes your answers and generates tailored insights and business directions quickly, 
        allowing you to start exploring opportunities right away.
    ''')

### Data and Privacy
st.subheader("Data And Privacy", divider="violet")

with st.expander("How does SoloShip protect my personal information?"):
    st.write('''
        Your privacy is our priority. We don't collect or store any personally identifiable information. 
        All data is used solely to generate business recommendations and is not stored after your session.
    ''')

### AI and tech
st.subheader("AI And Technology", divider="violet")

with st.expander("What AI technology does SoloShip use?"):
    st.write('''
        SoloShip uses Upstage AI, a powerful and advanced artificial intelligence platform, to analyze your information 
        and generate personalized business insights and directions.
    ''')

with st.expander("Can I use SoloShip if I'm not tech-savvy?"):
    st.write('''
        Absolutely! SoloShip is designed to be user-friendly for everyone. Our simple questionnaire and straightforward results 
        make it easy for users of all technical backgrounds to benefit from our service.
    ''')

### Business ideas and resources
st.subheader("Business Ideas And Resources", divider="violet")

with st.expander("Can I use SoloShip if I already have a business idea in mind?"):
    st.write('''
        Certainly! If you have an idea, we can provide valuable insights and resources to support it. 
        Our system can offer complementary ideas or highlight aspects of your existing concept you might not have considered.
    ''')

with st.expander("What if I don't like any of the three business directions provided?"):
    st.write('''
        No problem! You can easily retake the questionnaire, providing more detailed information to refine your results. 
        Remember, the more information you share, the better we can tailor our suggestions to your preferences.
    ''')

with st.expander("What kind of resources does SoloShip provide?"):
    st.write('''
        SoloShip provides curated resources to support your entrepreneurial journey. These may include learning materials 
        and guidance on where to find more information about your potential business directions.
    ''')

### Scope and limitations
st.subheader("Scope And Limitations", divider="violet")
with st.expander("Does SoloShip offer ongoing support after providing initial ideas?"):
    st.write('''
        Currently, we focus on providing initial guidance and business directions. Our service is designed to be a starting point 
        for your entrepreneurial journey, offering insights and potential paths to explore.
    ''')