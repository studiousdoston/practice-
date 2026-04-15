print("===== numbers =====")
# in Java, variable is a name of storage location!
# in Python, variable is named reference!

count = 100
print("count:", count)
print("count is", type(count))
print(f"the count: {count} and type: {type(count)}")

result1 = count.bit_count() #method
result2 = count.numerator # state
print(result1, result2)


print("===== strings =====")
# METHODS: upper(), lower(), title(), find(), replace()

course = "AI Python FullStack"
result = type(course)
print(f"the type of course result (1) {result}") # the type of course result (1) <class 'str'> 

result = course.title()
print(f" the result: result (2) {result}")  # Ai Python Fullstack

result = course.upper()
print(f"the result: result (3) {result}")  # AI PYTHON FULLSTACK

result = course.replace("FullStack", "MasterClass") 
print(f"the result: result (4) {result}")  # AI Python MasterClass

