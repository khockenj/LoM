from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json
app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

app.config["MONGO_URI"] = "mongodb://localhost:27017/lom"  
mongo = PyMongo(app)     
mongo.db.users.create_index([('name', 'text')])   
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/profileInfo/<user>')
def profileInfo(user):
    if user == "MENTORS":
        prep = mongo.db.users.find({"type": "mentor"}, { 'ip': 0, 'password': 0, 'type': 0 })
        response = json.dumps([mentor for mentor in prep], default=json_util.default)
    else:
        response = json.dumps(mongo.db.users.find_one({ "$text": { "$search": user } },  { 'ip': 0, 'password': 0 }), default=json_util.default)
    return response
