class MathProcessor:
    def __init__(self):
        pass
    
    def generate_solution(self, query):
        # Simple math problem solver
        try:
            solution = eval(query)
            return f"The solution is: {solution}"
        except Exception as e:
            return f"Failed to solve: {str(e)}"