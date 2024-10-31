# Real-Time Movie Ratings Analytics

## Project Overview

The **Real-Time Movie Ratings Analytics** project aims to collect and analyze real-time movie ratings data using a modern data processing pipeline. This project leverages **Apache Kafka** for data ingestion, **Apache Spark** for real-time data processing and analytics, and **MySQL** as the database for storing processed data.

### Project Components

- **Kafka**: Used to publish and collect data from various sources in real-time.
- **Spark**: Consumes data from Kafka topics and performs analytics and processing.
- **MySQL**: Stores the processed data for further analysis and retrieval.

## Features

- Real-time data ingestion of movie ratings and related information, including:
  - Title
  - Genre
  - Release Year
  - Number of Ratings
- Analysis of average movie ratings over the years.
- Insights into movie genre popularity based on user ratings.
- Examination of ratings based on user demographics (age, gender, location).

## Repository Contents

The repository contains the following files and directories:

- **`kafka/`**:
  - `producer.py`: A Python script to publish movie rating data to Kafka topics.
  - `consumer.py`: A Python script that consumes data from Kafka topics for processing.
  - `kafka_config.json`: Configuration file for setting up Kafka topics and producer/consumer settings.

- **`spark/`**:
  - `spark_processing.py`: A Python script that utilizes Spark to process data consumed from Kafka, performing transformations and analytics.
  - `spark_config.json`: Configuration file for Spark settings, including connection details to Kafka and MySQL.

- **`joined_data/`**:
  - Has the following Features: {"Rating","Year_x","UserID","Gender","Age","Occupation","Zip-code","id","name" ,"date","genre"} which is a joined file from 3 files 
  - This directory is intended for storing incoming and processed data files (if applicable).
  - Note: The dataset is too large to upload on GitHub. You can download it from [this Google Drive link]. The dataset is in LTS format.

- **`Spark_Overview/`**:
  - This summary provided by me about the tool from The Definative Guide of Spark, from first 3 chapters
 
- **`Kafka_Overview/`**:
  - This summary provided by me about the tool from The Definative Guide of Kafka, from first 3 chapters 

- **`README.md`**: 
  - This file, which provides an overview of the project, repository contents, and setup instructions.
 
- **`Important Commands`**:
  - This is commands about manipulating Kafka topics , which will be used alot in this project 

## Getting Started

### Prerequisites

- **Apache Kafka**: Ensure Kafka is installed and running.
- **Apache Spark**: Ensure Spark is installed and configured to work with Kafka.
- **MySQL**: Ensure MySQL is installed and a database is created for storing processed data.

### Running the Project

To run the project, follow these steps:

1. **Open two terminals**:
   - In **Terminal 1**, start Zookeeper and Kafka:
     ```bash
     sudo systemctl start zookeeper
     sudo systemctl start kafka
     ```

2. In **Terminal 2**, navigate to the Kafka installation directory to control topics:
   ```bash
   cd /usr/local/kafka

