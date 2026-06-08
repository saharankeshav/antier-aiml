import numpy as np
import matplotlib.pyplot as plt

# arr = np.array([10,20,30,40, 50])

# print(np.mean(arr))
# print(np.median(arr))

# print(np.std(arr))

# plt.hist(arr)
# plt.show()

# x = [1,2,3,4]
# y = [5,6,7,8]



# plt.plot(x,y, color="red",linestyle="--" , marker="o")

# plt.xlabel("Days")
# plt.ylabel("Sles")
# plt.title("Sales")
# plt.show()


# x = [1,2,3]
# sales=[20,30,40]
# profit= [10 ,20 , 30]
# plt.plot(x,sales,label="Sales")
# plt.plot(x,profit, label="Profit")
# plt.legend()
# plt.show()

subject = ["History", "geography" , "civics"]
marks = [50 , 30 ,30]

plt.pie(marks, labels=subject, autopct="%1.1f%%")
plt.show()

# x = [1,5,6,8,9,20]
# y = [10,2,3,4,7,40]

# plt.scatter(x,y)
# plt.show()