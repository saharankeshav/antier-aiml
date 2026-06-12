result = df.groupby("Department").agg(Average_salary=("Salary","mean"),
#                                       Total_salary = ("Salary","sum"),
#                                       Maximum_age = ("Age","max"),
#                                       Minimum_age = ('Age','min'))

# # print(result)