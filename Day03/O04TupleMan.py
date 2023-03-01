
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(2, 11, 2))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
# t4 = [1, 2, 3],
# t4 = {1: 'a', 2: 'b'},
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
# t1 = (1, 2, 3, 4, 5)
# print(f"t1[0] :{t1[0]}")
# t1[0] = 100
# print(dir(t1))

# t1.index()
# t1.count()

t1 = tuple(range(1, 6))
print(f"t1 :{t1}")
l1 = list(t1)
print(f"l1 :{l1}")
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)

print(f"l1 :{l1}")
t1 = tuple(l1)
print(f"t1 :{t1}")