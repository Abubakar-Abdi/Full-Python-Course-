class employee2:
    raise_amount=1.04
 
    def __init__(cls,self,name,pay):
        cls.name=name
        cls.pay=pay
    def amount(self):
        self.pay=  ((self.pay+self.raise_amount))
    @classmethod
    def gain(cls):
        cls.raise_amount=200




employee2.raise_amount=1.89
employee2.gain()
print(employee2.gain())
print(employee2.raise_amount)
print("abubakar".__len__())
