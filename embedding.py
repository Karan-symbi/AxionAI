import os
import numpy as np
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

class EmbeddingService:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        self.embedder = GoogleGenerativeAIEmbeddings(
            google_api_key=api_key,
            model="models/text-embedding-004"
        )

    def embed(self, text: str):
        return self.embedder.embed_query(text)

    def cosine_similarity(self, v1, v2):
        v1 = np.array(v1)
        v2 = np.array(v2)
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
