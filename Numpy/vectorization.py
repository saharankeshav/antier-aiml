import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# b= np.array([6, 7, 8, 9, 10])

# # Vectorized addition
# c = a + b
# print(c)

# a= 1,2,3,4
# b= 5,6,7,8
# c = []
# #add values each using loop 
# for i in range (len(a)):
#     c.append(a[i]+b[i])

# print(c)

# def square(a):
#     return a * a

# arr = np.array([1,2,3])
# print(square(arr))


# arr = np.array([1,2,3])
# result = np.where(arr%2==0 , "Even" , arr)
# print(result)

# a = np.array([1,2,3,4])

# print(a[a>3])

a = np.array([1,2,3,4])
b= lambda x:x*x
print(b(a))