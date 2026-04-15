print("===== numbers =====")
# in Java, variable is a name of storage location!
# in Python, variable is named reference!

count = 100
print("count:", count)
print("count is", type(count))
print(f"the count: {count} and type: {type(count)}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("===== strings =====")
# METHODS: upper(), lower(), title(), find(), replace()

course = "AI Python FullStack"
result = type(course)
# the type of course result (1) <class 'str'>
print(f"the type of course result (1) {result}")

result = course.title()
print(f" the result: result (2) {result}")  # Ai Python Fullstack

result = course.upper()
print(f"the result: result (3) {result}")  # AI PYTHON FULLSTACK

result = course.replace("FullStack", "MasterClass")
print(f"the result: result (4) {result}")  # AI Python MasterClass

print("===== boolean =====")
# FUNCTIONS => type(), input(), bool(), int(), str(),
y = input("Give some value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")


# TRUTHY vs FALSY values
# TRUTHY:True, str, int, dic
# FALSY: False, "", 0, None

test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("The TRUTHY:", bool(test_truthy))




















