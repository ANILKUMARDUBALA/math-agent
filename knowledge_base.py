from qdrant_client import QdrantClient
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.llms import OpenAI

class KnowledgeBase:
    def __init__(self):
        self.client = QdrantClient(url="http://localhost:6333")  # Run qdrant locally or use cloud
        self.index = self.load_index()

    def load_index(self):
        # For demo: Load some math Q&A documents
        documents = SimpleDirectoryReader('math_qa_docs').load_data()
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0))
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
        return GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

    def query(self, question: str) -> str:
        response = self.index.query(question, similarity_top_k=1)
        if response.response.strip():
            return response.response
        return None
