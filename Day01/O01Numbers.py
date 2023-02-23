
a = 10
b = -10

print(f"a :{a}")            # format string or f string - interpolation
print(type(a))              # RTTI = runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 10.5
d = -10.5
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g = 10 + 0j
h = 10 - 0j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 40)

x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("conversions".center(40, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number system".center(40, "-"))
print(11)           # decimal numbers
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o101)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number System Conversion".center(40, "-"))
a = 100
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")

