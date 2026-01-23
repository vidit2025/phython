class parrot:

    #Class attribute
    species="bird"

    # instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # instantiate the parrot class
blu = parrot("blu", 10)
woo = parrot("woo", 15)
# access the class atributes
print("Blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old" .format( blu.name, blu.age))
print("{} is {} years old" .format( woo.name, woo.age))