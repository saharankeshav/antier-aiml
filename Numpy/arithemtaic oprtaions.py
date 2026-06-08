import numpy as np

# a = np.array([3,6,9,12])
# print(a/3)

# for i in a:
#     if i/3 == 3:
#         print(i)

# arr = np.array([10,20,30,40])
# print(arr-10)

# print(arr>15)


a = np.array([1,2,3])
b = np.array([10,20,30])

result1 = a[:,np.newaxis]
result2 = a[np.newaxis: ,]
print(result1)
print(result2)
