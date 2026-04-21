'''CLASS
1. What is class
2. ordinary vs static method 
3. special methods
'''

print("==== What is class ====")
# class -> blueprint for object creation!
# structure -> state constructure method


class Person():
    # state
    message = "this is class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says peace upon you!")

    def say_age(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def explain(s):
        print("Static method property executed")
# NOTE Static methods must have one parameter to be executed correctly. I tried with NO parameter and TWO parameters, both did not work!


person_obj = Person("Deen", 21)
person2 = Person("John", 25)
person3 = Person("Kakashi", 34)

# ORDINARY STATE
print(person_obj.name)  # Deen

# ORDINARY METHOD
person_obj.introduce()  # Deen says peace upon you!
person2.say_age()  # John is 25 years old.


print(" ===== Ordinary vs static properties")

# STATIC PROPERTY
print("Message from the Person class", Person.message)
# Message from the Person class this is class state property

# STATIC METHOD
Person.explain()


print("==== MAGIC METHODS ====")

# Python's most common magic methods:
# __init__ , __new__ , __str__ , __call__ , __getitem__ , __leng__ , etc


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *arg):  #  💎*arg is a must. WHY cause we are using more than one arguments in __init__ magic method.
        print("* __new__*")
        return super().__new__(cls)
# NOTE:📝 KEEP IN MIND: before __init__ magic method, starts  __new__  method always runs in the back even though it is not written.

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"{self.name} started the engine!")

    def stop_engine(self):
        print(f"{self.name} stopped the engine!")

    def __str__(self):
        return f"The car.name: {self.name} was produced in {self.year}."
    
    def __call__(self):  # to make the object function alike
        print("Object is called as function!")
        return True 
my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-----------")
your_car = Car("Toyota", 2026)
#   * __new__*
print(your_car)  # The car.name: Toyota was produced in 2026.
response = your_car() # Object is called as function!
print("response:" , response)  # response: True

