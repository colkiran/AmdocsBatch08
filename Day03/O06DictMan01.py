
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': "Mike", 'age': '34', 'dept': 'finance', 'desig': 'MGR', 'sal': 85000}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'messi'), ('age', 35), ('goals', 350), ('club', 'PSG')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Tina", age=29, desig='TL', dept='QA', sal=60000)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
emp = {'ename': 'Ben', 'age': 30, 'desig': 'TL', 'dept': 'IT', 'sal': 65000}
print(f"emp :{emp}")

print("-" * 40)
# read
print(f"Name   :{emp['ename']}")
print(f"Age    :{emp['age']}")
print(f"Salary :{emp['sal']}")

print("-" * 40)
# iterate
for x in emp:
    print(x, " => ", emp[x])

print("-" * 40)
# modify
print(f"emp :{emp}")

emp['ename'] = "Ben Johnson"
emp['dept'] = 'procurement'
emp['loc'] = 'NYK'
emp['gender'] = 'Male'

print(f"emp :{emp}")

print("-" * 40)
# delete
print(f"emp :{emp}")

del emp['age']
del emp['dept']
del emp['loc']

print(f"emp :{emp}")

print("-" * 40)
print(dir(emp))
