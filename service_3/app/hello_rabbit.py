from flask import Flask 
from flask_restful import Resource, Api
import pika

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='',
                      		routing_key='hello',
                      		body='Hello World MQ!')
        connection.close()
        return {'response': 'Message has been produced'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)