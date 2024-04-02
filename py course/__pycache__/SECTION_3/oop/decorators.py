class employee :
    def __init__(self,first,last,email):
        self.first=first
        self.last=last
       # self.email= first +"."+last +"@gmail.com" we can solve this problem of not updating the email
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def fullname(self):
        return "{}{}".format(self.first,self.last)




e=employee("abubakar","warsame","email")
e.first="abdisalan"
print(e.first)
print(e.email)
print(e.fullname)