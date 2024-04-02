class employee:
    company_name="Yaqiin ltd "  # class variable 
    num=0
    # variables ... class variables and instance varibales 
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
        employee.num+=1
employee1=employee("Xaashi","300$","junior")
employee2=employee("Xaashi","300$","junior")
#print(employee1.name)
#print(employee1.position)
#print(employee1.name,"calling instance variable using object ")
#print(employee.name)
employee1.name="abubakar"
employee1.position="growing junior "
employee.company_name="google "
print(employee.company_name)
print(employee1.position)
print(employee1.company_name,"employee1")
print(employee1.num)

#employee2=employee("abdi","1200$","senior")
#print(employee2.company_name,"employee 2")

#print(employee.company_name,"used class ")