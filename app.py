import streamlit as st
from agent import MathAgent
from feedback import FeedbackSystem

st.title("Math Professor Agent")

agent = MathAgent()
feedback = FeedbackSystem()

query = st.text_input("Enter your math question:")

if query:
    # Get step-by-step solution from agent
    solution = agent.solve_question(query)
    st.markdown("### Step-by-step solution:")
    st.write(solution)

    # Human feedback
    rating = feedback.collect_feedback()
    if rating:
        feedback.process_feedback(query, solution, rating)
        st.success("Thank you for your feedback!")
