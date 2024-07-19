# Function to convert a response dictionary to a formatted string
from prompts.context import MULTI_SYS_PROMPT, SYSTEM_CONTEXT


def convert_response_to_string(response: dict):
    return "\n".join(f"{k}: {v}" for k, v in response.items())


def handle_questionnaire(questionnaire: dict):
    converted_response = convert_response_to_string(questionnaire)
    system_prompt = {
        "role": "system",
        "content": SYSTEM_CONTEXT,
    }
    user_prompt = {
        "role": "user",
        "content": f"Here is an overview of my professional experience: {converted_response}",
    }
    messages = [user_prompt]

    # TODO: ADD CSV Upload

    for prompt in MULTI_SYS_PROMPT:
        prompt_type, i = prompt
        multi_system_prompt = {
            "role": "user",
            "content": i,
        }
        updated_messages = [system_prompt, *messages, multi_system_prompt]
