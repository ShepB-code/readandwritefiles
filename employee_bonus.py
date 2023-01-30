# Author:     Shepard Berry
# Class:      MIS 4322
# Due:        1/30/2023
# Assignment: "Reading/Writing Files Review"

import pandas as pd

df = pd.read_csv("EmployeePay.csv")


# print out a report
for fName, lName, salary, bonus in zip(df['EmpFName'], df['EmpLName'], df['Salary'], df['Bonus']):
    print(f'{fName} {lName} has a salary of ${salary} with a bonus of {bonus}')