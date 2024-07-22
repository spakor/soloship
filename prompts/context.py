import json
import random

PERSONAL_RELATED = [
    """If you have a business idea in mind, please describe it in detail. \n If you're uncertain, feel free to skip this question.""",
    """Please share your professional experience, including roles, industries, and key skills. \n Even if you've submitted your resume, additional details here can help us tailor our recommendations more effectively.""",
    """Describe your interests, hobbies, or passions outside of your professional life. \n The more specific you can be, the better we can align business ideas with your personal interests.""",
    """Is there any additional information about yourself, your goals, or your circumstances that you'd like us to consider? \n This could include personal challenges, unique skills, or specific aspirations.""",
]

BUSINESS_RELATED = [
    """How many hours per week can you realistically dedicate to your new business? \n Consider your current commitments and desired work-life balance.""",
    """Every business requires time to become profitable. \n How long are you prepared to work on the business without seeing a profit? (e.g., 6 months, 1 year, 2 years)""",
    """What's the maximum amount you're willing to invest in this business before seeing a return? \n Please specify an amount you're comfortable with potentially losing.""",
    """Have you had any previous entrepreneurial experiences? \n If so, please describe the nature of the business, your role, and what you learned from the experience.""",
    """What are your primary motivations for starting this business? (e.g., financial independence, pursuing a passion, solving a problem, etc.)""",
    """Do you have a specific financial goal for this business? \n If so, what's a realistic annual income you'd like to achieve within the first few years?""",
]

LIST_OF_QUESTIONS = [*PERSONAL_RELATED, *BUSINESS_RELATED]


with open("prompts/business_examples.json", "r") as f:
    examples = json.load(f)
# randomly select 5 examples
random_sample_niche_examples = ", ".join(
    [example_dict["niches"][0] for example_dict in random.sample(examples, 5)]
)
random_sample_business_examples = ", ".join(
    [example_dict["business"] for example_dict in random.sample(examples, 5)]
)

TIME_CONSIERATION = """Ensure to include the time estimation for building audience. State the assumptions if made. 
                        Provide detailed reasoning for estimation in bulletpoints."""
COST_CONSIERATION = """Ensure to include the operation cost estimation(in USD) in the first year month by month. 
                        Provide detailed reasoning for estimation in bulletpoints."""

PROMPT_1 = (
    "Summary",
    """
        Provide a quick summary of your understanding of user's experience and desires in bulletpoints up to 5.
        Exact word count: [50 to 100]
        Always address the user as "You", and do not include the user's name.
    """,
)
PROMPT_2 = (
    "Niche Recommendations",
    f"""
        Provide top 5 niche recommendations related to the user's current skills and interests. 
        It's better for the recommendations to encompass diverse fields, not constrained to particular field. (e.g. {random_sample_niche_examples})
        Let's think step-by-step, but do not display each step in response.
        Always address the user as "You", and do not include the user's name.
    """,
)
PROMPT_3 = (
    "Business Recommendations",
    f"""
        Provide top 5 one-person business recommendations related to the user's professional experience and personal interests. 
        It's better for the recommendations to encompass diverse fields, not constrained to particular field. (e.g. {random_sample_business_examples})
        BUSINESS MODELS SHOULD ENCAPTULATE THE RECOMMENDED NICHES, NOT IDENTICAL. 
        Consider the time and cost tolerance from the user's input when recommending a business. 
        Ensure the recommended businesses are small but scalable over time. 
        {TIME_CONSIERATION}
        Let's think step-by-step.
        Always address the user as "You", and do not include the user's name.
    """,
)
PROMPT_4 = (
    "Required business skills and knowledge",
    """
        Provide a list of skills and knowledge for recommended businesses. 
        Include every aspect of business, such as marketing, accounting, legal, etc.
        The response must be in a formatted table.
        Ensure to inlcude online resources(learning platforms) to acquire each skill and knowledge
        Let's think step-by-step.
        Always address the user as "You", and do not include the user's name.
    """,
)
PROMPT_5 = (
    "Services and Tools needed",
    """
        Provide a list of existing services and tools required to operate recommended businesses to success. 
        These may include emailing, researching, marketing, etc. 
        For each service and tool, you must provide a service provider name. ie. email MailChimp
        The response must be in a formatted table.
        {COST_CONSIERATION}
        Let's think step-by-step.
        Always address the user as "You", and do not include the user's name.
    """,
)

SYSTEM_CONTEXT = """
        You are an experienced business consultant who is going to help the user to start a one-person business based on the user input. 
        You must not assume or add anything that was not mentioned. 
    """


MULTI_SYS_PROMPT = [PROMPT_1, PROMPT_2, PROMPT_3, PROMPT_4, PROMPT_5]
