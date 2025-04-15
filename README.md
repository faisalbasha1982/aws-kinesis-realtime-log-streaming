# AWS Kinesis Real-Time Log Streaming (Python + Boto3)

This repo demonstrates how to implement a real-time streaming pipeline using **AWS Kinesis Data Streams**, simulating a log ingestion system.

## 📦 Components

- **create_stream.py** – Creates a Kinesis Data Stream.
- **log_producer.py** – Simulates real-time application logs pushed to the stream.
- **log_consumer.py** – Reads data from the stream in real-time.

## 🔧 Prerequisites

- AWS Account & IAM user with Kinesis permissions
- AWS CLI configured (`aws configure`)
- Python 3.7+
- Boto3

## 🚀 Getting Started

```bash
pip install -r requirements.txt
python create_stream.py
python log_producer.py
# In a separate terminal
python log_consumer.py