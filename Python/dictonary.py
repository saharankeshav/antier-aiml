# d = {"name": "Keshav" , "age":20 , "age":10}

# print(d["age"])

# print(d.get("age"))

# print(d.items())

# print(d.keys())

# print(d.values())

# d1 = {"name", "age", "city"}
# d1 = dict.fromkeys(d1,0)
# print(d1)

d= {"name": "Keshav" , "age":20 , "city": "Delhi"}
l = {"age": 35}
d.update(l)
d.popitem()
print(d)