import pandas as pd

df = pd.read_csv('customers.csv')

for it in df.values:
    print(f'Name: {it[1]} Country: {it[4]}')
