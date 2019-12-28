from confluent_kafka import Consumer
from config import configs

def consume_fibonacci():
    try:
      while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print(msg.value().decode('utf-8'))
    except KeyboardInterrupt as e:
      print("Interrupted by user")
    finally:
      consumer.close()

if __name__ == '__main__':
    consumer = Consumer({
        'bootstrap.servers': configs['bootstrap.servers'],
        'group.id': configs['group.id'],
        'auto.offset.reset': configs['auto.offset.reset']
    })

    consumer.subscribe([configs['topic']])

    consume_fibonacci()
