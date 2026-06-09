import pandas as pd

input_file = "combine_master_data.csv"


# final row of part 1: 2563,4963010,46,14.91,1599203,24.34

df = pd.read_csv(input_file)

# add constants to align the two datasets

df["count"] = df["count"] + 2563 
df["time_stamp"] = df["time_stamp"] + 4963010

df.to_csv("combine_master_data.csv", index=False)