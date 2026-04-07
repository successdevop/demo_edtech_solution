class Kettle(object):
    power_source = "electricity"
    
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.55
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("================")
print("Model: {0.make}={0.price} : {1.make}={1.price}".format(kenwood, hamilton))
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
print(kenwood.on)

print("=============")
Kettle.switch_on(kenwood)
print(hamilton.on)
print(kenwood.on)
print("==============")
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)
print("========================")
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("==========================")
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print("switching to atomic power")
Kettle.power_source = "gas"
print(kenwood.power_source)




