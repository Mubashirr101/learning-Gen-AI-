import streamlit as st
from openai import OpenAI


def generate_ai_response(prompt: str, api_key: str) -> str:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")
st.title("AI Chatbot")

with st.sidebar:
    st.header("Chat Settings")
    api_key = st.text_input("Groq API Key", type="password", help="Enter your own Groq API key")    
    st.button("Clear Chat", use_container_width=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_ai_response(prompt, api_key)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

