#File Handling / File processing 
#Write, Read, Append
#Open()
#fileobject=open("filename","mode")
# mode "r","w","a", "r+","w+","a+"
#names=input("enter the names of your family ")
file=open("familynames.txt","a+")
file.write("Dahabo")
file.seek(0)
content=file.read()
print(content)

