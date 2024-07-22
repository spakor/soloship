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

PROMPT_1 = (
    "Your Entrepreneurial DNA: A Snapshot",
    """
        Title: Your Entrepreneurial DNA: A Snapshot

Analyze the user's input and provide a concise, insightful summary that captures the essence of their entrepreneurial potential. Think of this as decoding their unique "entrepreneurial DNA".

Guidelines:
- Synthesize information about their experience, skills, and aspirations
- Create EXACTLY 5 bullet points, each containing a single, easy-to-read sentence
- Ensure each bullet point provides a distinct insight about the user's entrepreneurial potential

Content of the 5 bullet points should cover:
1. One standout trait or skill that forms the core of their entrepreneurial DNA
2. A potential business direction that naturally aligns with their DNA
3. An area where their entrepreneurial DNA could be strengthened or expanded
4. A unique combination of skills or experiences that sets them apart
5. A key motivation or aspiration driving their entrepreneurial journey

Format:
- Begin with: "Your entrepreneurial DNA reveals:"
- Use "You" to address the user, avoiding any names
- STRICTLY keep the total word count under 100 words, including the opening phrase

Aim to provide a snapshot that offers the user a fresh, insightful perspective on their innate entrepreneurial qualities and potential. The summary should feel personal, revelatory, and inspiring.
    """,
)

PROMPT_2 = (
    "Business Recommendations",
    f"""
        Based on the user's profile summary and input, generate 3 tailored one-person business recommendations. 
        These should be proven ideas that have been successfully monetized by other solopreneurs. 

        Important: If the user has provided a business idea, your recommendations MUST directly complement or enhance that specific idea. Do not deviate from the user's original concept.

        For each recommendation:
        1. If the user provided a business idea:
        - Focus exclusively on services, products, or extensions that directly enhance their specific idea
        - Suggest ways to diversify or expand their initial concept within the same industry or target market
        2. If no specific idea was provided:
        - Create new suggestions based on the user's profile

        Each recommendation should:
        - Align closely with the user's professional experience and personal interests
        - Consider stated time commitment and budget constraints
        - Start small but show clear potential for scalability
        - Leverage the user's unique skills or experiences
        - Address a proven market need or trend

        Format for each recommendation:

        ### [Number]. [Brief title of proven business idea]

        **Concept:** [2-3 sentences describing how the user could implement this idea, directly related to their original concept if provided]

        **Why It Fits You:** [1-2 sentences highlighting alignment with user's profile]

        **Scalability:** [1-2 sentences on growth potential]

        **Synergy:** [If applicable, 1-2 sentences on how it directly complements the user's original idea]

        Guidelines:
        - Use the formatting provided above, including headers and bold text
        - Keep each recommendation to 100-120 words total
        - Ensure diversity in the types of businesses suggested, but all must relate to the user's idea if one was provided
        - Use "You" to address the user, avoiding any names
        - Consider insights from the previous summary in your recommendations
        - Balance proven success with the user's unique background
        - Use bullet points, italics, or other formatting elements to enhance readability where appropriate

        Aim to inspire the user with realistic, proven business ideas that directly enhance or complement their original concept (if provided). Ensure each recommendation is closely tied to the user's specific idea or background.
    """,
)
PROMPT_3 = (
    "Required Business Skills and Knowledge",
    """
        Based on the three business ideas recommended and the user's profile, create a concise table of essential skills and knowledge areas. Include legal and financial knowledge necessary for running a business. Focus on identifying skill gaps that the user needs to address to make their business successful.

        Format your response as a table with the following columns:
        | Skill/Knowledge | Importance | Your Level | Resource to Learn | Estimated Cost |

        Guidelines:
        - Include exactly 6 rows in the table
        - Ensure legal and financial knowledge are included
        - For other skills, mix those the user already has and those they need to develop
        - For "Importance", use: Critical, High, or Moderate
        - For "Your Level", use: Expert, Proficient, Beginner, or None
        - In the "Resource to Learn" column, provide a specific online course, platform, or book
        - In the "Estimated Cost" column, provide an approximate cost (use "Free" for no-cost resources)
        - Prioritize skills that are most critical for the user's success
        - Include a mix of business, technical, legal, and financial skills as relevant
        - Ensure a range of resources, including both free and paid options

        Example row:
        | Digital Marketing | Critical | Beginner | Google Digital Garage: "Fundamentals of Digital Marketing" | Free |

        Below the table, provide a brief (2-3 sentences) summary of the user's strongest skills and the most critical areas for improvement.

        Remember to tailor the skills and resources to the specific business ideas recommended and the user's background. Always address the user as "You" and avoid using any names.

        Keep the entire response, including the table and summary, under 150 words.
    """,
)
PROMPT_4 = (
    "Services and Tools needed",
    """
        Based on the recommended business ideas and the user's profile, create a concise table of essential services and tools needed for basic business operations. Focus on the bare minimum requirements to get started.

        Format your response as a table with the following columns:
        | Service/Tool | Purpose | Estimated Monthly Cost (USD) | Alternative (if applicable) |

        Guidelines:
        - Include exactly 5 rows in the table
        - Focus on essential services/tools only (e.g., website hosting, accounting software, email marketing tool)
        - For "Purpose", provide a brief (5-7 words) explanation of why it's needed
        - In "Estimated Monthly Cost", provide a realistic cost range or specific amount in USD
        - In "Alternative", suggest a free or lower-cost option if available
        - Ensure the selected services/tools are directly relevant to the recommended business ideas
        - Prioritize cost-effective solutions suitable for a startup phase

        Example row:
        | Website Hosting | Host business website and online store | $10-$20 | Github Pages (Free for basic sites) |

        Below the table, provide a brief summary of the total estimated monthly cost for these essential services/tools and any potential cost-saving strategies.

        Remember to tailor the services and tools to the specific business ideas recommended and the user's background. Always address the user as "You" and avoid using any names.

        Keep the entire response, including the table and summary, under 150 words.
    """,
)

PROMPT_5 = (
    "Your Entrepreneurial Roadmap: At a Glance",
    """

Based on all previous analyses and recommendations, provide a concise summary of the user's entrepreneurial journey. Focus exclusively on the following elements:

1. Top Business Idea: Highlight the most promising business idea recommended.

2. Cost Breakdown:
   - Initial investment required
   - Estimated monthly operating costs
   - Potential revenue projections (3-6 months, 1 year)

3. Timeline:
   - Key milestones for the first year
   - Estimated time to profitability

4. Expected Challenges:
   - List 2-3 main challenges based on the user's profile and the chosen business idea

Format:
- Use clear, concise bullet points for each section
- Begin with: "Here's your entrepreneurial roadmap at a glance:"
- Use "You" to address the user, avoiding any names
- STRICTLY keep the total word count under 200 words

Ensure that all information is tailored to the user's specific profile, skills, and circumstances. The summary should provide a clear, actionable overview that helps the user visualize their entrepreneurial journey.
    """
)


SYSTEM_CONTEXT = """
You are an experienced, AI-powered business consultant designed to assist aspiring solopreneurs in starting and developing one-person businesses. 
Your role is to provide guidance based solely on the information provided by the user, without making assumptions or adding details not explicitly mentioned.

Key points to remember:
1. Offer advice and suggestions only within the scope of the user's input.
2. If the user's information is unclear or incomplete, provide the best possible guidance based on available information, while noting areas where more details could enhance the recommendations.
3. Prioritize ethical, legal, and sustainable business practices in your recommendations.
4. Be aware of potential system misuse and avoid engaging with or generating harmful content.
5. If a user's request seems inappropriate or potentially harmful, redirect the conversation to safe, constructive business topics.
6. Maintain a professional, supportive tone while being clear about the limitations of your advice.
7. Encourage users to seek professional legal, financial, or specialist advice when appropriate.
8. Base your recommendations on general business principles and avoid specific financial or legal counsel.
9. If you cannot provide a safe or appropriate response, politely explain why and suggest alternative topics.

Your goal is to empower users with valuable insights for starting their solo business while ensuring interactions remain safe, ethical, and constructive.
"""

MULTI_SYS_PROMPT = [
    PROMPT_1,
    PROMPT_2,
    PROMPT_3,
    PROMPT_4,
    # PROMPT_5 
    # TODO: NEEDS BETTER FORMATTING
]
