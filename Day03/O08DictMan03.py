
emp = {
    'emp1': {'ename': 'Steve', 'age': 32, 'desig': 'TL', 'dept': 'HR', 'sal': 50000},
    'emp2': {'ename': 'Jenifer', 'age': 30, 'desig': 'MGR', 'dept': 'Finance', 'sal': 75000},
    'emp3': {'ename': 'Richard', 'age': 39, 'desig': 'MGR', 'dept': 'IT', 'sal': 95000}
}

print(f"emp :{emp}")
print("-" *  40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")
print("-" *  40)

# items - combination of keys and values

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'ename': 'Steve', 'age': 32, 'desig': 'TL',  'sal': 50000}
emp2 = {'ename': 'Jenifer', 'age': 30, 'desig': 'MGR', 'dept': 'Fin'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)

emp1.update(emp2)
print(f"emp1 :{emp1}")
