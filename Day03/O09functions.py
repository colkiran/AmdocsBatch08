
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# city is called the default argument
# gname is called non default argument
# a non default argument should not follow a default argument

def greetGstCty(gname,  city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")

greet()

print("-" * 40)
greetGst("Sachin")
greetGst("Rahul")

print("-" * 40)
greetGstCty('Sachin')
greetGstCty('Virat')
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
# named arguments

def admission(fn, ln, dob, qlf, exp, conno, email, gender):
    print(f"Name          :{fn} {ln}")
    print(f"DOB           :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Experience    :{exp}")
    print(f"Contact no.   : {conno}")
    print(f"Email         :{email}")
    print(f"Gender        :{gender}")


admission(gender='Male', exp='8 yrs', conno='56564632', fn="John", ln='Kennedy', email='jk@gmail.com', dob='10/04/1987', qlf='Mtech')


print("-" * 40)
# Variable length arguments
# ---------------------------

def multiplyMe(*numbers):       # *numbers can accept more than one number
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(multiplyMe(1, 2, 3, 4, 5))

print("-" * 40)

def extractDetails(**details):    # **details will accept data like a dictionary
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name='sachin', age=34, runs=125, oppn='Australia', loc='Perth')

print("-" * 40)
# python supports recursive calls

def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num - 1)

n = 5
print(f"The factorial of {n} is :{fact(n)}")

print("-" * 40)

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    flr_div = x // y
    return sum, diff, prod, quot, flr_div

print(arithCalc(20, 8))
