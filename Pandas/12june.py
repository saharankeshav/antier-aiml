
import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Raj', 'Neha', 'Karan'],
    'Age': [23, 25, 22, 24, 26],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [25000, 30000, 28000, 35000, 40000]
}
df = pd.DataFrame(data)


# df['comparison'] = df['Salary'].apply(lambda x: 'High' if x > 30000 else 'Less')

# df.drop('comparison',axis=1, inplace = True) 

# df.rename(columns={'Name':'New_Name'},inplace=True)
# df.columns=["Emp_name","emp_age","emp_dept","emp_salary"]

# df["Salary"].replace(25000,27000,inplace=True)


# Using loc (30000 -> 50000)
# df.loc[df['Salary'] == 30000, 'Salary'] = 50000


#Multiple agg 
# print(df.groupby("Department").agg({'Salary':['sum','mean'] , 'Age':['max','min']}))

# result = df.groupby("Department").agg(Average_salary=("Salary","mean"),
#                                       Total_salary = ("Salary","sum"),
#                                       Maximum_age = ("Age","max"),
#                                       Minimum_age = ('Age','min'))

# # print(result)


# df["Average_sal"] = df.groupby("Department")["Salary"].transform("mean")
# print(df)


# Sort by Department (A-Z), then by Salary (High to Low)
# sorted_df = df.sort_values(by=['Department', 'Salary'], ascending=[False])
# print(sorted_df)

#top 3 highest value
# print(df.sort_values(by="Salary",ascending=False).head(3))

#nlargest
# print(df.nlargest(3,"Salary"))