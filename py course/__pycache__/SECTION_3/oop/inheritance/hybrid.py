"""class parent:
    balance="20,000$"

class child1(parent):
    name1="child1"

class child2(parent):
    name2="child2"

class grand_child(child1,child2):
  pass

g=grand_child()
print(g.name2) """

class somalia:
    name="somalia"
    language="somali"
    color="black"
    religion="islam"
    culture="same"
    capital_city="Muqdisho"

class northern_somalia (somalia):
    def __init__(self,city,no_ofregions):
        self.city=city
        self.no_ofregions=no_ofregions
        self.no_of_people="7 milyan"
        self.waqooyi="gobolada waqooyi ila lowya cade"
s=northern_somalia("Hargeisa","5 regions")
print("rer waqooyi  data      //////---->")   
print(s.city)
print(s.no_ofregions)
print(s.no_of_people)
print(s.religion)
print(s.capital_city)

print("rer konnfureed data    //////---->")   

class sorthern_somalia(somalia):
    def __init__(self,city,no_ofregions):
        self.city=city
        self.no_ofregions=no_ofregions
        self.no_of_people="10 milyan"
        self.konfur="gobolada dhexe ila xududka"
n=sorthern_somalia("Beydhabo","13 regions")
print(n.city)
print(n.no_ofregions)
print(n.no_of_people)
print(n.religion)
print(n.capital_city)
print(n.name)


class population(northern_somalia,sorthern_somalia):  #MRO
    def __init__(self,city,no_ofregions):
        sorthern_somalia.__init__(self,city,no_ofregions)
        northern_somalia.__init__(self,city,no_ofregions)
    
     

p=population("xamar","18")
#print(p.city)
#print(p.konfur)

print(p.konfur)
print(p.waqooyi)


