
"""
reverse or reversed
reverse will reverse the original list

reversed - will return a copy of the reversed list
"""

print("reversed".center(40, "-"))
l1 = [10, 6, 3, 1, 9, 2, 8, 4, 7, 5]

print(f"l1 :{l1}")

res = list(reversed(l1))

print(f"res :{res}")

print("sort".center(40, "-"))
"""
sort     - will sort the original 

sorted  - will return a copy of the sorted list

"""

l1 = [10, 6, 3, 1, 9, 2, 8, 4, 7, 5]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"descending :{res_desc}")

print("-" * 40)

l1 = [10,'z', 'a', 6, 'y', 'b', 3, 'x', 'c', 1,'w', 'd', 9, 'u', 'e', 2,'v', 'f', 8, 'p', 'h', 4, 's', 'i', 7,'t', 'g', 5, 179, 1690, 12345, 29, 280, 2345, 20345]

print(f"l1 :{l1}")

print("-" * 40)

res = sorted(l1, key=ascii)
print(f"res : {res}")

print("-" * 40)

res1 = res[0:res.index('z')+1] + sorted(res[res.index('z')+1:])
print(f"res1 :{res1}")