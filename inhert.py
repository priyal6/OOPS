# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")
# class Dog(Animal):
#     def __init__(self):
#         self.behaviour = "friendly"
#     def speak(self):
#         print(f"{self.name} barks. He is very {self.behaviour}")
# animal = Animal("Generic Animal")
# animal.speak()

# dog = Dog()
# dog.speak()

#dog is able to inherit the methods and attributes of the parent class Animal

class Animal:
    def __init__(self):
        self.name = "Buddy"
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}")

dog = Dog("Golden Retriever")
dog.speak()