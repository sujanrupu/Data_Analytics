a = "apple", "india", 12, 12,23
print(a)
print(type(a))

b = ("apple", "india", 12, 12,23)
print(b[1:3])
print(b[::2])

for i in b:
    print(i)
for i in range(len(b)) :
    print(i, " : ", b[i])
    
print(type(b))
b = list(b)
print(type(b))
b = tuple(b)
print(b.count("apple"))
print(b.index("india"))

# Dictionary -> json

import json
data = {"name" : "Sujan", "age" : 12, "marks" : 90}
print(type(data))
data = json.dumps(data)
print(type(data))
print(data)
data = json.loads(data)
print(data["age"])
# Pretty printing
data = json.dumps(data, indent=2, separators=(",","="))
print(data)