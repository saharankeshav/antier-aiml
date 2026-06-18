#pivot table
#17june2026

# PIVOT TABLE
import pandas as pd

# Create sample DataFrame
data = {
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'Gender': ['M', 'F', 'F', 'M', 'M', 'F'],
    'Salary': [50000, 60000, 55000, 52000, 58000, 62000],
    'Experience': [2, 5, 3, 4, 6, 7]
}

df = pd.DataFrame(data)

result1 = pd.pivot_table(
    df,
    values="Salary", # coloum to agg
    index = "Department" , #row
    aggfunc="mean"
)


result2 = pd.pivot_table(
    df,
    values="Salary", # coloum to agg
    index = "Department" , #row
    aggfunc=["mean","max"]
)


result3 = pd.pivot_table(
    df,
    values="Salary", # coloum to agg
    index = "Department" , #row
    aggfunc=["mean","max"],
    columns="Gender",
    fill_value = 0
)

result4 = pd.pivot_table(
    df,
    values="Salary", # coloum to agg
    index = "Department" , #row
    aggfunc=["mean","max"],
    columns="Gender",
    fill_value = 0,
margins=True
)
print(result3)


