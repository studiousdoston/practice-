'''List 
  1. Working with lists 
  2. Lists methods 
  3.Lambda function
  4. Enumerate(), map(), filter()
'''

print("====== Working with lists ======")

# literal
person = {'name': 'Deen', 'age': 25}  # dictionary
people = ('Andrew', 'John', 'Michael')  # tuple
groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']  # list
for team in groups:
    print(f'the team: {team}')


# constructor
result = list('Hello World!')
print(f'the letters: {result} and the size: {len(result)}')

print("-----------------")
fruits = ['apple', 'orange', 'lemon', 'kiwi']
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print('a:', a)
print('b:', b)
print('c', c)
print('reversed list:', d)

print("====== Built-in List Methods ======")
# methods ---> append(), insert(), pop(), remove(), clear(), sort(),index()

letters = ['a', 'd', 'b']
letters.append('c')
print(f'the append result: {letters}')

letters.insert(0, 'z')  # add front
print(f'the insert result: {letters}')

size = len(letters)-1
result1 = letters.pop(size)
print(f'the pop result: {result1} and {letters}')

result2 = letters.pop(0)  # pop front
print(f'the pop result: {result2} and letters: {letters}')


print("--------------")
animals = ['dog', 'cat', 'capybara', 'fish', 'lion']
print('animals:', animals)
animals.remove('lion')
print('remove:', animals)

del animals[2:4]
print('delete:', animals)

exist = animals.index('cat')
print('exist:', exist)

animals.clear()
print('clear:', animals)

if 'cat' in animals:
    print('index of cat:', animals.index('cat'))
else:
    print('cat does not exist')

print('---------------')
nums = [2, 3, 5, 55, 12, 23, 19, 89]
nums.sort()
print(f'nums:', nums)
nums.sort(reverse=True)
print('reversed:', nums)

# immutable sorted() & index()
numbers = [2, 7, 9, 5, 35, 67, 9, 63]
new_numbers = sorted(numbers)
print(f'the sorted numbers:{numbers} and new_numbers {new_numbers}')


print("====== Lambda functions ======")
# lambda is small anonymous function!


def calculate(x, y): return x*y


result = calculate(3, 5)
print(result)

people = [
    ('Robert', 20),
    ('Steve', 19),
    ('Joseph', 25),
    ('Michael', 30),
    ('Ali', 40)
]
people.sort()
print('people', people)

# sort by age using lambda
people.sort(key=lambda person: person[1])
print('sorted by age:', people)


print("====== Enumerate(), Map(), Filter() ======")
# enumerate for index & value

animals = ['dog', 'cat', 'fish']
for ele in enumerate(animals):
    print('element:', ele)
print('------------------')
for (i, value) in enumerate(animals):
    print(f'the index: {i} and value: {value}')

car_obj = dict(brand='Ferrari', year='2025')
result = car_obj.items()
print('result:', result)

for (key, value) in result:
    print(f'the key {key} and value: {value}')

print('---------------------')
cars = [
    ('Ferrari', 78),
    ('Toyota', 87),
    ('Audi', 116),
    ('BMW', 109),
    ('Pagani', 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print('new cars:', new_cars)

result1 = map(lambda car: car[0], cars)
print(f'the result1: {result1} and type: {type(result1)}')

new_cars2 = list(result1)
print('new cars2:', new_cars2)

print('-------------------')
# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(f'the filtered result: {result_filter} and type: {type(result_filter)}')
print(list(result_filter))