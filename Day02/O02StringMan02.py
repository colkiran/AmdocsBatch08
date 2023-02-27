
print("find".center(40, "-"))

st1 = 'hello world'
st2 = 'the quick brown fox jumps over the lazy dog'

print(f"st1 :{st1}")
print("w :", st1.find("w"))     # returns the index

print("l :", st1.find("l"))
print("l :", st1.find("l", st1.find("l")+1))
print("l :", st1.find("l", st1.find("l", st1.find("l")+1)+1))

print("-" * 40)
print(f"st2 :{st2}")
print("fox :", st2.find("fox"))

print("the :", st2.find("the"))
print("the :", st2.find("the", st2.find("the")+1))

print("replace".center(40, "-"))
print(f"st1 :{st1}")

res = st1.replace("h", "H")
print(f"res :{res}")

res1 = st1.replace("l", "L")
print(f"res1 :{res1}")

res1 = st1.replace("l", "L", 2)
print(f"res1 :{res1}")

res1 = st1.replace("l", "L", 1)
print(f"res1 :{res1}")

print("-" * 40)
print(f"st2 :{st2}")

res2 = st2.replace("brown fox", "white tiger")
print(f"res2 :{res2}")

res2 = st2.replace("the", "The")
print(f"res2 :{res2}")

res2 = st2.replace("the", "The", 1)
print(f"res2 :{res2}")

# maketrans and translate
"""
change characters in a string byte by byte,
hello world => maketrans("l", "x") => hexxo worxd

"""
print("maketrans".center(40, "-"))
st = "hello world"      # covert to upper case
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# the length of a and b should be the same

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
