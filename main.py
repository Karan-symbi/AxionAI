from Models import Model
from Parser import Parser
from DB import DB
from Embedder import Embed
from Scheduler import Schedule
import json

# parser = Parser()
# result = parser.parse(r"D:\Download\Hackathons\AIBoomi\AxionAI\resume\example1.pdf")
# content = result["content"][0]
# print("Parsed")
# model = Model()
# structured = model.structure(content)
# embed = Embed()
# db = DB()
# db.connect()
# print("Connection Successful")
# embed.create_db(db.string, db.collection)
# docs = embed.create_document(1, json.dumps(structured))
# embed.add_docs([docs])
# db.close()
# print("Connection Closed")
scheduler = Schedule()
scheduler.defaults("2026-02-05","10:00",30)
scheduler.schedule_slots("./test.csv")
scheduler.send_emails()
