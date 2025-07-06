from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder     .appName("TradeSurveillance")     .getOrCreate()

schema = StructType()     .add("user_id", IntegerType())     .add("symbol", StringType())     .add("action", StringType())     .add("quantity", IntegerType())     .add("timestamp", IntegerType())

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "trade-events")     .load()

df_parsed = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

suspicious = df_parsed.filter("quantity > 500")

query = suspicious.writeStream     .format("console")     .start()

query.awaitTermination()
