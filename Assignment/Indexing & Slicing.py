import numpy as np

#Extract elements from index 2 to 5.
arr = np.array([10,20,30,40,50,60,70,80])
print(arr[2:6])

#Extract the last 4 elements using slicing.
arr = np.array([10,20,30,40,50,60,70,80])
print(arr[-4:])


#Extract every second element.
arr = np.array([10,20,30,40,50,60,70,80])
print(arr[0:-1:2])


#Reverse the array using slicing.
arr = np.array([10,20,30,40,50,60,70,80])
print(arr[::-1])

#Extract elements at odd index positions.
arr = np.array([5,10,15,20,25,30,35,40])
print(arr[1::2])

#Print the second row.
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr[1])

#Using the same array, print the third column.
print(arr[:,2])

#Using the same array, extract [[10,20],[40,50]].
print(arr[0:2,0:2])

#Extract [[6,7],[10,11]].
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr[1:3,1:3])

#Using the same array, extract the last two rows.
print(arr[0:2])
#Extract all elements greater than 20 using Boolean Indexing.
arr = np.array([12,25,18,7,30,45,9,16])
print(arr[arr>20])

#Using the same array, extract all even numbers.
print(arr[arr%2==0])

#Using the same array, extract elements between 10 and 30.
print(arr[(arr>10) & (arr<30)])

#Using Fancy Indexing, create [100,300,500].
arr = np.array([100,200,300,400,500,600])
print(arr[[0,2,4]])

#Using the same array, create [600,400,200].
print(arr[[5,3,1]])


#Extract [[8,9,10],[13,14,15],[18,19,20]].
arr = np.arange(1,26).reshape(5,5)
print(arr[1:4 , 2:5])

#Using the same array, extract the diagonal elements [1,7,13,19,25].
print(arr.diagonal())

#Using the same array, extract all elements greater than 15.
print(arr[arr>15])

#Extract [[60,70],[100,110]].
arr = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(arr[1:3,1:3])


#Extract [[1,3],[9,11]] using indexing and slicing only.
arr = np.arange(1,17).reshape(4,4)
print(arr[0:4:2,0:4:2])
