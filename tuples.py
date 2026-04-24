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


print("====== UNPACKING ARGUMENTS ======")
groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']
(x, y, *z) = groups
print(x)
print(y)
print('Rest:', z)
print('---------------------------')

# *args > tuple


def calculate(*args):
    print('*args:', args)
    total = 1
    for x in args:
        total *= x
    print(f'the type(args) value: {type(args)}')
    print('total', total)
    return


# Call
calculate(1, 7, 9, 2)
print('---------------------------')
calculate(1, 4, 356, 2, 8, 7, 35)

# ** kwargs > dictionary


def introduce(**kwargs):
    print(f'The type (kwargs): {type(kwargs)}')
    print(f'Hi I am  {kwargs['name']} and I am {kwargs['age']} years old!')


# Call
introduce(name='Deen', age=25)
introduce(name='John', age=25, is_single=True)
print('---------------------------')


def greeting(*args, **kwargs):
    print('* args: ', args)
    print('**kwargs:', kwargs)


# Call
greeting('Hi', True, 10, name='Deen', age=22)


print("====== zip ======")
tuple_1 = (1, 2, 3, 4)
tuple_2 = ('a', 'b', 'c')

zipped = list(zip(tuple_1, tuple_2))
print('zipped:', zipped)  # zipped: [(1, 'a'), (2, 'b'), (3, 'c')]


