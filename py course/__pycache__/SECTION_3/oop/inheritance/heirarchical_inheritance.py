class employee:
    comp_name="Apple"



class developer(employee):
    pass
c1=developer()
print(c1.comp_name +   '\t',"child1 developer ")
class manager(employee):
    pass
c2=manager()
print(c2.comp_name +   '\t',"child2 manager")

class editter(employee):
    pass
c3=editter()
print(c3.comp_name +   '\t',"child3   editter")