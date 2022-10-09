from flask import Flask 
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb', 27017, username="artem", password="0000")

db = client.serv_2_db
text = db.text

class HelloWorld(Resource):
    def get(self):
        doc = text.find_one()['text']
        return {'response': doc}

class Health(Resource):
    def get(self):
        return {'response': 'healthy'}

api.add_resource(HelloWorld, '/')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(debug=True)