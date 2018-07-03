import boto3
import time
from faker import Faker
import random
import json
import logging

fake = Faker()
# defining firehose client

client = boto3.client('firehose')

logging.basicConfig(level=logging.DEBUG)
#  create a list

movies_watched = [
    'lust stories',
    'mahanati',
    'sanju', 'hello',
    'ragngasthalam',
]



# create a dict within while loop which is always true
data = {}

while True:
    data['name'] = fake.name()
    data['city'] = fake.city()
    data['country'] = fake.country()
    data['login_time'] = time.time()
    data['movie_watchedtched'] = random.choice(movies_watched)
    client.put_record(
        DeliveryStreamName='string', 'Data': json.dumps(data))
    logging.info("record streamed to kinesis : {}".format(data))






