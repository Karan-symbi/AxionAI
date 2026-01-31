from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_postgres import PGVector
from langchain_core.documents import Document
import os
import json

load_dotenv()
class Embed:
    def __init__(self):
        API = os.getenv("API_KEY")
        self.embeddings = GoogleGenerativeAIEmbeddings(google_api_key = API,
            model="models/text-embedding-004")
        
    def create_db(self,String,Name):
        self.db = PGVector(self.embeddings,connection = String,collection_name = Name,use_jsonb = True)

    def create_document(self,n,resume):
        json_res = json.loads(resume)
        return Document(
            page_content = f"{resume}",
            metadata = {"id": n, "name": json_res["name"] , "Phone": json_res["phone"]}
        )
    def add_docs(self,documents):
        self.db.add_documents(documents=documents)
    
    def match(self,skills,select):
        result = self.db.similarity_search(skills,k = select)
        return result



