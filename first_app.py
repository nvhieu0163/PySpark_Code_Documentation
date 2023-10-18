from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName("PySpark first application")\
    .getOrCreate()

sc = spark.sparkContext
print(sc)
sc.stop()

spark
spark.stop()