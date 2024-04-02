#class blue print 
#object
class car:
    # to make a constructor we need to create __init__() function 
    #constructor 
    #self stands for the instance or object
    def __init__(self,colour,price,comp):
        self.colour=colour
        self.price=price
        self.comp=comp
        


#objectname =classname()
blue_car=car("blue","1000$","Toyotta")   # when we created the object we have allocated memory 
#print(blue_car.colour)
#print(blue_car.price)
#print(blue_car.comp)

red_car=car("Red","2000$","Toyotta")
print(red_car.colour)
print(red_car.price)
#print(blue_car)
#print(car)