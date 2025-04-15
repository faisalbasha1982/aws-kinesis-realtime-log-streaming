import boto3
import base64

kinesis = boto3.client('kinesis', region_name='us-east-1')

stream_name = 'AppLogStream'
shard_id = kinesis.describe_stream(StreamName=stream_name)['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='LATEST'
)['ShardIterator']

while True:
    records_response = kinesis.get_records(ShardIterator=shard_iterator, Limit=5)
    for record in records_response['Records']:
        print("Received:", record['Data'].decode('utf-8'))
    shard_iterator = records_response['NextShardIterator']
    time.sleep(2)