''' FUNCTIONS

   1. Define  vs  Call
   2. Parameter vs Arguments
   3. Keyword & default arguments
   4. Scope
'''
print("==== DEFINE vs CALL ====")
# built-in functions => print() type()
# function -> reusable block of code
# Instead of block {} in langs like java, JS, C langs, Python uses indentation!

# DEFINE -> building part


def greet(name):
    # this one is void cause it does not have return
    print(f"What's up, {name}")


def greeting(name):
    print("greeting function is executed")
    return f"Hi {name}"


# CALL -> execution part
result1 = greet("Deen")
print(result1)

# CALL
result2 = greeting("Justin")
print(result2)


print("==== Keyword & Default arguments ====")
# DEFINE


def sayHi(name, age="over 25"):
    print("sayHi function is executed")
    return f"Hi {name}! you are {age} years old right?"


# CALL
result3 = sayHi(name="Deen", age=21)
print("result3", result3)

result4 = sayHi("John")
print("result4", result4)
