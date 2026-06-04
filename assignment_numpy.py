import numpy as np  

#Create array [2, 4, 6, 8], add 5 to each element, then multiply result by 2
arr = np.array([2,4,6,8])
arr = arr + 5
arr = arr * 2
print(arr)

#Create array [10, 20, 30, 40], subtract 10, check which elements are greater than 15
arr = np.array([10,20,30,40])
arr = arr -10
arr = arr>15
print(arr) 

#Given a = [1,2,3] and b = [4,5,6], find a+b and a*b
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a*b) 

#Create array [5, 15, 25, 35], find elements greater than 10 AND less than 30
arr = np.array([5,15,25,35])
arr = (arr>10)&(arr<30)
print(arr)


#Create array [3, 6, 9, 12], divide by 3, check which results are equal to 3
arr = np.array([3,6,9,12])
arr = arr/3
arr = arr ==3
print(arr) 

#Create an array from 0 to 9
arr = np.arange(10)
print(arr)

#Generate numbers from 1 to 10
arr = np.arange(1,11)
print(arr)

#Create an array from 0 to 20 with step 2
arr = np.arange(0,20,2)
print(arr)

#Generate numbers from 5 to 15
arr = np.arange(5,16)
print(arr)

#Create an array from 50 to 10 (reverse order)
arr = np.arange(50,9,-1)
print(arr)

#Generate odd numbers from 1 to 15
arr = np.arange(1,16,2)
print(arr)

#Generate even numbers from 2 to 20
arr = np.arange(2,21,2)
print(arr) 


#Create 5 evenly spaced values between 0 and 10
arr = np.linspace(0,10,5)
print(arr)

#Generate 4 values between 1 and 5
arr = np.linspace(1,5,4)
print(arr)

#Generate 3 values between 10 and 20
arr = np.linspace(10,20,3 )
print(arr)

#Create 10 evenly spaced numbers between 0 and 10
arr= np.linspace(0,10,10)
print(arr) 

#Create a 2×2 matrix of zeros
arr = np.zeros((2,2))
print(arr)

#Create a 1D array of 7 zeros with integer type
arr = np.zeros(7,dtype=int)
print(arr)