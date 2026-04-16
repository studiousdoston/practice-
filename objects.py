'''OBJECTS
  1. Objects
  2. Iterable Objects & Range
  3. Dictionaries
  4. Error handling 
  '''

import array  # package/module
import math
from math import floor, ceil
# NOTE:  we are importing only the methods from math package

print("=====What is object in Pyhton======")
# An object has state, methods, properties.
# In Python everything is considered to be objects

print(type("Hi"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Programming Paradigms => Functional & OOP programming
# OOP 4 Concepts => Abstractions| Encapsulation| Inheritance| Polimorphism
result = math.ceil(97.1)
print(result)  # 98

floorNum = math.floor(99.9)
print(floorNum)  # 99

result2 = ceil(18.4)
print(result2)  # 19
# NOTE: to use math methods without math. , I need to use from math import ceil, ..., ... sytnax


print("===== Error handling =====")
car_dict = dict(
    name="Toyota",
    year=2026,
    isEV=True
)

try:
  print("passed here")
  carSpeed = car_dict.speed
  result3 = car_dict["year"]
  print("result", result3)
except KeyError as err:
  print("No origin state property found:", err)
except AttributeError as err:
  print("No speed attribute found:", err)
else:
  print("Executed successfully!")
finally:
  print("Final closing logic")

