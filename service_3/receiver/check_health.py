import pika 


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
              		routing_key='hello',
              		body='Health')
connection.close()