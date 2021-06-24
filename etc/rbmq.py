'''
cloudamqp.com
https://vulture.rmq.cloudamqp.com/#/

User: gzinbdkc
Password: z5w_te_sHpmhGTs2mc2XRz1u20UsWobG
AMQP URL: amqp://gzinbdkc:z5w_te_sHpmhGTs2mc2XRz1u20UsWobG@vulture.rmq.cloudamqp.com/gzinbdkc

pip install pika
'''
import pika, os

def get_connection():  ## 'amqp://<pwd>@vulture.rmq.cloudamqp.com/<user>
    AMQP_URL = 'amqp://gzinbdkc:z5w_te_sHpmhGTs2mc2XRz1u20UsWobG@vulture.rmq.cloudamqp.com/gzinbdkc'
    params = pika.URLParameters(AMQP_URL)
    params.socket_timeout = 5
    return pika.BlockingConnection(params) ## Connect to CloudAMQP     

## Send a message
def send(queue, msg):
    connection = get_connection()
    channel = connection.channel()            ## start a channel
    channel.queue_declare(queue=queue)
    
    channel.basic_publish(exchange='', routing_key=queue, body=msg)
    connection.close()
    print('Message sent')
# send('วิชา ไทยชม', 'Hello 1')

# A callback function on incoming messages
def callback(ch, method, properties, body):
    print(body.decode())
        
def consume(queue):
    connection = get_connection()
    channel = connection.channel()      ## start a channel
    channel.queue_declare(queue=queue)  ## Declare a queue
    
    channel.basic_consume(queue, callback, auto_ack=True)
    channel.start_consuming()       ## start consuming (blocks)
    connection.close()
# consume('วิชา ไทยชม')
