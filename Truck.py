import datetime

class Truck:
    def __init__(self, capacity, speed, load, packageIdArray, miles, address, departureTime):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packageIdArray = packageIdArray
        self.miles = miles
        self.address = address
        self.departureTime = departureTime
        self.time = departureTime


truckNumberOne = Truck(16, 18, None, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truckNumberTwo = Truck(16, 18, None, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truckNumberThree = Truck(16, 18, None, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

