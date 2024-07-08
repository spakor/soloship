PERSONAL_RELATED = [
    "Tell us your business idea if you have any, you can skip this if you're uncertain.",
    "Tell us about your professional experience. Even if you submitted your resume, giving us more information is always helpful for us to help you more efficiently.",
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

TIME_CONSIERATION = """Ensure to include the time estimation for building audience. State the assumptions if made."""
COST_CONSIERATION = """Ensure to include the operation cost estimation(in USD) in the first year month by month."""

PROMPT_1 = """Provide a quick summary and breakdown of the user input in 200 words or less."""
PROMPT_2 = """Provide top 5 niche recommendations related to the user's current skills and interests.""" + TIME_CONSIERATION
PROMPT_3 = """Provide top 5 one-person business recommendations related to the user's current skills and interests.""" + TIME_CONSIERATION
PROMPT_4 = """
Provide a list of skills and knowledge for recommended businesses. 
Include every aspect of business, such as marketing, accounting, legal, etc.
""" + COST_CONSIERATION
PROMPT_5 = """
Provide a list of services and tools required to operate recommended businesses to success. 
These may include emailing, researching, marketing, etc. 
""" + COST_CONSIERATION

SYSTEM_CONTEXT = """
    You are an experienced business consultant who is going to help the user to start a one-person business based on the user input. 
    You must not assume or add anything that was not mentioned. 
""" + PROMPT_1 + PROMPT_2 + PROMPT_3 + PROMPT_4 + PROMPT_5