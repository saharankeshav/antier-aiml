import pandas as pd

# df1 = pd.DataFrame({
#     "Name": ["Keshav", "Rahul", "Priya", "Anish"],
#     "Marks": [70, 80, 90, 95]
# })

# df2 = pd.DataFrame({
#     "Name": ["Sneha", "Rohit"],
#     "Marks": [85, 75]
# })

# df3 = pd.DataFrame({
#     "Name": ["Keshav", "Rahul", "Priya"],
#     "City": ["Jind", "Jaipur", "Jind"]
# })

# # merge df1 and df3 on Name with how="left" — what happens to Anish?
# result = pd.merge(df1,df3,how = "left")
# print(result)

# 


# Using ONE dataset, do all of these:
data = {
    "Name": ["Keshav", "Rahul", "Priya", "Anish", "Sneha", "Rohit"],
    "City": ["Jind", "Jaipur", "Jind", "Bangalore", "Jaipur", None],
    "Marks": [70, 80, 90, 95, None, 75],
    "Subject": ["Math", "Science", "Math", "English", "Science", "English"]
}

df = pd.DataFrame(data)

# Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())


# Fill missing City with "Unknown"
df["City"] = df["City"].fillna("Unknown")

# Add Grade column — A/B/C/F
def get_marks(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"
    
df["Grades"] = df["Marks"].apply(get_marks)


# Print average marks per City
avg = df.groupby("City")["Marks"].mean()
print(avg)

# Print students who scored above 80
above_80 = df[df["Marks"]> 80]
print(above_80)