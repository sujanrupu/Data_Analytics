# Print Statement

print("Hello World")

print("""Hello Sujan,
Good Morning, Hope you are well.
Thanks, 
Python""")

print('It\'s raining')
print("it's raining")

a = "Hello World"
print(a)
a = 2
print(a)
a = True
print(a)
a = 'z'
print(a)

# User Input

name = input("Enter your name: ")
print(name)
age = int(input("Enter age: "))
print(age)

eq = input("Enter equation: ")
print(eq)
eq = eval(input("Enter equation: "))
print(eq)

# Data-type and type-casting

a = 2
print(type(a))
a = float(a)
print(type(a))

# Operator

print(4+2)
print(4-2)
print(4*2)
print(4/2)
print(5%2)
print(5//2)
print(4 ** 2)

print(2 == 3)
print(3>2)
print(3<2)

print(3>2 and 3<2)
print(3>2 or 3<2)

a = 5
a += 1    
print(a)
a -= 1
print(a)

a = 2
b = 4
print(a is b)
print(a is not b)

print(bin(5)) 
print(10 & 8)
print(bin(10 & 8))

a = "hello"
print('e' in a)

# Conditional statement

marks = 54
if marks>=90:
    print("Grade O")
elif marks>=50 and marks<90:
    print("Grade A")
else:
    print("Failed")


a = 2
b = 3
c = 4
if a>b:
    if a>c:
        print("a is largest")
    else:
        print("c is largest")
else:
    if b>c:
        print("b is largest")
    else:
        print("c is largest")