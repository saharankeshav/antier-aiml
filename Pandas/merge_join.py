import pandas as pd

# # DataFrame 1
# df1 = pd.DataFrame({
#     'Emp_ID': [1, 2, 3, 4],
#     'Name': ['A', 'B', 'C', 'D'],
#     'Department': ['IT', 'HR', 'IT', 'Finance']
# })

# # DataFrame 2
# df2 = pd.DataFrame({
#     'Emp_ID': [1, 2, 3, 5],
#     'Salary': [50000, 60000, 55000, 70000]
# })

# # DataFrame 3
# df3 = pd.DataFrame({
#     'Emp_ID': [1, 2, 4],
#     'Experience': [2, 5, 4]
# })


# result1 = pd.merge(df1,df2,on="Emp_ID",how="inner")
# print(result1)

# result2 = pd.merge(df1,df2,on='Emp_ID',how= "outer")
# print(result2)

# new_df1 = df1.set_index("Emp_ID")


# new_df3 = df3.set_index("Emp_ID")

# result = new_df1.join(new_df3,how ="left")



# new = pd.concat([df1,df2],axis =1)
# print(new)

# compare method -----------------------

df_a = pd.DataFrame({'A': [1,2,3]})
df_b = pd.DataFrame({'A': [9,2,4]})

result = df_a.compare(df_b)
print(result)