class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def __str__(self):
        return "price {}, max_speed {}, miles {}".format(self.price,
                                                self.max_speed,
                                                self.miles)

    def displayInfo(self):
        print(str(self))
        return self

    def ride(self):
        print("riding!")
        self.miles += 10
        return self

    def reverse(self):
        print("reverse")
        self.miles = abs(self.miles - 5) #seems like a consistent way to define distance
        return self                     

b = Bike(140, '55kph', miles=111)
b.ride().displayInfo().ride().displayInfo().reverse().displayInfo().ride().displayInfo()
