
# formatting
# emulate C style

st = "Welcome %s, what a %s player"
print(f"st :{st}")
values = ("Messi", "superb")            # tuple
print(f"values :{values}")
print(st % values)

print("Welcome %s, what a %s player" % ("Messi", "class"))
print("Welcome %s, with a rating of %d what a %s player" % ("Messi", 4, "class"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Messi", 4.8, "class"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Messi", 4.8456663, "class"))


print("-" * 40)
# interpolation
from math import pi, e

print(f"PI = {pi} and eulers constant E = {e}")

print("-" * 40)
# format of string functions
print("PI = {} and Eulers constant E = {}".format(pi, e))
print("PI = {0} and Eulers constant E = {1}".format(pi, e))
print("PI = {0:.3f} and Eulers constant E = {1:.3f}".format(pi, e))

print("-" * 40)
fname = ['Lionel', 'Messi']
print("Mr.{name}".format(name=fname))
print("Mr.{name[0]}".format(name=fname))
print("Mr.{name[1]}".format(name=fname))
print("Mr.{name[0]} {name[1]}".format(name=fname))

print("-" * 40)
print("Welcome {}, what a {} player".format("Messi", "class"))
print("Welcome {}, with a rating of {} what a {} player".format("Messi", 4, "class"))
print("Welcome {0}, with a rating of {1} what a {2} player".format("Messi", 4.876543, "class"))
print("Welcome {0}, with a rating of {1:.3f} what a {2} player".format("Messi", 4.876543, "class"))

print("Welcome {gname}, with a rating of {rating:.3f} what a {adj} player".format(gname = "Messi", rating = 4.876543, adj = "class"))

print("-" * 40)
import math
print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers e = {mod.e}".format(mod=math))

print("-" * 40)
print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))     # conversion

print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 363456456))
print("{num:05} {num:f} {num:b}".format(num = 36))
print("{num:010} {num:f} {num:b}".format(num = 36))

print("-" * 40)
print("{num:15} Messi ".format(num = "Lionel"))
print("{}".format("Lionel Messi"))
print("{:.6}".format("Lionel Messi"))

print("-" * 40)
print("{0:>15} Messi".format("Lionel"))          # right alignment
print("{0:^15} Messi".format("Lionel"))          # center alignment
print("{0:<15} Messi".format("Lionel"))          # left alignment

print("-" * 40)
print("{0:->15} Messi".format("Lionel"))          # right alignment
print("{0:*^15} Messi".format("Lionel"))          # center alignment
print("{0:#<15} Messi".format("Lionel"))          # left alignment

