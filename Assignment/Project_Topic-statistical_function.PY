import numpy as np
import matplotlib.pyplot as plt

list_marks = []
for i in range(10):
    marks = int(input("Enter marks: "))
    list_marks.append(marks)
print(list_marks)

arr = np.array(list_marks)

mean = np.mean(list_marks)
median = np.median(list_marks)
std = np.std(list_marks)

per1 = np.percentile(list_marks,25)
per2 = np.percentile(list_marks,50)
per3 = np.percentile(list_marks,75)

if(mean>75):
    print("Excellent")
elif mean>=50 and mean<=75:
    print("Average")
else:
    print("Poor")

highest = np.max(list_marks)
lowest = np.min(list_marks)
above_mean = len(arr[arr > mean])

plt.hist(list_marks)       
plt.title("Student Marks")     
plt.xlabel("Marks")   
plt.ylabel("Number of Students")    
plt.show()         