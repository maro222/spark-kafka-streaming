import json
from confluent_kafka import Producer
import chardet

# Function to detect the file encoding
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read(100000)  # Read the first 100,000 bytes to analyze
        result = chardet.detect(rawdata)

    return result['encoding']

# Function to produce data to Kafka
def produce_json_to_kafka(topic, data_file):
    file_encoding = detect_file_encoding(data_file)

    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'dataset_producer',
        'queue.buffering.max.messages': 1000000000
    }

    producer = Producer(producer_config)

    with open(data_file, 'r', encoding=file_encoding, errors='replace') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                record = json.loads(line)
                producer.produce(topic, value=json.dumps(record))
            except json.JSONDecodeError as e:
                print(f"JSONDecodeError in line {line_number}: {e}")
            except Exception as e:
                print(f"Error producing data to {topic} in line {line_number}: {e}")

    # Flush the producer to wait for outstanding message delivery
    producer.flush()

# Paths to your dataset JSON files
joined_file = '/home/omar/project/dataset/joined_data.json'

# Produce data to Kafka for each JSON file
produce_json_to_kafka('dataset', joined_file)