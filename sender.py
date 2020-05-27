import pika


class RabbitMQSender:
    def __init__(self, queue='test', exchange='', routing_key='test'):
        self.queue = queue
        self.exchange = exchange
        self.routing_key = routing_key

        self.connection_parameters = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue)

    def publish_message(self, payload):
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key=self.routing_key,
                                   body=str(payload))
        print("PUBLISHED MESSAGE SUCCESSFULLY")
        self.connection.close()


rabbit_mq_sender = RabbitMQSender('test', '', 'test')
rabbit_mq_sender.publish_message({'key': 'value'})
