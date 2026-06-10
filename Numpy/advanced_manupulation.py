import numpy as np 

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# result = np.vstack((a,b))
# hori = np.hstack((a,b))
# dep = np.dstack((a,b))
# print(result)
# print(hori)
# print(dep)

a = np.array([[1,2],[3,4],[5,6],[7,8]])
# result1 = np.hsplit(a, 3)
result = np.vsplit(a,2)
print(result)

