# Author:     Shepard Berry
# Class:      MIS 4322
# Due:        1/30/2023
# Assignment: "Reading/Writing Files Review"

import pandas as pd
from pandas import DataFrame

df = pd.read_csv("sales.csv")

info_dict = {}


# read in columns from csv file and zip them together
# zip_obj: (id, subtotal, taxamt, freight)
for package in zip(df["CustomerID"], df["SubTotal"], df["TaxAmt"], df["Freight"]):
    amount = package[1] + package[2] + package[3]
    c_id = package[0]

    # if if is not a key in info_dict, add it
    if c_id not in info_dict:
        info_dict[c_id] = amount
    else:
        info_dict[c_id] += amount

# make a new dict from the old values with new key pairs
new_dict = {'Id': info_dict.keys(), 'Total': info_dict.values()}

# make a new data frame object from the new dict and round all values to the 100th
df2 = DataFrame(data=new_dict)
df2 = df2.round(2)
df2.to_csv(path_or_buf="salesreport.csv", index=False)