import pandas as pd
from pathlib import Path

# master final row: 2563,4963010,46,14.91,1599203,24.34
# slave final row: 635,3720668,295,51.75,4343,23.37


MASTER_COUNT = 2563
SLAVE_COUNT = 635
MASTER_TIME_STAMP = 4963010
SLAVE_TIME_STAMP = 3720668

input_file = Path(__file__).with_name("combine_slave_data.csv")

df = pd.read_csv(input_file)

# add constants to align the two datasets

df["count"] = df["count"] + SLAVE_COUNT
df["time_stamp"] = df["time_stamp"] + SLAVE_TIME_STAMP

df.to_csv(input_file, index=False)
