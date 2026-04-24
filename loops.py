''' LOOP operators
  1. for
  2. while 
  3. break/ else
'''

print(" ====== for operator ======")
# Iterable objects: strings, dictionary, tuple, list, sets, range
text = "MIT"
nums = [10, 7, 3, 4]
car_obj = dict(brand="Toyota", year=2025)
range_obj = range(5)

# iterate through string
for letter in text:
    print(letter)

print("--------")

# iterate through int
for num in nums:
    print(num)

print("--------")

# iterate through a dictionary
for key in car_obj:
    print(f"the key: {key}, value: {car_obj.get(key)}")

print("--------")
for x in range(1, 20, 5):
    print(f"range: {x}")


print("==== break/else ====")
for x in range(1, 20, 5):
    print(f"x: {x}")
    if x > 10:
        print("reached break!")
        break

else:
    print("Looped ever successfully")


print("==== while operator ====")
number = 40
while number > -1:  # 0>-1 ✅
    number -= 10  # -10
    print(f'number = {number}')  # 30, 20, 10, 0, -10

print("--------")

count = 0
while True:
    count +=1 
    x = int(input("Enter number:"))

    if x == 41:
      print(f" You found the number in {count} attempt/s")
      break
    else:
        print("Wrong guess!")
