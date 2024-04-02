#overriding means the child class takes the a method with same name of the one of the parent class
# diiferent implementation 
#the method in the child class overrides the method in the parent class 
class shape:
    def area(self):
        return " The area of the parent shape is unknown "
class suqare(shape):
    
    def area (self,length):
        self.length=length
        return f" the area of the square= {self.length**2}"
s=suqare()
print(s.area(10))

    
