class Person:
    def __init__(self):
        print("Person class is ready")
    def whoisThis(self):
        print("Person")

    def walk(self):
        print("walk to any direction")


class adult(Person):

    def __init__(self):
        super().__init__()
        print("Adult is ready")

    def whoisThis(self):
        print("Adult")

    def read(self):
        print("Reading")


charles = adult()
charles.whoisThis()
charles.walk()
charles.read()



class bus:
    def __init__(self):
        print("Bus class is off")
    def drive(self):
        print("Drive")

    def brake(self):
        print("Brake at stop sign")

    def hoot(self):
        print("Hoot at rouge cars")
    
