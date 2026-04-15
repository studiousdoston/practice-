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
    print(f"What's up, {name}") # this one is void cause it does not have return 


def greeting(name):
    print("greeting function is executed")
    return f"Hi {name}"


# CALL -> execution part 
result1 = greet("Deen")
print(result1)

# CALL
result2 = greeting("Justin")
print(result2)
