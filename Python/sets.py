'''
set = {1,2,3,4,5}
print(set)

s ={1,2,3,4,5}
s.add(6)
print(s)


s = {1,2,3,3,4,5,6}
s.remove(7)
print(s)

s.discard(7)
print(s)


s = {1,2,3,3,4,5,6}
s.pop()
print(s)

print(s.clear())


a = {1,2,3}
b ={3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

a ={1,2,3}
b = {1,2,3,4,5}

print(a.issubset(b))


a = {1,2,3,4,5}
print(3 in a)

list = {x for x in range(1,21) if x%2 ==0}
print(list)'''


