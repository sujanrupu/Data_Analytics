# for loop

for i in range(1, 6) :
    print(i)

for i in range(1, 6, 2) :
    print(i)

n = int(input("Enter no.: "))
for i in range(1, 11) :
    print(n, " * ", i, " = ", (n * i))

# while loop

n = int(input("Enter no.: "))
i = 0
while(i <= 10):
    print(n, " * ", i, " = ", (n * i))
    i += 1
    
# nested loop

for i in range (1, 4):
    for j in range (1, 11):
        print(j, " ", end = "")
    print()

# Combination loop

for i in range(1, 11):
    if(i%2 == 0) :
        print(i)
        
i = 0
while (i <= 10) :
    if(i % 2 == 1) :
        print(i)
    i += 1

# break and continue statement

for i in range(1, 11) :
    if(i == 5) :
        continue
    if(i == 8) :
        break
    print(i)