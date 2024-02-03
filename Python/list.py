list = ["Sujan", 'c', True, 24]
print(list)
print(type(list))
print(list[3])
print(list[1:3])
print(list[::-1])

for i in list:
    print(i)
    
for i in range(len(list)) :
    print(i, " : ", list[i])

i = 0
while(i < len(list)):
    print(i, " : ", list[i])
    i += 1
    
list.append("Hello")
print(list)

list1 = list.copy()
print(list1)

c = ["India", "Human"]
list.append(c)
print(list)

list = [2, 4, 1, 3, 7, 5]
list.sort()
print(list)