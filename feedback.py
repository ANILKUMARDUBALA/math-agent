class FeedbackSystem:
    def collect_feedback(self):
        import streamlit as st
        rating = st.radio("How useful was this answer?", ["", "👍 Helpful", "👎 Not helpful"])
        return rating

    def process_feedback(self, question, answer, rating):
        # Here you can log feedback for model improvements
        # For demo, just print or save locally
        print(f"Feedback received: Question: {question}, Rating: {rating}")
