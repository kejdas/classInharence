class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I have {self.age} years old")

class Cat(Pet):
    def __init__(self,name,age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("meow")

class Dog(Pet):
    def speak(self):
        print("bark")

p = Pet("Tim", 12)
p.show()
c = Cat("Kupa", 3, "Red")
c.speak()
d = Dog("Lali", 2)
d.speak()

