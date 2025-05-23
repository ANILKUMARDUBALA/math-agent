class Router:
    def __init__(self, knowledge_base, web_search, math_processor):
        self.knowledge_base = knowledge_base
        self.web_search = web_search
        self.math_processor = math_processor
    
    def route_query(self, query):
        result = self.knowledge_base.search(query)
        if result:
            return result["solution"]
        
        web_result = self.web_search.search(query)
        if web_result:
            return web_result
        
        return self.math_processor.generate_solution(query)