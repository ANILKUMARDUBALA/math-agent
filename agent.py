from knowledge_base import KnowledgeBase
from web_search import WebSearch
from utils import input_guardrail, output_guardrail

class MathAgent:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.web_search = WebSearch()

    @input_guardrail
    @output_guardrail
    def solve_question(self, question: str) -> str:
        # 1. Check KB
        kb_result = self.kb.query(question)
        if kb_result:
            return kb_result

        # 2. Else, Web Search
        web_result = self.web_search.search_and_summarize(question)
        if web_result:
            return web_result

        # 3. No reliable answer found
        return "Sorry, I couldn't find a reliable solution for your question."
