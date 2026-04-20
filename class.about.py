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
#NOTE Static methods must have one parameter to be executed correctly. I tried with NO parameter and TWO parameters, both did not work!


person_obj = Person("Deen", 21)
person2 = Person("John", 25)
person3 = Person("Kakashi", 34)

# ORDINARY STATE
print(person_obj.name)  # Deen

#ORDINARY METHOD 
person_obj.introduce()  # Deen says peace upon you!
person2.say_age()  # John is 25 years old.


print(" ===== Ordinary vs static properties")

#STATIC PROPERTY
print("Message from the Person class", Person.message)
# Message from the Person class this is class state property

#STATIC METHOD 
Person.explain()


