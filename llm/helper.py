import os
import streamlit as st
from openai import OpenAI

from prompts.context import MULTI_SYS_PROMPT, SYSTEM_CONTEXT

BASE_URL = "https://api.upstage.ai/v1/"
CHAT_URL = BASE_URL + "solar"
OCR_URL = BASE_URL + "document-ai/ocr"
SOLAR_MODEL = "solar-1-mini-chat"

UPSTAGE_API_TOKEN = os.getenv("UPSTAGE_API_TOKEN")
client = OpenAI(api_key=UPSTAGE_API_TOKEN, base_url=CHAT_URL)


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

    if st.session_state.document_ocr:
        messages.append(
            {
                "role": "user",
                "content": f"Here is a document I uploaded, going over my professional experience: {st.session_state.document_ocr}.",
            }
        )

    for prompt in MULTI_SYS_PROMPT:
        prompt_type, i = prompt
        multi_system_prompt = {
            "role": "user",
            "content": i,
        }
        updated_messages = [system_prompt, *messages, multi_system_prompt]

        # Generate the response without streaming
        response = client.chat.completions.create(
            model=SOLAR_MODEL, messages=updated_messages, stream=False
        )

        response_text = response.choices[0].message.content

        st.session_state.response_dict[prompt_type] = response_text
        st.session_state.response_text = response_text

    st.toast("Ready!", icon=":material/rocket_launch:")
