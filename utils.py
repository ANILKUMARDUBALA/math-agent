import functools

def input_guardrail(func):
    @functools.wraps(func)
    def wrapper(question):
        # Basic filtering: allow only math content (can be improved)
        allowed_chars = "0123456789abcdefghijklmnopqrstuvwxyz +-*/^=()[]{}.,"
        if any(ch.lower() not in allowed_chars for ch in question.lower()):
            return "Your question contains unsupported characters."
        return func(question)
    return wrapper

def output_guardrail(func):
    @functools.wraps(func)
    def wrapper(question):
        result = func(question)
        # Prevent any output with URLs except those from web search
        if "http" in result and "Source:" not in result:
            return "Output contains unsupported content."
        return result
    return wrapper
