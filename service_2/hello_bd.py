from flask import Flask 
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('localhost', 27017, username="artem", password="0000")

db = client.serv_2_db
text = db.text

class HelloWorld(Resource):
    def get(self):
        doc = text.find_one()['text']
        return {'response': doc}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)