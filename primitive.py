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