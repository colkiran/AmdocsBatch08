
#! c:\python\bin

print("Hello World")
print("Hello World")
print("Hello World")

"""
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 40)


def fun():

    print("hello world")
    print("this is function code")

    for i in range(1, 11):      # from 1 to < 11
        print("this is for loop code")

        if i % 2 == 1:
            print("if condition code")
            print(i)

fun()

print("-" * 40)

def fun1():
    # this is a comment
    """
	funtion fun takes two argument and both are of type integers

	fun will find the average of the two numbers passed

"""
    print("hello world")

fun1()

print("-" * 40)

print(fun1.__doc__)

print("-" * 40)

help(fun1)
