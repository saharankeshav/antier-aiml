

# Section 1: Series from List

# Questions:
# Create a Pandas Series of at least 6 elements containing repeated values.
    # a = [1,2,3,4,4,5]
    # s = pd.Series(a)

# Display the first 3 elements of the Series.
    # print(s[0:3])

# Display the last element of the Series.
    # print(s[-1:])

# Find all unique values in the Series.
    # print(s.unique())

# Count the frequency of each value.
    # print(s.value_counts())







#  Section 2: Series from Dictionary
# Questions:


# Create a Series using a dictionary with at least 4 key-value pairs.
    # a = {'a1':1,'a2':2,'a3':3,'a4':4}
    # s = pd.Series(a)
    # print(a)

# Access the value of any one key.
    # print(s['a1'])

# Update the value of any one key.
    # s['a1'] = 10
    # print(s)

# Add a new key-value pair to the Series.
    # s['a5'] = 5
# print(s)

# Display all values greater than a specific number.
    # print(s[s>2])






#  Section 3: Series with Custom Index
# Questions:

# Create a Series with custom index labels and numeric values.
    # a = pd.Series([10,30,30,40], index=['x','y','z','w'])
# print(a)

# Access the value of any one label.
    # print(a['x'])

# Display the first 3 elements of the Series.
    # print(a[0:3])

# Update the value of any one label.
    # a['x'] = 20
    # print(a)

# Find all unique values.
    # print(a.unique())

# Count the frequency of each value.
    # print(a.value_counts())




#  Section 4: Combined Practice
# Questions:

# Create a Series of at least 7 elements with repeated values.
    # a = [1,2,2,3,3,3,4]
    # s = pd.Series(a)
    # print(s)

# Find the total number of elements.
    # print(s.size)

# Find all unique values.
    # print(s.unique())

# Count frequency of each value.
    # print(s.value_counts())




import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Anita', 'Vikram', 'Neha'],
    'Age': [23, 25, 22, 24, 26, 23, 27, 25],
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Pune', 'Bangalore', 'Delhi', 'Mumbai'],
    'Score': [85, 90, 78, 92, 88, 76, 95, 89]
}

df = pd.DataFrame(data)

# Questions:

# Display the first 3 rows using iloc.
    # print(df.iloc[0:3])

# Display the last 2 rows using iloc.
    # print(df.iloc[-2:])

# Display 'Name' and 'Score' columns for the first 5 rows using iloc.
    # print(df.iloc[:5,[0,3]])

# Display the row at index 3 using both loc and iloc.
    # print(df.loc['Score'])
    # print(df.iloc[3])

# Display the 'City' column for all rows using loc.
print(df.loc[:,'City'])

# Display details of the row with index 4 using loc.
# Display the age of the person whose index is 6 using iloc.
# Display rows from index 2 to 5 and only 'Name' and 'City' columns using iloc.
# Display Name and Score of all people from Delhi using loc.
# Display all rows where Age is greater than 24 using loc.
# Display the Score of the last 3 rows using iloc.
# Display alternate rows using iloc.
# Display details of people with indexes [1, 3, 5, 7] using loc.
# Display the first 4 names using iloc.
# Display rows from index 1 to 6 and columns from index 1 to 3 using iloc.