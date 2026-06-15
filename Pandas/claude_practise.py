import pandas as pd

data = {
    "Name": ["Keshav", "Rahul", "Priya", "Anish", "Sneha", "Rohit"],
    "City": ["Jind", "Jaipur", "Jind", "Bangalore", "Jaipur", "Bangalore"],
    "Marks": [70, 80, 90, 95, 85, 75],
    "Subject": ["Math", "Science", "Math", "English", "Science", "English"]
}

df = pd.DataFrame(data)
print(df.groupby("City")["Marks"].mean())

