class somalia:
    count_name="somalia"
    city_name="mogadishu"
    def __init__(self,name,city,pre):
     self.magaca=name
     self.casimada=city
     self.madax=pre
     self.name=name
    
    def __repr__(self):
     return f"{self.name}"

jl=somalia("jubaland","kismayo","madobe ")
jl.magaca="puntland"
print(jl.count_name)

print(somalia.count_name)
