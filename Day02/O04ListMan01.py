
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.9, 8.1, 9.0, 10+2j, 11-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(10, 101, 10))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
#memory allocation
l1 = [1, 2, 3, 'four', 'five', 'six']
print(f"l1 :{l1}")

print(f"id(l1[0]) :{id(l1[0])}")
print(f"id(l1[1]) :{id(l1[1])}")
print(f"id(l1[2]) :{id(l1[2])}")
print(f"id(l1[3]) :{id(l1[3])}")
print(f"id(l1[4]) :{id(l1[4])}")

print("-" * 40)
# creation
l2 = list(range(1, 11))
print(f"l2 :{l2}")

print("-" * 40)
# read
print(f"l2[3] :{l2[3]}")
print(f"l2[7] :{l2[7]}")

# iterate
for i in l2:
    print(i, end=" ")
print()

print("-" * 40)
# modify
print(f"l2 :{l2}")
l2[0] = 100             # replacement
l2[3] = 4.5             # insertion

print(f"l2 :{l2}")
# We cannot insert a new value into the list

print("-" * 40)
# delete values
del l2[4]
del l2[8]

print(f"l2 :{l2}")

print("-" * 40)
print(dir(l1))

