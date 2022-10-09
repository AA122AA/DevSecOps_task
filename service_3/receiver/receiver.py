import pika, sys, os
from pymongo import MongoClient

client = MongoClient('mongodb', 27017, username='artem', password='0000')

db = client.serv_2_db
text = db.text

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        if body == b"Health":
            print("Healthy")
        else:
            doc = {
			    'response': f'{body}'
		    }
            text.insert_one(doc)
            print(" [x] Inserted %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)