#library
#function 
#loop for loop
#conditionals( if else )
#variables

# passWord
import getpass
import string
l_count= u_count=w_count=d_count=s_count=0
strength=0
def Tijaabi_passwordka ():
 
  global l_count,u_count,w_count,s_count,d_count,strength
  password=getpass.getpass("enter your password please ")
  for char in password:
    if char in string.ascii_lowercase:
      l_count+=1
    elif char in string.ascii_uppercase:
      u_count+=1
    elif char in string.whitespace:
      w_count+=1
    elif char in string.digits:
      d_count+=1
    else:
      s_count+=1
  if l_count >=1:
    strength+=1
  if u_count >=1:
    strength+=1
  if w_count >=1:
     strength+=1
  if d_count >=1:
    strength+=1
  if s_count >=1:
    strength+=1
  if strength == 1:
    print("your password is very weak ")
  if strength==2:
     print(" your password is weak please improve it ")
  if strength==3:
    print(" your password is good but you can improve ")
  if strength==4:
    print(" your password is strong but you can further improve it  ")
  if strength==5:
    print(" your password is very strong even hackers can not try  ")
 
Tijaabi_passwordka()
print("password information >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
 
print(f"number of lower case letters in the password={l_count}")
print(f"number of UPPER_CASE case letters in the password={u_count}")
print(f"number of whitespace in the password={w_count}")
print(f"number of digits in the password={d_count}")
print(f"number of special characters in the password={s_count}")


 


#Tijaabi_passwordka()

