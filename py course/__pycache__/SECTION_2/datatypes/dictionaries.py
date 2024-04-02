"""d={1:"Muqdisho",2:"kismayo",3:"Beydhabo"}
#del
del(d)
print("data before clearing",d)
d.clear()

print("data after clearing ",d)"""
#Teacher information 
d={}
number=int(input("enter the number of teachers "))
i=1
while i <=number:
    name=input("enter the name of the teacher ")
    salary=input("enter the salary of the teacher ")
    d[name]=salary
    i=i+1
for teacher in d:
    print("name of the teacher",teacher,"salary of the teacher =",d[teacher])