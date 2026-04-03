<<<<<<< HEAD
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()

c.sell()

# change the price

c.__maxprice = 1000

c.sell()

# using setter function

c.setMaxPrice(1000)

=======
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()

c.sell()

# change the price

c.__maxprice = 1000

c.sell()

# using setter function

c.setMaxPrice(1000)

>>>>>>> e8ce271afc779164b220b9d5c8d606bdd7e82efa
c.sell()              