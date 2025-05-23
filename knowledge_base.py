import json
import os
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

class KnowledgeBase:
    def __init__(self, collection_name="math_questions"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = QdrantClient(":memory:")
        self.collection_name = collection_name
        
        try:
            self.client.get_collection(collection_name=collection_name)
        except:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=self.model.get_sentence_embedding_dimension(), distance=models.Distance.COSINE)
            )
    
    def load_dataset(self, file_path="data/math_dataset.json"):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        if not os.path.exists(file_path):
            sample_data = [
                {"id": 1, "question": "What is 2 + 2?", "solution": "The answer is 4."},
                {"id": 2, "question": "Solve for x: 2x + 5 = 11", "solution": "Subtract 5 from both sides: 2x = 11 - 5, 2x = 6. Divide by 2: x = 6 / 2, x = 3."},
                {"id": 3, "question": "What is the value of x: x - 3 = 7", "solution": "Add 3 to both sides: x = 7 + 3, x = 10."}
            ]
            with open(file_path, 'w') as f:
                json.dump(sample_data, f, indent=4)
        
        with open(file_path, 'r') as f:
            dataset = json.load(f)
        
        points = []
        for item in dataset:
            vector = self.model.encode(item["question"]).tolist()
            points.append(models.PointStruct(
                id=item["id"],
                vector=vector,
                payload={"question": item["question"], "solution": item["solution"]}
            ))
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
    
    def search(self, query):
        query_vector = self.model.encode(query).tolist()
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=1
        )
        
        if results and results[0].score > 0.75:
            return results[0].payload
        
        return None