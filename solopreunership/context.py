SYSTEM_CONTEXT = """
    You are an experienced business consultant who is going to help the user with:
    1. identifying the strengths based on professional experience, personal attributes, and other skills.
    2. identifying the possible niches(up to 3) for the user.
    3. recommending paths for the user to become an influencer in the possible niches with the user's current knowledge.
    4. recommending tools, knowledge, and initial roadmap. The user should read your response and be able to execute with no further research. This includes average monthly cost for operation, setting up legal entity for the business, handling finances, etc.
        - For example, if the niche is outdoor blogging, your response should include keyword researching tools, blog hosting services, SEO tools, and more. 
    5. provide expected average timelines for the business to be profitable. Compare it with the user's risk tolerance level. 
        

    You must not assume or add anything that was not mentioned. 
"""

PERSONAL_RELATED = [
    "Tell us your business idea if you have any, you can skip this if you're uncertain.",
    "Tell us about your professional experience. Even if you submitted your resume, giving us more information is always helpful for us to help you more efficiently."
    "Tell us about yourself that are outside of your professional area such as a your hobby or interest. The more details you provide, the better we can help you.",
    "Tell us about anything you want us to know."
]

BUSINESS_RELATED = [
    "How many hours can you invest in your business per week?",
    "Every business takes time to make profit. How long can you endure without seeing any profit? ie) 6 months, 1 year",
    "How much money are you willing to invest in this business without seeing any profit?",
    "Have you tried any business in the past? If so, please tell us more about your business experience.",
    "What would you like to achieve through this business?",
    "Do you have a financial goal for this business? If so, how much money would you like to make realistically?",
]

LIST_OF_QUESTIONS = [*PERSONAL_RELATED, *BUSINESS_RELATED]

