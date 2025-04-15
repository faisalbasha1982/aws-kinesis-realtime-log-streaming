import boto3
import json
import time
import random

kinesis = boto3.client('kinesis', region_name='us-east-1')

def generate_log():
    levels = ['INFO', 'WARNING', 'ERROR']
    return {
        'timestamp': time.time(),
        'log_level': random.choice(levels),
        'message': 'User accessed dashboard',
        'user_id': random.randint(1000, 9999)
    }

while True:
    log_data = json.dumps(generate_log())
    kinesis.put_record(
        StreamName='AppLogStream',
        Data=log_data,
        PartitionKey='user_id'
    )
    print("Pushed:", log_data)
    time.sleep(1)