'''OPERATORS & CONDITIONS
      1. Operators
      2. Conditions
      3. Logical Operators 
'''
print("===== Operators =====")
# + - > >= < <= == is * /  // %  +=  *=

a = 19
b = 5
# print("a>b", a > b)
# print("a*b", a * b)
# print("a/b", a / b)

result = a // b
print("Floor divison:", result)

left = a % b
print("The reminder:", left)

a += 100
print("a:", a)

print("b squared:", b**2)
print("b cubed:", b**3)

print("="*10)

c = dict(name="Deen", age=22)
d = dict(name="Deen", age=22)
e = c
print("is c equal to d ?", c == d)  # only values is compared
print(id(c), id(d), id(e))


print("c is d:", c is d)
print("e is c", e is c)


print("===== Conditions =====")
x = 5

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")


print("="*10)

age = 19
# person = None
# if age> 16:
#     person =  "adult"
# else:
#     person = "child"


print("===== Logical Operators =====")

# Ternary operator
person = "adult" if age > 18 else "child"
print("The person is", person)

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome! do you wnat to become our student")
elif is_admin:
    print("Please head to the office!")
elif is_guest and is_parent:
    print("Waiting room is over there!")
else:
    print("Your case was not found")