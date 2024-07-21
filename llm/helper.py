import requests
import os
import streamlit as st
from openai import OpenAI

from prompts.context import MULTI_SYS_PROMPT, SYSTEM_CONTEXT


# Constants
BASE_URL = "https://api.upstage.ai/v1/"
CHAT_URL = BASE_URL + "solar"
OCR_URL = BASE_URL + "document-ai/ocr"
SOLAR_MODEL = "solar-1-mini-chat"

# Environment Variables
UPSTAGE_API_TOKEN = os.getenv("UPSTAGE_API_TOKEN")

# OpenAI Client Initialization
client = OpenAI(api_key=UPSTAGE_API_TOKEN, base_url=CHAT_URL)

# --- Session State for LLM scope ---


# Function to create a chat stream
def create_chat_stream(messages: list[dict], model: str = SOLAR_MODEL):
    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


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
        st.write(prompt_type)
        st.write_stream(_stream_chunks(updated_messages))
        response_text = "".join(st.session_state.response_chunks)
        st.session_state.response_dict = {prompt_type: response_text}
        st.session_state.response_text = response_text


def _stream_chunks(updated_messages: list[str]):
    for chunk in create_chat_stream(updated_messages):
        st.session_state.response_chunks.append(chunk)
        yield chunk
