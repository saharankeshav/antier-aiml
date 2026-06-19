import pandas as pd
import numpy as np 

# # Create sample dataset
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
#     'Age': [25, 30, np.nan, 35, 28, 40, 29, np.nan, 32, 38],
#     'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
#     'Salary': [50000, 60000, 55000, np.nan, 52000, 80000, 58000, 62000, np.nan, 90000],
#     'City': ['Delhi', 'Mumbai', 'Delhi', np.nan, 'Chennai', 'Bangalore', 'Delhi', 'Mumbai', 'Bangalore', 'Chennai'],
#     'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
# }

# df = pd.DataFrame(data)

# Q1 = df["Salary"].quantile(0.25)
# Q3 = df["Salary"].quantile(0.75)

# IQR = Q3 -Q1
# lower = Q1 - 1.5*IQR
# upper = Q3 + 1.5*IQR

# outliers = df[(df['Salary'] < lower) | (df['Salary'] > upper) ]

# print(outliers)
# print(lower)
# print(upper)


df = pd.DataFrame({
    "marks": [10,12,14,15,16,18,20,100,150]
})

Q1 = np.quantile(df["marks"],0.25)
Q3 = np.quantile(df["marks"],0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

# outliers = df[(df['marks'] < lower) | (df['marks'] > upper)]
# print(outliers)

clean_df = df[(df['marks'] >= lower) & (df['marks'] <= upper)]
print(clean_df)

