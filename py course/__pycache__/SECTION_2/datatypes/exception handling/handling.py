
#crashes the whole program 
try:
    print(3/0)


except ZeroDivisionError:
    print("Hey man Zerdivision error occured")
except ValueError:
    print("Hey man value error occured ")
print("hello")