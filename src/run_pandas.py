import pandas as pd
import io

csv_str="""
col
10
20
30
40
"""

expected_data = io.StringIO(csv_str)       
expected_df = pd.read_csv(expected_data, sep=",")
print(expected_df)