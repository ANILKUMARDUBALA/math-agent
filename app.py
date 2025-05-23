import streamlit as st
from ai_gateway import AIGateway
from knowledge_base import KnowledgeBase
from web_search import WebSearch
from feedback_system import FeedbackSystem
from math_processor import MathProcessor
from router import Router

def main():
    st.title("Math Agent")
    
    ai_gateway = AIGateway()
    knowledge_base = KnowledgeBase()
    knowledge_base.load_dataset()
    web_search = WebSearch()
    feedback_system = FeedbackSystem()
    math_processor = MathProcessor()
    router = Router(knowledge_base, web_search, math_processor)
    
    query = st.text_input("Enter your math query:")
    
    if st.button("Submit"):
        is_safe, query = ai_gateway.input_guard(query)
        if not is_safe:
            st.error(query)
        else:
            response = router.route_query(query)
            is_safe, response = ai_gateway.output_guard(response)
            if not is_safe:
                st.error(response)
            else:
                st.write("Response:", response)

                with st.form("feedback_form"):
                    user_feedback = st.text_area("Please provide feedback on the response:")
                    submitted = st.form_submit_button("Submit Feedback")

                    if submitted:
                        feedback_system.collect_feedback(response, user_feedback)
                        st.write("Feedback submitted successfully.")

if __name__ == "__main__":
    main()