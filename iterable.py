print("===== ITERABLE OBJECTS & RANGE =====")

# Iterable objects => string, dictionary, tuple, list, range, map, filter

range_obj = range(3)
print(range_obj)  # (0, 3)


text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(ele)  # 0 1 2


# NOTE: in JS we had OF keyword to iterate through the values and IN keyword to iterate through the indices. but Python does not support OF keyword 👌🏻 but uses IN to iterate through values.


print("==== DICTIONARIES ====")
# Dictionary is sometimes called JSON object by many!
# 1st way of creating objects
person = {
    "name": "Deen",
    "age": 25,
    "isMarried": False
}
# 2nd way if creating objects using dict
person_obj = dict(name="Johnny", age=25, isMarried=True)

print(f"The person: {person}")
print(f"The person_obj: {person_obj}")

name = person["name"]
# hobby = person["hobby"] this throws an error

hobby = person.get("hobby")
balance = person.get("balanace", 2000)
# NOTE: .get() method when used with objects can help add extra states to the object without mutating the original object

print(name)  # Deen
print(hobby)  # None
print("balance:", balance)  # balance: 2000
print(person)  # {'name': 'Deen', 'age': 25, 'isMarried': False}. NOT MUTATED
print(f"my name is {name} and {hobby} is my hobby, my balance is {balance}")
# my name is Deen and None is my hobby, my balance is 2000

for key in person:
    print(f"keys: {key}")  # name age isMarried

for values in person:
    print(f"values: {person[values]}") #Deen 25 False

del person["age"]
print(person)  # {'name': 'Deen', 'isMarried': False}