import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()
class Model:
    def __init__(self):
        API_KEY = os.getenv("GOOGLE_API_KEY")
        PROMPT = os.getenv("Prompt")
        self.client = genai.Client(api_key=API_KEY)
        self.chat = self.client.chats.create(model = "gemini-2.5-flash")
        response = self.chat.send_message(PROMPT)

    def json(self,text):
        if not text.strip():
            return ""
        
        s_idx = text.find("{")
        e_idx = text.rfind("}") + 1
        
        if s_idx == -1 or e_idx == -1 :
            return ""
        
        try:
            output = json.loads(text[s_idx:e_idx])
        except Exception as e:
            raise  ValueError(f"Error Parsing {e}")

        return output if output else ""


    def structure(self,content):
        response = self.chat.send_message(content)
        result = self.json(response.text)
        return result

parser = Parser()
result = parser.parse(r"D:\Download\Hackathons\AIBoomi\AxionAI\resume\example1.pdf")
content = result["content"][0]
model = Model()
print(model.structure(content))
