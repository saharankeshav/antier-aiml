import pandas as pd
import numpy as np

# data = {
#     'Name': ['Amit','Priya','Raj'],
#     'Salary': [30000,50000,60000]
# }

# df = pd.DataFrame(data)

# df.to_csv("employee_data.csv",index=False)


# df = pd.read_csv("employee_data.csv")
# print(df)


data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, np.nan, 22, np.nan, 25],
    "Salary": [25000, 30000, np.nan, 40000, np.nan]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())

