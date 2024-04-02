"""
dicts=dict()
dicts['abubakar']=1
dicts["Hasan"]=2
print(dicts)
dicts['Adan']=dicts['abubakar']+2
print(dicts)


counts=dict()
names=['abdi','adan','xashi','Abdille','xashi','abdi','abdi','abdi']
for name in names:
    if name in counts:
        counts[name]=counts[name]+1
    else:
        counts[name]=1
print(counts) """
names={"abdi":21, "Asal":67,"bakorad":67}
x=names.get("abdi")
print(x)
