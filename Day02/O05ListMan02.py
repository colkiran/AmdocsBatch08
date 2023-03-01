
# add elements into the list - append, extend, insert

print("append".center(40, "-"))
# append adds one element into the list and the end of the list
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)

print(f"l1 :{l1}")
l1.append([10, 11, 12, 13, 14, 15])
print(f"l1 :{l1}")
print(F"l1[9] :{l1[9]}")
print(F"l1[9][2:5] :{l1[9][2:5]}")

