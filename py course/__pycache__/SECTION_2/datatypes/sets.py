"""s={1,2,3,"husen",True,23.8}
s2={10,11,12}
print('sets elements before adding number ',s)
s.add(34)
print("value before update ",s)
s.update(s2)
s.pop()
print("sets elements after adding number and also updating it",s)
print(type(s))"""
s={1,2,3,4,5}
#s.pop()
s.remove(1)
s.discard(5)
print(s)