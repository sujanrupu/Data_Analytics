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

