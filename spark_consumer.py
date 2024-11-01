from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, array_contains, explode, expr, window, count, desc, avg
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, StructField, IntegerType, ArrayType, LongType, TimestampType
import os
import logging


#facilities methods and configuration:
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 pyspark-shell'
logging.getLogger("org.apache.spark.streaming.kafka010.KafkaDataConsumer").setLevel(logging.ERROR)
mysql_jar_path = "/home/omar/dataset/ml-1m/mysql-connector-j_8.2.0-1ubuntu22.04_all/usr/share/java/mysql-connector-java-8.2.0.jar"

mysql_url = "jdbc:mysql://localhost:3306/spark_schema"
mysql_properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

def write_to_mysql(df,table_name,epoch_id):
    dfwriter = df.write.mode("append") 
    # dfwriter.jdbc(url=mysql_url, table=user, properties=mysql_properties) # if this is not working use below
    df.write.jdbc(url=mysql_url, table=table_name, properties=mysql_properties, mode="append")
    pass



# Create a Spark session
spark = SparkSession.builder.appName("KafkaConsumer").config("spark.jars", mysql_jar_path).config("spark.executor.memory", "4g").config("spark.driver.memory", "4g").getOrCreate()

spark.sparkContext.setLogLevel('WARN')

# Define the Kafka parameters
kafka_bootstrap_servers = 'localhost:9092'
kafka_topics = 'dataset'  # Add your topics here, separated by commas

# Define the schema for the Kafka message value
message_schema = StructType().add("value", StringType())

# Define the schema for the user JSON data
dataset_schema = StructType([
    StructField("UserID", StringType(), True),
    StructField("Gender", StringType(), True),
    StructField("Age", StringType(), True),
    StructField("Occupation", StringType(), True),
    StructField("Zip-code", StringType(), True),
    StructField("Rating", StringType(), True),
    StructField("Year_x", StringType(), True),
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("date", StringType(), True),
    StructField("genre", StringType(), True),
   
])


# Read data from Kafka topics
kafka_stream_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers)
    .option("startingOffsets", "earliest") 
    .option("subscribe", kafka_topics)
    .load()
)

# Deserialize JSON data for users and movies
dataset_deserialized_df = kafka_stream_df.filter("topic = 'dataset'").select(
    from_json(col("value").cast("string"), dataset_schema).alias("dataset")
).select("dataset.*")



####################################
# average_ratings_over_years dataframe (avor)
average_ratings_over_years = dataset_deserialized_df\
    .groupBy("Year_x")\
    .agg({"Rating": "avg"})\
    .withColumnRenamed("avg(Rating)", "AverageRating")


movie_rating = dataset_deserialized_df.groupBy("name", "genre").agg(count("Rating").alias("RatingCount"))
demographics_ratings = dataset_deserialized_df.groupBy('Age', 'Gender', 'Zip-code').agg(avg('Rating').alias('AvgRating')).orderBy(desc("AvgRating"))





genre_popularity =(
    dataset_deserialized_df
    .groupBy("genre")
    .agg(avg("Rating").alias("average_rating"))
    .orderBy(desc("average_rating"))
)




#average_ratings_over_years.show(5)
# Output the streaming data to the console
genre_popularity_query = genre_popularity\
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()


average_query = average_ratings_over_years\
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()


dataset_query=dataset_deserialized_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

movie_rating_query = movie_rating  \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()                  

demographics_ratings_query = demographics_ratings  \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()  



#sink to database
query1 = dataset_deserialized_df.writeStream.outputMode("append").foreachBatch(lambda df, epoch_id: write_to_mysql(df, "dataset", epoch_id)).start()
query2 = genre_popularity.writeStream.outputMode("complete").foreachBatch(lambda df, epoch_id: write_to_mysql(df, "avg_rating_genre", epoch_id)).start()
query3 = average_ratings_over_years.writeStream.outputMode("complete").foreachBatch(lambda df, epoch_id: write_to_mysql(df, "average_rating_year", epoch_id)).start()
query4 = movie_rating.writeStream.outputMode("complete").foreachBatch(lambda df, epoch_id: write_to_mysql(df, "average_rating_film", epoch_id)).start()
query5 = demographics_ratings.writeStream.outputMode("complete").foreachBatch(lambda df, epoch_id: write_to_mysql(df, "demographics", epoch_id)).start()


dataset_query.awaitTermination()
average_query.awaitTermination()
movie_rating_query.awaitTermination()
genre_popularity_query.awaitTermination()
demographics_ratings_query.awaitTermination()
