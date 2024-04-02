class parent:
    wealthy=1000
    homes=10
    farms=20

class child (parent):
    pass
c=child()
print(c.wealthy,"money")
print(c.farms , "farms ")
print(c.homes, "homes")
class grand_child(child):
  pass

g=grand_child()
print(g.wealthy, "money of grand child")
print(g.farms, "frams of grand child")
print(g.homes, "homes of grand child")
