import streamlit as st
import os
from dotenv import load_dotenv
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from llm.llm_client import LLMClient
import json
import logging

load_dotenv()
# Logging setup
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom CSS
st.markdown("""
    <style>
    .stApp { background-color: #1e1e1e; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #2d2d2d; color: #ffffff; border: 1px solid #4a4a4a; }
    .stButton > button { background-color: #007bff; color: white; border: none; border-radius: 5px; }
    .stSpinner > div { color: #ffffff; }
    .chat-message { padding: 10px; border-radius: 10px; margin-bottom: 10px; }
    .user-message { background-color: #007bff; text-align: right; }
    .bot-message { background-color: #333333; text-align: left; }
    </style>
""", unsafe_allow_html=True)

st.title("AI Operations Assistant")
st.markdown("Select an example or enter a task. The system will plan, execute, and verify.")

# Example prompts
examples = [
    "Find the top 3 Python repos on GitHub and get their star counts.",
    "What's the weather in Mumbai right now?",
    "Search for AI repos on GitHub and check the weather in San Francisco.",
    "Get details for the 'tensorflow/tensorflow' repo on GitHub.",
    "Plan a trip: Weather in New York and popular ML repos."
]

selected_example = st.selectbox("Run an example prompt:", [""] + examples)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="chat-message {message["role"]}-message">{message["content"]}</div>', unsafe_allow_html=True)

# User input or selected example
prompt = st.chat_input("Enter your task...") or selected_example
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="chat-message user-message">{prompt}</div>', unsafe_allow_html=True)
    try:
        with st.spinner("Planning..."):
            llm = LLMClient()
            planner = PlannerAgent(llm)
            plan = planner.plan(prompt)
            plan_json = json.dumps(plan)
        with st.spinner("Executing..."):
            executor = ExecutorAgent(llm)
            execution_results = executor.execute(plan)
            exec_json = json.dumps(execution_results)
        with st.spinner("Verifying..."):
            verifier = VerifierAgent(llm)
            final_output = verifier.verify(execution_results, prompt)
        st.session_state.messages.append({"role": "assistant", "content": final_output})
        with st.chat_message("assistant"):
            st.markdown(f'<div class="chat-message bot-message">{final_output}</div>', unsafe_allow_html=True)
        # Collapsible raw JSON
        with st.expander("View Raw Agent Outputs"):
            st.json({"plan": json.loads(plan_json), "execution": json.loads(exec_json)})
    except Exception as e:
        logging.error(f"Error in main flow: {str(e)}")
        st.error(f"Error: {str(e)}. Check app.log for details.")