import re

class AIGateway:
    def __init__(self):
        self.unsafe_patterns = [
            r'(password|credit\s*card|ssn|social\s*security)',
            r'(hack|exploit|bypass)',
            r'(porn|nude|sexual)',
        ]
        
        self.math_patterns = [
            r'(solve|calculate|compute|find|evaluate|simplify|what|expand)',
            r'(equation|formula|expression|function|derivative|integral)',
            r'(algebra|calculus|geometry|trigonometry|statistics|probability)',
            r'(theorem|proof|axiom|lemma|corollary)',
            r'(\d+[\+\-\*\/\^\=$$$$$$$$\{\}])',
        ]
    
    def input_guard(self, query):
        for pattern in self.unsafe_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                return False, "Your query contains potentially unsafe content."
        
        is_math = False
        for pattern in self.math_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                is_math = True
                break
        
        if not is_math:
            return False, "Please ask a mathematics-related question."
        
        return True, query
    
    def output_guard(self, response):
        for pattern in self.unsafe_patterns:
            if re.search(pattern, response, re.IGNORECASE):
                return False, "The response contains potentially unsafe content."
        
        return True, response