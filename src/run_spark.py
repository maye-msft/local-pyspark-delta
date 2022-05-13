from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import os
import pandas as pd
from pandas.testing import assert_frame_equal
import io
from .get_path import get_path 

def run():
    conf = SparkConf().setAppName("data-app").setMaster("local[*]")
    spark = SparkSession.builder.config(conf=conf)\
                    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.2.0,com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.21") \
                    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\
                    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")\
                    .getOrCreate()
    
    # current_dir_path = os.path.dirname(os.path.realpath(__file__))
    # parent_dir_path = os.path.join(current_dir_path, os.pardir)
    # storage_dir_path = os.path.join(parent_dir_path, f'test_data')
    # print(storage_dir_path)

    storage_dir_path = get_path()

    data = spark.sql("SELECT explode_outer(array(10, 20)) ")
    data.write.format("delta").mode("overwrite").save(storage_dir_path)
    data = spark.sql("SELECT explode_outer(array(30, 40)) ")
    data.write.format("delta").mode("append").save(storage_dir_path)

    data = spark.read.format("delta").load(storage_dir_path)

    data.orderBy(col("col").asc())
    print("actual")
    data.show()

    return data

run()