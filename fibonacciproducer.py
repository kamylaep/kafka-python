import argparse
import time

from confluent_kafka import Producer
from config import configs


def produce_fibonacci(n):
    first = 0
    second = 1

    try:
        if n:
            for i in range(0, n + 1):
                __produce__(first)
                first, second = __calc_fibonacci__(first, second)
        else:
            while(True):
                __produce__(first)
                first, second = __calc_fibonacci__(first, second)
                time.sleep(3)
    except KeyboardInterrupt as e:
        print("Interrupted by user")
    finally:
        producer.flush()


def __delivery_report__(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print(
            f'topic = {msg.topic()}, partition = {msg.partition()}, key = {msg.key()}, value = {msg.value()}')


def __produce__(value):
    producer.produce(topic=configs['topic'],
                     key=str(value).encode('utf-8'),
                     value=str(value).encode('utf-8'),
                     callback=__delivery_report__)
    producer.poll(0)


def __calc_fibonacci__(first, second):
    fibonacci = first + second
    first = second
    second = fibonacci
    return [first, second]


if __name__ == '__main__':
    producer = Producer({'bootstrap.servers': configs['bootstrap.servers']})

    parser = argparse.ArgumentParser(
        description="Produces the Fibonacci sequence up to the 'n' parameter. If 'N' is omitted, then, generates a new sequence every 5 seconds, indefinitely.")
    parser.add_argument("-n", help="number of sequences to generate", type=int)
    args = parser.parse_args()

    produce_fibonacci(args.n)
