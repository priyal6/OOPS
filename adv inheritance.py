#multilevel - inheritance
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story")

# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working")

# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing")

# child = Child("Charlie")
# child.tell_story()
# child.work()
# child.play()


#heirarchical inheritance
# class Parent:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")
        
# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()

# child2.study()


#multilevel
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

# Intermediate class 1
class B(A):

    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()

# Intermediate class 2
class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()

# Derived class
class D(B, C):

    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()

# Create an instance of D
d = D("Frank")
d.greet()