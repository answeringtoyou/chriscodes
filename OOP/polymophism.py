class Hen(object):
    def feed(self):
        print("eats seeds")

class Duck(object):
    def feed(self):
        print("filter feeding")

class Dove(object):
    def feed(self):
        print("tears flesh")

def canFeed(birdType):
    birdType.feed()

henObj = Hen()
duckObj = Duck()
doveObj = Dove()

canFeed(henObj)
canFeed(duckObj)
canFeed(doveObj)

#second example
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Suv(Vehicle):
    def drive(self):
        return 'SUV is a very comfortable vehicle'

    def stop(self):
        return'The SUV is very easy to control and make it stop'


class Bus(Vehicle):
    def drive(self):
        return 'A Bus is a very long vehicle'

    def stop(self):
        return'Be careful when stopping a Bus'
vehiclesObj = [Bus("Goes to CBD"),
Bus("Goes to other places from CBD"),
Suv("Tesla")]

for vehicle in vehiclesObj:
    print (vehicle.name + ':' + vehicle.drive())


class Learner:
    def __init__(self, name):
        self.name = name

    def think(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Student(Learner):
    def think(self):
        return 'This Studentis a quick problem solver'

    def write(self):
        return'This Students write faster than the human eyes recognition'

class Pupil(Learner):
    def think(self):
        return 'Thinking ahead isnt his greatest skill'

    def write(self):
        return'My grandmother writes faster than him'
learners = [Student("Problem solver"),
Student("Writes quickly"),
Pupil("Thinks averagely")]

for learner in learners:
    print (learner.name + ':' + learner.think())       



