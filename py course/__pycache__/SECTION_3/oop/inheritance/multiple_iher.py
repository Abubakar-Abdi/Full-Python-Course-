class parent1:
    comp_name1="Hormuud"
    homes1="20 homes"



class parent2:
    comp_name2="somtel"
    homes2="30 homes"


class common_child(parent1,parent2):
    pass
c=common_child()
print(c.comp_name1)
print(c.comp_name2)
print(c.homes1)
print(c.homes2)

