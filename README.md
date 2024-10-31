# Real-Time Movie Ratings Analytics

## Project Overview

The **Real-Time Movie Ratings Analytics** project aims to collect and analyze real-time movie ratings data using a modern data processing pipeline. The project leverages **Apache Kafka** for data ingestion, **Apache Spark** for real-time data processing and analytics, and **MySQL** as the database for storing processed data.

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

- **`data/`**:
  - This directory is intended for storing incoming and processed data files (if applicable).
  - Include any sample data files or dummy data used for testing (if applicable).

- **`setup_instructions.txt`**:
  - Instructions for setting up the project on an Ubuntu environment, including prerequisites, installation steps, and configuration details.

- **`README.md`**: 
  - This file, which provides an overview of the project, repository contents, and setup instructions.

## Getting Started

### Prerequisites

- **Apache Kafka**: Ensure Kafka is installed and running.
- **Apache Spark**: Ensure Spark is installed and configured to work with Kafka.
- **MySQL**: Ensure MySQL is installed and a database is created for storing processed data.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name

