# function 

def hello(name):
    print("Hello: ", name)
hello("Sujan")

def hello():
    print("Hello World")
hello()

def add(nums):
    total = 0
    for i in nums:
        total += i
    return total
print(add([1, 2, 3, 4]))

# Recursion

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))

# Lambda function

a = lambda b : b * 5
print(a(4))

