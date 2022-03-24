


class Person:
    category = "person"

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age 
        self.weight = weight

john = Person("John", 15, 45)
mary = Person("Mary", 14, 40)
david = Person("David", 22, 50)

print("John is a {}".format(john.__class__.category))
print("Mary is also a {}".format(mary.__class__.category))
print("David is also a {}".format(david.__class__.category))

print("{} is {}years old.His weight is {}".format(john.name, john.age, john.weight))
print("{} is {}years old.Her weight is {}".format(mary.name, mary.age, mary.weight))
print("{} is {}years old.His weight is {}".format(david.name, david.age, david.weight))


class House:
    place = "house"

    def __init__(self,colour, type, year, location, owner):
        self.colour = colour
        self.type = type
        self.year = year
        self.location = location
        self.owner = owner

house_1 = House("Blue", "Mansionette", "Dubai", "2019", "Chris")


print("House_1 is {}".format(house_1.__class__.place))


print("The colour of the house is {}. The owner of the house is {}.")


class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self, marathon):
        return "{} runs a {}".format(self.name, marathon)

    def read(self, read):
            return "{} is now reading".format(self.name)

john = Persons("John", 15)

print(john.run("42 km" ))
print(john.read(""))