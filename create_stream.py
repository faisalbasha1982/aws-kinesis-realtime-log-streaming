import boto3

kinesis = boto3.client('kinesis', region_name='us-east-1')

response = kinesis.create_stream(
    StreamName='AppLogStream',
    ShardCount=1  # You can scale this based on throughput
)

print("Stream created:", response)