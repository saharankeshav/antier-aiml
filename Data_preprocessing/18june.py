import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('train.csv')

# print(df.shape)
# print(df.head())

# print(df.isnull().sum())

df["Product_Category_2"] = df["Product_Category_2"].fillna(0)
df["Product_Category_3"] = df["Product_Category_3"].fillna(0)

# print(df.isnull().sum())

# print(df.duplicated().sum())

# print(df["Gender"].unique())
# print(df["City_Category"].unique())
# print(df["Age"].unique())

le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])
# print(df["Gender"].unique())
print(df[["Gender"]].head())