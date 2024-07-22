import streamlit as st

st.title("FAQs")
### ABOUT 
st.subheader("About Soloship", divider="violet")

with st.expander("What is SoloShip and how does it work?"):
    st.write('''
        SoloShip is an AI-powered platform designed to help aspiring entrepreneurs find their ideal solo business. 
        We use advanced algorithms to match your skills, experience, and preferences with viable business ideas. \n
        Simply answer our 10-question survey, and we'll instantly provide you with tailored business suggestions, complete with resource and cost breakdowns.
    ''')

with st.expander("Is SoloShip really free? Are there any hidden costs?"):
    st.write('''
        Yes, SoloShip's core ideation service is completely free! We're committed to helping entrepreneurs start their journey without financial barriers. \n
        While our current offerings are free, we're always working to expand and improve our services. 
        In the future, we may introduce premium features or additional paid services to enhance your experience. 
        However, we'll always strive to maintain a valuable free tier. \n
        Rest assured, any future paid services will be clearly marked, and you'll always have the choice to opt in or continue using our free features.
    ''')

### Business Process
st.subheader("The Process", divider="violet")

with st.expander("What kind of questions will I be asked?"):
    st.write('''
        Our questionnaire covers three key areas: your professional experience, skill set, and risk tolerance. \n
        This comprehensive approach allows us to provide business ideas that align with your background and comfort level.
    ''')

with st.expander("Can I change my answers after submitting them?"):
    st.write('''
        Absolutely! We understand that circumstances and preferences can change. \n
        You can easily restart the process and provide new answers at any time to receive fresh, updated recommendations.
    ''')

with st.expander("What if I don't have a resume to upload?"):
    st.write('''
        No worries! While uploading a resume can provide additional insights, it's completely optional. \n
        Our questionnaire is designed to gather all the essential information we need to offer you great business ideas.
    ''')

with st.expander("How long does it take to get results after answering the questions?"):
    st.write('''
        You'll receive your results instantly! \n
        Our AI processes your answers and generates tailored business ideas in a matter of seconds, allowing you to start exploring opportunities right away.
    ''')

### Data and Privacy
st.subheader("Data And Privacy", divider="violet")

with st.expander("How does SoloShip protect my personal information?"):
    st.write('''
        Your privacy is our priority. \n 
        We don't collect or store any personally identifiable information. All data is anonymized and used solely to generate business recommendations. \n 
        Our system is designed with privacy and security at its core.
    ''')

with st.expander("How often is your database updated with new business ideas and market trends?"):
    st.write('''
        We're committed to providing the most current information. \n
        Our database is updated regularly with new business ideas, market trends, and economic data to ensure you receive relevant and timely recommendations.
    ''')

with st.expander("How accurate are the business ideas and cost estimates?"):
    st.write('''
        We strive for high accuracy by regularly updating our data from reliable sources. \n 
        However, market conditions can vary, so we recommend using our estimates as a starting point for your own research and planning.
    ''')

### AI and tech
st.subheader("AI And Technology", divider="violet")

with st.expander("How does SoloShip's AI compare to traditional business consultants?"):
    st.write('''
        While traditional consultants offer personalized advice, SoloShip provides instant, data-driven recommendations at a fraction of the cost. \n
        Our AI analyzes vast amounts of data to offer diverse, up-to-date ideas that you can explore at your own pace.
    ''')

with st.expander("Can I use SoloShip if I'm not tech-savvy?"):
    st.write('''
        Absolutely! SoloShip is designed to be user-friendly for everyone. \n
        Our simple questionnaire and straightforward results make it easy for users of all technical backgrounds to benefit from our service.
    ''')

with st.expander("How does SoloShip determine my risk tolerance?"):
    st.write('''
        We assess your risk tolerance through specific questions about your preferred time and financial investment levels. \n
        This helps us recommend business ideas that align with your comfort zone and resources.
    ''')

### Business ideas and resources
st.subheader("Business Ideas And Resources", divider="violet")

with st.expander("Can I use SoloShip if I already have a business idea in mind?"):
    st.write('''
        Certainly! If you have an idea, we can provide valuable insights and resources to support it. \n
        Our system can offer complementary ideas or highlight aspects of your existing concept you might not have considered.
    ''')

with st.expander("What if I don't like any of the three business ideas provided?"):
    st.write('''
        No problem! You can easily retake the questionnaire, providing more detailed information to refine your results. \n
        Remember, the more information you share, the better we can tailor our suggestions to your preferences.
    ''')

with st.expander("Are the learning resources provided free or paid?"):
    st.write('''
        We offer a mix of free and paid learning resources. \n
        Our goal is to provide the most valuable information for each business idea, regardless of cost. We clearly indicate which resources are free and which may require payment.
    ''')

### Scope and limitations
st.subheader("Scope And Limitations", divider="violet")
with st.expander("Does SoloShip offer ongoing support after providing initial ideas?"):
    st.write('''
        We're actively developing additional support features! \n
        Currently, we focus on providing comprehensive initial guidance. Stay tuned for updates as we expand our services to offer more ongoing support for your entrepreneurial journey.
    ''')