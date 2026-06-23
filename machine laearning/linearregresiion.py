import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


experience = [1, 2, 3, 4, 5, 6]   
salary = [10, 20, 30, 40, 50, 60]



df = pd.DataFrame({
    'Experience': experience,
    'Salary': salary
})

# print(df.to_string(index=False))



# plt.figure(figsize=(8, 5))
# plt.scatter(experience, salary)

# plt.title('Experience vs Salary')
# plt.xlabel('Experience (Years)')
# plt.ylabel('Salary (k)')
# plt.xticks(experience)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

model = LinearRegression()

X = df.iloc[:, 0:1]
y = df.iloc[:, -1]

X_train , y_train , X_test , y_test = train_test_split(X, y , test_size = 0.2 )
# print(X_train.shape)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(model.score(X_test,y_test))

