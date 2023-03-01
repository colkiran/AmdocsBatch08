
print("extend".center(40, "-"))
# used to add more than one element into the list and at the end of the list
l1 = list(range(1, 10, 2))
print(f"l1 :{l1}")
l1.extend([11, 13, 15])

print(f"l1 :{l1}")

print("insert".center(40, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)

l2.insert(15, 100)

print(f"l2 :{l2}")

# delete elements from the list - pop, remove, clear

print("clear".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()

print(f"l1 :{l1}")

print("pop".center(40, "-"))

l1 = list(range(1,11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(8)
print(f"res :{res}")

print(f"l1 :{l1}")
res = l1.pop()          # pops the last element in the list
print(f"res :{res}")

# res = l1.pop(10)
# print(f"res :{res}")

print(f"l1 :{l1}")

print("count".center(40, "-"))
l2 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1]

print(f"1 :{l2.count(1)}")
print(f"2 :{l2.count(2)}")
print(f"3 :{l2.count(3)}")
print(f"5 :{l2.count(5)}")

print("remove".center(40, "-"))

l2 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1]

print(f"l2 :{l2}")

l2.remove(3)
l2.remove(3)
l2.remove(3)

print("-" * 40)
print(f"l2 :{l2}")

while l2.count(1):
    l2.remove(1)

print("-" * 40)
print(f"l2 :{l2}")
