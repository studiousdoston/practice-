'''Comprehension
    1. What is comprehension & list comprehension
    2. Set and dictionary comprehensions 
'''

print("===== What is comprehension & list comprehension =====")

'''Compreheansion general syntax:
    a) *iterable 
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>'''

# list comp
nums = [1,2,1,3,5,6,8,5,23]
list_nums =[*nums] #                                  version A
print("list_nums:", list_nums)
print(nums is list_nums)
print(id(nums), id(list_nums))

print("--------------")
people = [("Deen", 22), ("Steve", 67), ("Yusuf", 28)]
list_people = [person[0] for person in people] #       version B

print("list_people:", list_people)
# list_people: ['Deen', 'Steve', 'Yusuf']

cars = [
  ("Ferrari", 78),
  ("Toyota", 87),
  ("Audi", 116),
  ("BMW", 109),
  ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80] #  version C

print("list_cars:", list_cars)
# list_cars: ['Toyota', 'Audi', 'BMW']
