
print("keys".center(40, "-"))
emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000, 'loc': 'NYK', 'gender': 'Male'}

print(f"emp :{emp}")
print("-" * 40)

k = emp.keys()
print(f"k :{k}")
print("-" * 40)

for k in emp.keys():
    print(k + " => " + str(emp[k]))

print("values".center(40, "-"))

emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000, 'loc': 'NYK', 'gender': 'Male'}

print(f"emp :{emp}")

v = emp.values()
print(v)

print("get".center(40, "-"))
emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000}

print(f"emp :{emp}")
print("-" * 40)

print(f"Name   :{emp.get('ename', 'Invalid Key, Please enter a valid key')}")
print(f"Gender :{emp.get('gender', 'Invalid Key, Please enter a valid key')}")


print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'kol', 'hyd', 'del']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("setdefault".center(40, "-"))
emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000}

print(f"emp :{emp}")

print("-" * 40)
emp.setdefault('age', 45)
emp.setdefault('desig', 'PM')
emp.setdefault('loc', 'NYK')
emp.setdefault('gender', 'Male')

print(f"emp :{emp}")

print('pop'.center(40, "-"))

emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000, 'loc': 'NYK', 'gender': 'Male'}

print(f"emp :{emp}")

print("-" *  40)
res = emp.pop('dept')
print(f"res :{res}")

res = emp.pop('age')
print(f"res :{res}")

# res = emp.pop()
# print(f"res :{res}")

print(f"emp :{emp}")

print("popitem".center(40, "-"))

emp = {'ename': 'Ben Johnson', 'age': 30, 'desig': 'TL', 'dept': 'procurement', 'sal': 65000, 'loc': 'NYK', 'gender': 'Male'}

print(f"emp :{emp}")

print("-" *  40)
res = emp.popitem()
print(f"res :{res}")

res = emp.popitem()
print(f"res :{res}")

print(f"emp :{emp}")

