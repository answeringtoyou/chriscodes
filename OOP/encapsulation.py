class Car:

    def __init__(self):
        self.__updateSoftware()
    
    def drive(self):
            print("driving")

    def __updateSoftware(self):
        print("Updating Software")

teslacar = Car()
teslacar.drive()


class Cars:
    __maxSpeed = 0
    __name = ""

    def __init__(self):
        self.__maxSpeed = 200
        self.__name = "Tesla car"

    def drive(self):
        print("driving. maxSpeed " + str(self.__maxSpeed))

    #Using the setter mehtod to change the value of a private variable
    def setMaxSpeed(self, speed):
        self.__maxSpeed = speed

teslaCar = Cars()
teslaCar.drive()
teslaCar.setMaxSpeed(500)
teslaCar.drive()





