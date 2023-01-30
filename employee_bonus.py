# Author:     Shepard Berry
# Class:      MIS 4322
# Due:        1/30/2023
# Assignment: "Reading/Writing Files Review"

import pandas as pd

df = pd.read_csv("EmployeePay.csv")


# make lists with each element
fNames = [name for name in df["EmpFName"]]
lNames = [name for name in df["EmpLName"]]
salary = [sal for sal in df["Salary"]]
bonus = [bonus for bonus in df["Bonus"]]

# print out a report
for i in range(len(fNames)):
    print(f'{fNames[i]} {lNames[i]} has a salary of ${salary[i]} with a bonus of {bonus[i]}')