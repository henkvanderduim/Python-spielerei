from pyspark.sql import SparkSession
import pandas as pd

# Create SparkSession
spark = (
    SparkSession.builder.master("local[*]")
    .appName("Great Expectations with Pandas DataFrame")
    .getOrCreate()
)

# Read data from CSV file
raw_df = spark.read.option("header", True).csv("../Kickstarter_projects_Feb19.csv")
raw_df.createOrReplaceTempView("CAMPAIGNS")
type(raw_df)
raw_df.printSchema()
raw_df.toPandas()
