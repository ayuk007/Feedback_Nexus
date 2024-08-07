import streamlit as st
from src.feedback_responder import FeedbackResponder

feedback_responder = FeedbackResponder()
st.title("Feedback Nexus")
st.subheader("A feedback responding AI")

def process_feedback(feedback, model_name, temperature):
    response = feedback_responder.generate_response(feedback = feedback,
     model = model_name, temperature = temperature)
    return response

with st.sidebar:
    st.header("Input Parameters")
    model_name = st.text_input("Model Name", "mixtral-8x7b-32768")
    temperature = st.slider("Temperature", 0.1, 1.0, value = 0.7, step = 0.1)

feedback = st.text_input("Your Feedback")
if st.button("Process"):
    response_to_feedback = process_feedback(feedback, model_name, temperature)
    st.write(response_to_feedback)