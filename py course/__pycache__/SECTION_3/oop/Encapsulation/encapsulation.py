#class
#object
#constructor
#encapsulation
#inheritance
#Ploymorphisim

#modifiers ...public .... private....protected 
#protected .. can be only accessed inside the class or it's subclasses
class premier:
   balance=1000 #private can not accessed outside the class
   def __enc(self): # all of them are public by default 
      return self.balance
   


b=premier()
#print(b._balance)
print(b._enc(),"encapsulated protected func in parent class")

# class childclassname (parent_class_name)
class premierkm4 (premier):
   pass
k=premierkm4()
print(k._enc(),"protected encapsulated in child class")
#print(k._balance,"in premier km4")

class IBS:
   pass
i=IBS()
print(i._enc())
#print(i._balance)



