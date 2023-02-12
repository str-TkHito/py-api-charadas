from flask import Flask
from pymongo import MongoClient
from dotenv import dotenv_values
import json
import random
import pprint

env = dotenv_values(".env")

app = Flask(__name__)

client = MongoClient(env["MONGO_URL"])

@app.route("/")
def hello_world():
    db = client.Principal
    collection = db.Jokes

    count = collection.count_documents({})
    data = collection.find_one({"id": random.randint(1, count)})
    print(data)
    return json.dumps({"id": data["id"], "question": data["question"], "answer": data["answer"]})
    

app.run(host=env["HOST"], port=env["PORT"])

