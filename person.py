class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people_()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @staticmethod
    def skin(color):
        return color

print(Person.skin("White"))

