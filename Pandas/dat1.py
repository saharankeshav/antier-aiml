import pandas as pd
import numpy as np

#1-D ARRAY IS SERIES
# a = [1,2,3,4]
# s = pd.Series(a, index=["a1","b1","c1","d1"])
# print(s)

# b ={'a1':1, 'a2':2, 'a3':3}
# c = pd.Series(b)
# print(c)

#value count

# s = pd.Series([1,2,2,3,4,4])
# count = s.value_counts(normalize="True")
# print(count) 

# s = pd.Series([1,2,2,3,4,4])
# count = s.value_counts(normalize="True")
# print(count)

#DROPNA
# s = pd.Series([1,2,3,4,4,np.nan, np.nan])
# count = s.value_counts(dropna=False)
# print(count)

#Dataframe = 2d array , Table

# a = pd.Series([1,2,3,4,5,6,7,8])
# b = pd.Series(["a","b","c","d","e","f"])
# x = pd.DataFrame({'Numbers':a , 'Letters':b})
# print(x)

#DATAFRAE FROM DICTONARIES

# data = {
#     'Name': ['Alice', 'k', 'a' , 'b'],
#     'Age' : [10,12,21,21],
#     'City' : ['delhi','mumbai','agra','delhi']
# }
# df = pd.DataFrame(data)
# print(df)

#from list of list

# data = [
#     ['alice',25,'delhi'],
#     ['q',25,'delhi'],
#     ['l',25,'delhi'],
#     ['k',25,'delhi']
# ]
# df = pd.DataFrame(data,columns=['name','age','city'])
# print(df)


# print(df['name'])
# print(df.head(2))
# print(df.tail(2))

# print(df.describe())

#loc

# data = {'Name': ['ALice','bob','charlie','delta'],
#         'age' : [12,12,34,56],
#          'city' : ['delhi', 'mumbai', 'agra','pune']
#          }

# df = pd.DataFrame(data,index= ['A','B','C','D'])
# filtered = df.loc[(df['age'] > 10) & (df['city'] == 'delhi')]
# print(filtered)
# print(df)


# #loc functions

# print(df.loc['B'])

# print(df.loc[["A","C"], ['Name','age']])

# #iloc (uses only indexing other than loc)


#GroupBy

# x=pd.DataFrame({'Department':['Sales','Sales','IT','IT','Marketing','Marketing'],
#                 "Employee":['A','B','C','D','E','F'], 
#                 'Salary':[1000,2000,5000,5000,3000,3000]})

# Salary_sum = x.groupby('Department')['Salary'].sum()
# print(Salary_sum)

# year = pd.Series([2021,2022,2023,2024,2025,2026])
# y = pd.DataFrame({'Year':year})
# x= pd.concat([x,y],axis = 1)

# min = x.groupby(["Department"])["Salary"].agg(['max','min'])
# print(min)

# min['diff'] = min['max'] - min['min']
# print(min)


