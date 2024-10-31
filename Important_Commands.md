![image](https://github.com/user-attachments/assets/4ccafcf8-5f8a-4840-bae9-c393104f07b8)# Apache Kafka CLI Cheat Sheet

## Essential Commands

### 1. Create Topic
To create a topic, use the following command:
```bash
bin/kafka-topics.sh \
	--bootstrap-server localhost:9092 \
	--create \
	--topic "name_of_topic" \
	--partitions 2 \
	--replication-factor 2 \
	--if-not-exists \
	--config retention.ms=86400000 \
	--config retention.bytes=1073741824


### 2. Drop Topic
bin/kafka-topics.sh \
	--bootstrap-server localhost:9092 \
	--delete \
	--topic "name_of_topic"


### 3. List Topics
bin/kafka-topics.sh \
	--bootstrap-server localhost:9092 \
	--list


### 4. Describe Topic
bin/kafka-topics.sh \
	--bootstrap-server localhost:9092 \
	--describe \
	--topic "name_of_topic"


### 5. Produce Message to Topic
bin/kafka-console-producer.sh \
	--bootstrap-server localhost:9092 \
	--topic "name_of_topic"


### 6. Consume Message from Topic
bin/kafka-console-consumer.sh \
	--bootstrap-server localhost:9092 \
	--topic "name_of_topic" \
	--from-beginning
