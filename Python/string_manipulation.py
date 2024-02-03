# a = input("Enter name: ")
# print(a)
# print(type(a))
# print(len(a))
# print(a.count('u'))
# print(a.upper())
# print(a.lower())
# print(a.index('u'))
# print(a.capitalize())

# name = "Sujan"
# a = "Name is {}"
# print(a.format(name))

# a = "Sujan"
# print(a.center(10, '*'))



# String function -> part - 2

# str = "Sujan"
# print(str.isalnum()) # true if al chras are alphanumeric
# print(str.isalpha()) # true if al chras are alphabet

# str = "1234"
# print(str.isdecimal()) # true if all chras are decimal
# print(str.isdigit()) # true if all chras are digit
# print(str.isnumeric()) # true if all chras are neumeric

# str = "dfgd"
# print(str.islower()) # true if all chras are lower case
# str = "GHSD"
# print(str.isupper()) # true if all chras are upper

# str = "  "
# print(str.isspace()) # true if all chras are whitespace

# str1 = "Sujan Ghosh"
# str2 = "suJan GHOSH"
# print(str1.istitle())
# print(str2.istitle()) # true if string is title format


# String function -> part - 3

# str = "Sujan"
# print(str.endswith('n'))
# print(str.startswith('s'))

# str = "Sujan"
# print(str.swapcase())

# str = "  Sujan  "
# print(str)
# print(str.strip())

# a = "sd12#kdl#d87"
# print(a.split('#'))
# b = "Hello. Sujan. Indian"
# print(b.split('#'))

# str = "Sujan Ghosh"
# str = str.ljust(20, "*")
# print(str, " is an indian")

# str = "Sujan Ghosh"
# str = str.rjust(20, "*")
# print(str, " is an indian")

# String slicing

str = "Sujan  Ghosh"
print(str[0:6])
print(str[7:12])
print(str[:6])

str = "0123456789"
print(str[::2])
print(str[:7:2])
print(str[::-1])