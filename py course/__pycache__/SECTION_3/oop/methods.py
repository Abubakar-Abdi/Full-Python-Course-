#instance method ... regular function ..it just takes self= as the first argument 
#class method ...... decorator @classmethod .... first argument= cls
#static method ..... neither of these obove..decorator @static it does not need object 

class employee:
    company_name="Yaqiin ltd "  # class variable 
    employeenumber=0
    # variables ... class variables and instance varibales 
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
        employee.employeenumber+=1
    #@property
    def instancemeth(self):
        return self.position
    @classmethod
    def classmeth(cls):
        return cls.company_name
    @staticmethod
    def staticmeth(self):
       if len(self.name)>5:
           print("Bad")
       else:
       
         print("good")

employee1=employee("Xaashi","300$","junior")
employee2=employee("Xaashi","300$","junior")
employee3=employee("Xaashi","300$","junior")
employee4=employee("Xaashi","300$","junior")
#print(employee1.name)
#print(employee1.position)
#print(employee1.name,"calling instance variable using object ")
#print(employee.name)
employee1.name="abu"
employee1.position="growing junior "
employee.company_name="google "
#print(employee.company_name)
#print(employee1.position)
#print(employee1.company_name,"employee1")
#print(employee1.num)

#employee2=employee("abdi","1200$","senior")
#print(employee2.company_name,"employee 2")

#print(employee.company_name,"used class ")

#print(employee1.instancemeth())
#print(employee1.classmeth())
#print(employee.staticmeth())
print(employee.staticmeth(employee1.name))
print(employee.employeenumber)