import pandas as pd
from pandas.testing import assert_frame_equal
from pyspark import SparkConf
from pyspark.sql import SparkSession
import io
import os
from pyspark.sql.types import *
from pyspark.sql.functions import *
from src import run_spark, get_path

def test_data():       
    data = run_spark.run()
    spark = SparkSession.getActiveSession()
    storage_dir_path = get_path.get_path()
    print(storage_dir_path)
    data = spark.read.format("delta").load(storage_dir_path)
    data.orderBy(col("col").asc())

    csv_str="""col
10
20
30
40"""

    expected_data = io.StringIO(csv_str)       
    pd_df = pd.read_csv(expected_data, sep=",")
    expected_df = spark.createDataFrame(pd_df)
    expected_df.orderBy(col("col").asc())
    print("expected")
    expected_df.show()

    assert_frame_equal(data.toPandas(), expected_df.toPandas(), check_dtype=False)