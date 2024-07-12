import os
from dotenv import load_dotenv
from openai import OpenAI
from pprint import pprint
from solopreunership.prompts.context import SYSTEM_CONTEXT

load_dotenv()

client = OpenAI(
    api_key=os.environ["UPSTAGE_API_KEY"], base_url="https://api.upstage.ai/v1/solar"
)

user_response_business_idea="""Create a service that offers personalized meal planning and delivery based on individual dietary needs, preferences, and health goals. \
    The service leverages technology and nutritional expertise to provide tailored meal plans and delivers fresh, pre-portioned ingredients or fully prepared meals to customers' doors."""
user_response_professional_experience="""I've worked as a professional nutritionist and also I have experience working as a chef."""
user_response_hobby_interest = """"""
USER_PROMPT = """I want to start a one-person business. I'll tell you my idea. {}
I'll tell you more about myself. {}. Also, {}.""".format(user_response_business_idea,user_response_professional_experience, user_response_hobby_interest)
query1 = USER_PROMPT + "What do you think my strengths are?"

# identify strengths
chat_result = client.chat.completions.create(
    model="solar-1-mini-chat",
    messages=[
        {"role": "system", "content": SYSTEM_CONTEXT},
        {"role": "user", "content": query1},
    ],
)

response1 = chat_result.choices[0].message.content

# ---
# pdf document(ex. CV) RAG
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate,  MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import (
    UpstageLayoutAnalysisLoader,
    UpstageGroundednessCheck,
    ChatUpstage,
    UpstageEmbeddings,
)


layzer = UpstageLayoutAnalysisLoader("skills-based-cv.pdf", output_type="html")
# For improved memory efficiency, consider using the lazy_load method to load documents page by page.
docs = layzer.load()  # or layzer.lazy_load()
llm = ChatUpstage()

rag_with_history_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            SYSTEM_CONTEXT + """
We will give you the CV of user, use this information to answer the question considering the history of the conversation. 
If you don't know the answer, just say that you don't know. 
---
CONTEXT:
{context}
         """,
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

from langchain_core.messages import AIMessage, HumanMessage

history = [HumanMessage(query1), AIMessage(response1)]

chain = rag_with_history_prompt | llm | StrOutputParser()
query2 = "Think step-by-step. Can you identify the possible niches(up to 3) for the user?"
response2 = chain.invoke({"history": history, "context": docs, "input": query2})
print("RESPONSE\n", response2)

history = [HumanMessage(query2), AIMessage(response2)]
query3 = ""
response3 = chain.invoke({"history": history, "context": docs, "input": query3})
print("RESPONSE2\n", response3)


# --- 
# FEW-SHOT TEMPLATE with GPT-4o created example + COT
from langchain_core.prompts import PromptTemplate

example = f"""I will give you an example.
Q: {USER_PROMPT} Can you tell me my strengths based on my professional experience?

A: Based on your professional experience as a nutritionist and chef, here are some key strengths that you bring to your new business venture:

### Strengths:

1. **Nutritional Expertise**:
   - **In-Depth Knowledge**: You have a comprehensive understanding of nutrition, dietary needs, and health goals, allowing you to create well-balanced and health-focused meal plans.
   - **Personalized Plans**: You can offer highly customized meal plans that cater to specific dietary restrictions, allergies, and health conditions, ensuring client satisfaction and trust.

2. **Culinary Skills**:
   - **Quality and Taste**: Your experience as a chef ensures that the meals you plan and prepare are not only nutritious but also delicious, appealing to a wide range of palates.
   - **Menu Development**: You can design diverse and exciting menus, keeping clients engaged and satisfied with a variety of meal options.

3. **Professional Experience**:
   - **Client Relations**: Your background working directly with clients as a nutritionist means you have strong interpersonal skills and can effectively communicate and understand client needs and preferences.
   - **Problem-Solving**: Handling various dietary requirements and creating suitable meal plans has honed your ability to find creative solutions to dietary challenges.

4. **Technical Knowledge**:
   - **Use of Technology**: Leveraging technology to create efficient meal plans and manage deliveries can enhance the customer experience. Your ability to incorporate tech solutions can streamline operations and improve service quality.

5. **Health and Wellness Focus**:
   - **Holistic Approach**: Combining your knowledge as a nutritionist and a chef allows you to take a holistic approach to health and wellness, promoting overall well-being through your meal plans.
   - **Educational Component**: You can educate clients on the importance of nutrition and healthy eating habits, adding value to your service and positioning yourself as a trusted authority.

6. **Attention to Detail**:
   - **Precision in Meal Preparation**: Your culinary training ensures that meals are prepared with attention to detail, both in terms of portion control and presentation.
   - **Accuracy in Nutritional Information**: You can provide precise nutritional information for each meal, which is crucial for clients who track their intake.

7. **Passion and Commitment**:
   - **Dedication**: Your passion for both nutrition and cooking is likely to drive your commitment to providing high-quality services, which can lead to higher client satisfaction and retention.

### How to Leverage These Strengths:

- **Market Differentiation**: Use your unique combination of skills to differentiate your service from competitors. Emphasize the personalized, health-focused, and gourmet aspects of your meal plans.
- **Customer Trust**: Build trust with potential clients by showcasing your credentials and experience in both nutrition and culinary arts.
- **Efficiency and Innovation**: Implement technology to streamline operations, manage client preferences, and ensure timely delivery, making your service more convenient and reliable.
- **Branding and Marketing**: Highlight your expertise in nutrition and cooking in your marketing materials, positioning yourself as a knowledgeable and trustworthy provider of personalized meal planning and delivery services.

Your diverse skill set and professional background provide a strong foundation for launching a successful personalized meal planning and delivery service.
"""
query = ''
prompt_template = PromptTemplate.from_template("Reference the following example dialogue between ai assistant and human, then answer the question. {}\n\nQ: {}\n\nA: Let's think step-by-step.").format(example, query)

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_CONTEXT),
        ("human", prompt_template),
    ]
)