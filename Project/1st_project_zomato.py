import pandas as pd

df = pd.read_csv('Zomato_data.csv')
# print(df.shape)
# print(df.head())

# Question 1 — "What type of restaurant do the majority of customers order from?"
# print(df["listed_in(type)"].value_counts())

# Question 2 — "How many votes has each type of restaurant received?"
# print(df.groupby("listed_in(type)")["votes"].sum())

# Question 3 — "What are the ratings that the majority of restaurants have received?"
# print(df['rate'].head())
# print(df['rate'].unique())
print(df['rate'].value_counts().head(10))