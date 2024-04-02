class student:
    def __init__(self,name,roll_no,sub):
       self.name=name
       self.roll_no=roll_no
       self.sub=sub
    def accept(self):
        l=[]
       # names= self.name,self.roll_no,self.sub=l.append(names)
        self.name=input("enter the name of the student ")
        self.roll_no= input("input the roll number of the student ")
        self.sub= input("enter the marks of the students ")
    def display (self):
       print(self.name)
       print(self.roll_no)
       print(self.sub)
    def search(self):
       if self.name in :
         pass
          
     


s1=student(name="abubakar",)
s1.accept()
s1.display()