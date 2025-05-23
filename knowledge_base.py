from qdrant_client import QdrantClient
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.llms import OpenAI

class KnowledgeBase:
    def __init__(self):
        # Replace your local URL and no API key with cloud URL + API key here:
        self.client = QdrantClient(
            url="https://19f142e4-5101-4604-b7ba-a0ab51c1af5a.eu-west-1-0.aws.cloud.qdrant.io",
            api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.rs-8jlqocaYQMn0qyEK2O5iu27nqgW2n1NXEzDikgxg"
        )
        self.index = self.load_index()

    def load_index(self):
        documents = SimpleDirectoryReader('math_qa_docs').load_data()
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0))
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
        return GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

    def query(self, question: str) -> str:
        response = self.index.query(question, similarity_top_k=1)
        if response.response.strip():
            return response.response
        return None
