# Author:     Shepard Berry
# Class:      MIS 4322
# Due:        1/30/2023
# Assignment: "Reading/Writing Files Review"

import pandas as pd
from pandas import DataFrame

pf = pd.read_csv("sales.csv")

info_dict = {}

info_dict["Id"] = []
info_dict["Total"] = []

for package in zip(pf["CustomerID"], pf["SubTotal"], pf["TaxAmt"], pf["Freight"]):
    info_dict["Id"].append(package[0])
    info_dict["Total"].append(round(package[1] + package[2] + package[3], 2))

pf2 = DataFrame(data=info_dict)

pf2.to_csv(path_or_buf="salesreport.csv", index=False)