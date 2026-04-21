''' CLASS deep dive
  1. ENCAPSULATION
  2. INHERITANCE
  3. POLYMORPHISM
'''

print("===== INHERITANCE =====")

#                PARENT
#            /     |     \
#        child   child   child

# NOTE:Parent class can only share its public and protected properties (state & methods) to children!📌


class Animal():  # Parent class
    # state
    description = "This class is parent class for  animal objects"

    # constructor
    def __init__(self, voice):
        self._status = f"The animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"This animal can make voice: {self.voice}")

# child 1


class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

# child 2


class Cat(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def play(self):
        print("Yes, I can play with you!")

# child 3


class Fish(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "Woof", True)
cat = Cat("Tommy", "Meaw", True)
fish = Fish("Nemo", "Zaz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-------------")
dog.make_voice()
fish.make_voice()

print("-------------")
print(Animal.description)  # This class is parent class for  animal objects
print(Dog.description)  # This class is parent class for  animal objects

print(dog.voice, fish.voice)  # True False
print("status:", dog._status)  # status:  The animal is alive
print("status:", cat._status)  # status:  The animal is alive
