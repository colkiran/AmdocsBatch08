
print("index".center(40, "-"))

l2 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1]

print(f"l2 :{l2}")
print("-" * 40)

print("3 :", l2.index(3))
print("3 :", l2.index(3, l2.index(3)+1))
print("3 :", l2.index(3, l2.index(3, l2.index(3)+1)+1))

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

l2 = l1             # shallow copy - l2 copies the address of l1 along with data

print(f"l2 before :{l2}")

print("-" * 40)
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("\n", "-" * 40, "\n")

l3 = [11, 22, 33, 44, 55]
print(f"l3 before :{l3}")

l4 = l3.copy()          # deep copy - copies only the data to another location

print(f"l4 before :{l4}")
print("-" * 40)

l4.extend([66, 77, 88])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("\n", "-" * 40, "\n")

l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]

print(f"l5 before :{l5}")

l6 = l5.copy()

print(f"l6 before :{l6}")

print("-" * 40)

l6[3].extend([60, 70, 80, 90])

print(f"l6 after :{l6}")
print(f"l6 after :{l5}")

print("\n", "-" * 40, "\n")

l7 = [11, 12, 13, 14, [1, 2, 3, 4, 5], 15]
print(f"l7 before :{l7}")

from copy import deepcopy

l8 = deepcopy(l7)

print(f"l8 after :{l8}")

print("-" * 40)

l8[4].extend([6, 7, 8, 9])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

