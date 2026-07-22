import streamlit as st


def initialize_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_chat():

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def add_user_message(message):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant_message(message):

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": message
        }
    )