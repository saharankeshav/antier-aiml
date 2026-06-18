import pandas as pd
import numpy as np

# data = {
#     "Name": ["A", "B", "C", "D", "E"],
#     "Age": [20, np.nan, 22, np.nan, 25],
#     "Salary": [25000, 30000, np.nan, 40000, np.nan]
# }

# df = pd.DataFrame(data)

# Display original dataframe
# print("Original DataFrame:\n")


# df_constant = df.copy()

# df_constant.fillna(0,inplace=True)
# print(df_constant)

# df_mean = df.copy()

# df_mean["Age"].fillna(df_mean["Age"].mean(),inplace=True)
# # print(df_mean)

# df_median = df.copy()
# df_median["Salary"].fillna(df_median["Salary"].median(),inplace=True)

# # print(df_median)

# df_ffill = df.copy()
# df_ffill.fillna(method='ffill',inplace=True)

# # print(df_ffill)

# df_bfill = df.copy()
# df_bfill.fillna(method='bfill',inplace=True)

# # print(df_bfill)

# df_drop_cols = df.copy()

# df_drop_cols.dropna(axis=1,inplace=True)
# # print(df_drop_cols)

# df_all = df.copy()

# df_all.dropna(how='all',inplace=True)
# # print(df_all)

# df_any = df.copy()

# df_any.dropna(how='any',inplace=True)
# # print(df_any)

# df_inter = pd.DataFrame({
#     "Marks" : [10, np.nan , np.nan , 40 , 50]
# })

# df_inter["Marks"] = df_inter["Marks"].interpolate()

# print(df_inter)



df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Aman", "Neha"],
    "Marks": [90, 85, 90, 70]
})

# print(df)

# print(df.duplicated())

df = df.drop_duplicates()
# print(df)


data = {
    "Date": ["2025-01-01","2025-01-02","2025-01-03"],
    "Price": [100,105,110]
}
df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

# print(df)
# print(df.dtypes)

# -----------------------------------------------------
# resampling

dates = pd.date_range("2025-01-01", periods=12,freq="D")

df = pd.DataFrame({
    "Sales": [100,120,130,140,150,160,170,180,190,200,210,220]
},index=dates)

# print(df)

# print(df.resample("3D").mean())

df["Previous_Day_Sales"] = df["Sales"].shift(1)
# print(df)

df["Previous_Day_Sales"] = df["Sales"].shift(-1)


df["3_Day_MA"] = df["Sales"].rolling(window=2).mean()
print(df)

