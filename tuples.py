''' Tuple
  1. What is tuple 
  2. Unpacking arguments
  3. zip()
'''
print("==== What is tuple: tuple vs list ====")
# Java/ PHP/ NodeJS array <=> Python List

# using literal way
nums = [3, 5, 3, 1, 2]
print(nums)

# using constructor
letters = list("Hello world!")
print(letters)

fruits = ['Apple', 'Lemon', 'Banana', 'Kiwi']
print('fruits:', fruits)

fruits[2] = 'Melon'
print("fruits updated:", fruits)


print("====== TUPLES ======")
# we cannot change tuples elements once declared

animal = ('dog', 'deer', 'cat', 'fish')
tuple_obj = ('MIT', 100, True, None)
print(animal[0])
# animal[0] = 'falcon'  # TypeError: 'tuple' object does not support item assignment
