#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,IntegerType, StringType
from pyspark.sql.functions import from_json,col

# issuesSchema = StructType([
#                 StructField("id",IntegerType(),False),
#                 StructField("eventType",StringType(),False),
#                 StructField("user",StringType(),False),
#                 StructField("repoName",StringType(),False),
#                 StructField("action",StringType(),False),
#                 StructField("created_at",StringType(),False),
#                 StructField("opened_at",StringType(),True),
#                 StructField("closed_at",StringType(),True)
#             ])

spark = SparkSession.builder.appName("PrintToConsole") \
    .config('spark.maser', 'spark://spark-master:7077') \
    .config('spark.executor.cores', 1) \
    .config('spark.cores.max', 1) \
    .config('spark.executor.memory', '1g') \
    .getOrCreate()

# spark = SparkSession \
#     .builder \
#     .appName("SparkStructuredStreaming") \
#     .config("spark.cassandra.connection.host","172.18.0.5")\
#     .config("spark.cassandra.connection.port","9042")\
#     .config("spark.cassandra.auth.username","cassandra")\
#     .config("spark.cassandra.auth.password","cassandra")\
#     .config("spark.driver.host", "localhost")\
#     .getOrCreate()

# spark.sparkContext.setLogLevel("ERROR")

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9094") \
    .option("startingOffsets", "earliest") \
    .option("subscribe", "test") \
    .load()


# df = spark \
#   .readStream \
#   .format("kafka") \
#   .option("kafka.bootstrap.servers", "172.18.0.4:9092") \
#   .option("subscribe", "ghData") \
#   .option("startingOffsets", "earliest") \
#   .load() 

sc = spark.sparkContext
dfJson = spark.read.json(sc.parallelize([df.selectExpr("CAST(value AS STRING)")]))


#df1 = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"),issuesSchema).alias("data")).select("data.*")
issuesDF = dfJson \
  .select("key", "repo.id") \
  .select("key", "repo.name") \
  .select("key", "type") \
  .select("key", "payload.action") \
  .select("key", "actor.login") \
  .select("key", "payload.issue.created_at") \
  .select("key", "payload.issue.closed_at")

issuesDF.printSchema()


# def writeToCassandra(writeDF, _):
#   writeDF.write \
#     .format("org.apache.spark.sql.cassandra")\
#     .mode('append')\
#     .options(table="issuesEvents", keyspace="issues")\
#     .save()

# df1.writeStream \
#     .foreachBatch(writeToCassandra) \
#     .outputMode("update") \
#     .start()\
#     .awaitTermination()
# df1.show()