# python pseudo code

# parent class
class Appliance :
    def __init__ (self, volts=0, weight=0, price=0.00) :
        self.volts = volts
        self.weight = weight
        self.price = price

    def discount(self, discount) :
        self.price = self.price - (self.price * discount)
        self.price = round(self.price,2)

# child class
class Toaster(Appliance):
    def __init__ (self, volts=120, price=20.00) :
    	self.price = price
    	self.volts = volts

# child class
class Blender(Appliance):
    def __init__ (self, weight=10) :
        self.weight = weight

# create blender object
blender = Blender()
blender.volts = 200
print(blender.volts) #output 200

# since by default price = 0, setting price will show discount
blender.price = 10.00
blender.discount(0.20) # output 8.0
print(blender.price)
