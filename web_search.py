from duckduckgo_search import ddg

class WebSearch:
    def search_and_summarize(self, query: str) -> str:
        results = ddg(query, max_results=1)
        if not results:
            return None
        snippet = results[0].get('body', '') or results[0].get('snippet', '')
        # Basic fallback: return snippet + link
        answer = f"{snippet}\n\nSource: {results[0].get('href')}"
        return answer if snippet else None
