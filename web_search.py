# web_search.py
import os
import requests
from bs4 import BeautifulSoup

class WebSearch:
    def __init__(self):
        self.tavily_api_key = "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"
        self.search_engine_url = "https://api.duckduckgo.com"
    
    def search(self, query):
        # Implement web search functionality
        url = "https://api.tavily.com/search"
        params = {
            "api_key": self.tavily_api_key,
            "query": query,
            "search_depth": "advanced",
            "include_answer": True
        }
        
        response = requests.post(url, json=params)
        result = response.json()
        
        if "answer" in result and result["answer"]:
            return result["answer"]
        
        return None