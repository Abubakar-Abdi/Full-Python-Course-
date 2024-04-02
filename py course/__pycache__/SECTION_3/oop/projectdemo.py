import datetime
from  tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
#from datetime import DateEntry
headlabelfont=("calibri","15",'bold')
labelfont=("calibri","14",'bold')
entryfont=("calibri","14",'bold')

#database connection 
connector=sqlite3.connect("st.db")
cursor=connector.cursor()
connector.execute("CREATE TABLE IF NOT EXISTS STUDENT_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT)"
)
#GUI initialization
main=Tk()
main.title="tudent management system "
main.geometry("1000x1000")
# Creating the background and foreground color variables
lf_bg = 'SteelBlue' # bg color for the left_framelf_bg = 'SteelBlue'

#Creating string variables 
# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()
Label(main,text="STUDENT MANAGEMENT STYSTEM", font="Arial", background="skyblue").pack(side=TOP,fill=X)
Label(main,text="The best programmer and algorithim engineer is Aubakar warsame ", font="Arial", bg="white").pack()

#framing 
left_frame=Frame(main,bg=lf_bg)
left_frame.place(x=0,y=50,height=1000, width=400)
right_frame=Frame(main,bg="gray")
right_frame.place(x=400,y=50,height=1000, width=600)

# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(x=30, y=50)
Label(left_frame,text="contact_number", font=labelfont, bg=lf_bg).place(x=30,y=100)
Label(left_frame,text="Email_Address", font=labelfont, bg=lf_bg).place(x=30,y=150)
Label(left_frame,text="Gender", font=labelfont, bg=lf_bg).place(x=30,y=200)
Label(left_frame,text="Date of birth", font=labelfont, bg=lf_bg).place(x=30,y=250)
Label(left_frame,text="Stream", font=labelfont, bg=lf_bg).place(x=30,y=300)
Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=50)
Entry(left_frame,width=20,textvariable=contact_strvar).place(x=170,y=100)
Entry(left_frame,width=20,textvariable=email_strvar).place(x=170,y=150)
#Entry(left_frame,width=20,textvariable=gender_strvar).place(x=170,y=200)
Entry(left_frame,width=20,textvariable=stream_strvar).place(x=170,y=300)
OptionMenu(left_frame,gender_strvar, "male", "female" ).place(x=170,y=200)
DOB=DateEntry(left_frame,font=('arial',12),width=20).
DOB.place(x=170, y=250)






main.update()
main.mainloop()