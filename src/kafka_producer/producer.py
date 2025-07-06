import json
import time
from kafka import KafkaProducer
from random import choice, randint

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

symbols = ['AAPL', 'GOOG', 'MSFT', 'TSLA']
actions = ['BUY', 'SELL']

while True:
    trade_event = {
        'user_id': randint(1000, 1100),
        'symbol': choice(symbols),
        'action': choice(actions),
        'quantity': randint(1, 1000),
        'timestamp': int(time.time())
    }
    producer.send('trade-events', trade_event)
    print(f"Sent: {trade_event}")
    time.sleep(1)
