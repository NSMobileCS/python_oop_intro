from random import randrange

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15

    def __str__(self):
        return "price ${}K\n speed {}MPH\n fuel {}\n mileage {}\n tax {}".format(self.price,
                                                                    self.speed, 
                                                                    self.fuel, 
                                                                    self.mileage, 
                                                                    self.tax)

    def display_all(self):
        print(self)
        return self

cars = [Car(randrange(100),
            randrange(256),
            randrange(100),
            randrange(100)) for _ in range(6)]

for car in cars:
    car.display_all()