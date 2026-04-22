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
print("is c equal to d ?", c == d) #only values is compared
print(id(c), id(d), id(e))


print("c is d:", c is d)
print("e is c", e is c)