class Person:
    "This is a person Class shown here"
    age = 14

    def greet(self):
        print("hello world")

davidObj = Person()

print(Person.age)
print(Person.greet)
print(Person.__doc__)
davidObj.greet()  #Person.greet(davidObj)









