PERSONAL_RELATED = [
    "Tell us your business idea if you have any, you can skip this if you're uncertain.",
    "Tell us about your professional experience. Even if you submitted your resume, giving us more information is always helpful for us to help you more efficiently.",
    "Tell us about yourself that are outside of your professional area such as a your hobby or interest. The more details you provide, the better we can help you.",
    "Tell us about anything you want us to know.",
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

import json
import random

with open("solopreunership/business_examples.json", "r") as f:
    examples = json.load(f)
#randomly select 5 examples
random_sample_niche_examples = ", ".join([example_dict["niches"][0] for example_dict in random.sample(examples, 5)])
random_sample_business_examples = ", ".join([example_dict["business"] for example_dict in random.sample(examples, 5)])

TIME_CONSIERATION = """Ensure to include the time estimation for building audience. State the assumptions if made. Provide detailed reasoning for estimation."""
COST_CONSIERATION = """Ensure to include the operation cost estimation(in USD) in the first year month by month. Provide detailed reasoning for estimation."""

PROMPT_1 = (
    "## Summary", 
    """Provide a quick summary and breakdown of my professional experience and myself in 200 words or less."""
)
PROMPT_2 = (
    "## Niche Recommendations",
    f"""Provide top 5 niche recommendations related to the user's current skills and interests. It's better for the recommendations to encompass diverse fields, not constrained to particular field. (e.g. {random_sample_niche_examples})
DO THIS ONLY IF THE USER DID NOT INPUT ANY BUSINESS IDEA.
"""
    + TIME_CONSIERATION + " Let's think step-by-step."
)
PROMPT_3 = (
    "## Business Recommendations",
    f"""Provide top 5 one-person business recommendations related to the user's current skills and interests. It's better for the recommendations to encompass diverse fields, not constrained to particular field. (e.g. {random_sample_business_examples})
BUSINESS RECOMMENDATIONS SHOULD ENCAPTULATE THE NICHE(IF PROVIDED), BUT NOT IDENTICAL. 
"""
    + TIME_CONSIERATION + " Let's think step-by-step."
)
PROMPT_4 = (
    "## Required business skills and knowledge",
    """
Provide a list of skills and knowledge for recommended businesses. 
Include every aspect of business, such as marketing, accounting, legal, etc.
"""
    + COST_CONSIERATION + " Let's think step-by-step."
)
PROMPT_5 = (
    "## Services and Tools needed",
    """
Provide a list of services and tools required to operate recommended businesses to success. 
These may include emailing, researching, marketing, etc. 
"""
    + COST_CONSIERATION + " Let's think step-by-step."
)

SYSTEM_CONTEXT = (
    """
    You are an experienced business consultant who is going to help the user to start a one-person business based on the user input. 
    You must not assume or add anything that was not mentioned. 
"""
    # + PROMPT_1
    # + PROMPT_2
    # + PROMPT_3
    # + PROMPT_4
    # + PROMPT_5
)


MULTI_SYS_PROMPT = [PROMPT_1, PROMPT_2, PROMPT_3, PROMPT_4, PROMPT_5]
