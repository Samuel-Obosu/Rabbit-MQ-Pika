import pika
import ast


class RabbitMqReceiver:
    def __init__(self, callback, host='localhost', queue='test'):
        self.host = host
        self.queue = queue
        self.callback = callback

        self.connection_parameters = pika.ConnectionParameters(self.host)
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue)
        self.channel.basic_consume(queue='test', on_message_callback=self.callback, auto_ack=True)
        print("**** WAITING FOR MESSAGES *****")
        self.channel.start_consuming()


def callback_received(ch, method, properties, body):
    json_body = ast.literal_eval(body.decode('utf-8'))
    print("RECEIVED BODY ::: {}".format(body))
    print("RECEIVED BODY JSON ::: {}".format(json_body))


rabbit_mq_receiver = RabbitMqReceiver(callback_received, host='localhost', queue='test')
