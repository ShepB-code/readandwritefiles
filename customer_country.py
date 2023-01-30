# Author:     Shepard Berry
# Class:      MIS 4322
# Due:        1/30/2023
# Assignment: "Reading/Writing Files Review"

import pandas as pd
from pandas import DataFrame

df = pd.read_csv('customers.csv')

info_dict = {}

info_dict["Name"] = []
info_dict["Country"] = []

for info in zip(df["FirstName"], df["LastName"], df["Country"]):
    info_dict["Name"].append(f'{info[0]} {info[1]}')
    info_dict["Country"].append(info[2])

df2 = DataFrame(data=info_dict)

df2.to_csv(path_or_buf="customer_country.csv", index=False)
