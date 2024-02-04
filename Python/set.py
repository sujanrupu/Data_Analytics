# Set

a = {1, 2, 3, 4}
b = {5, 6, 7}
c = {2, 3}

print(a.isdisjoint(b))
print(a.issubset(c))
print(a.issuperset(b))

print(a.union(b))
print(a.intersection(c))
x = a.difference(c)
print(x)

print(a.intersection_update(c))
print(a)

