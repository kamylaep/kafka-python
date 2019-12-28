# Kafka Python

Small app used to demonstrate how to use [Confluent Kafka Client ](https://github.com/confluentinc/confluent-kafka-python) to consume and produce Kafka messages.

It will generate and consume Fibonacci sequence numbers.

## Environment

The project is configured to use Python 3.8.
To use it:

- Install [pipenv](https://pipenv.kennethreitz.org/en/latest/)
- Enter the virtual env: `pipenv shell`
- Install the dependencies: `pipenv install`
  
## Running

- Consumer: `python consumer.py`. Ctrl+C to stop it.
- Producer: `python producer.py --n XXX` where XXX is the number of Fibonacci sequence numbers that should be generated. If omitted, it will generate a new number
  every 3 seconds