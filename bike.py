class Bike:
    def __init__(self, name, price, max_speed, miles = 0):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        print self.name,"costs", self.price,"has", self.max_speed,"and" , self.miles, "mileage"
        return self
    def ride(self):
        self.miles += 10
        print self.name, "Riding", self.miles, "miles."
        return self
    def reverse(self):
        if self.miles < 5:
            print "cannot reverse anymore!!!"
            return self
        self.miles -= 5
        print self.name, "Reversing to", self.miles, "miles."
        return self

bike_one = Bike("BikeOne", "$100","30mph")
bike_two = Bike("BikeTwo", "$500","40mph")
bike_three = Bike("BikeThree", "$900","60mph")

bike_one.ride().ride().ride().reverse().displayInfo()
bike_two.ride().ride().reverse().reverse().displayInfo()
bike_three.reverse().reverse().reverse().displayInfo()

