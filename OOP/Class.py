# Class with private Attribute, Methods and Object Creation
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def info(self):
        return f"Animal name is {self.__name} and {self.age} years old"


animal = Animal("Hulk", 2)
print("Animal info : ", animal.info())


# Inheritance
class Dog(Animal):
    def info(self):
        return f"Dog age is {self.age} years old"


dog = Dog("Chris", 1)
print("Dog info : ", dog.info())

#
