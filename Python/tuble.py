#tuple

'''
arr = (1,2,3,4,5,6,7,7,8,9)
a,b,*c = arr

print(c)

t = (1,2,2,3,4,4,4,4)

print(t.count(2))
print(len(t))
print(sum(t))
print(max(t))
print(min(t)) '''

t = (0,1,2,3,4,5,6,7,8,9,10)
count = 0
for i in t:
    count = 0 
    if(i%2 == 0):
        count+= 1
print(count)
        
