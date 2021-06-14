#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('500x500')
#Declaring Window Color
window.configure(background = "pink");
#Creating drop down box
options = ["I",
"II" , "III" , "IV"]
clicked= StringVar()
clicked.set("I")
#creating radiobutton
def viewSelected():
    choice  = var.get()
    if choice == 1:
       output = "cse"

    elif choice == 2:
       output =  "eee"
    
    elif choice == 3:
       output =  "mech"
    else:
        output = "Invalid selection"
var = IntVar()
#below fields are declared
Name = Label(window ,text = "Name").grid(row = 2,column = 1)
Course = Label(window ,text = "Course").grid(row = 4,column = 1)
branch = Label(window ,text = "Branch").grid(row = 6,column = 1)
year = Label(window ,text = "Year").grid(row = 12,column = 1)
college = Label(window ,text = "College").grid(row = 14,column = 1)
Interest = Label(window ,text = "Interest").grid(row = 16,column = 1)
Email = Label(window ,text = "Email Id").grid(row = 18,column = 1)
Mobile = Label(window ,text = "MobileNo").grid(row = 20 ,column = 1)
project1 = Label(window ,text = "Project1").grid(row = 22,column = 1)
project2 = Label(window ,text = "Project2").grid(row = 24,column = 1)
feedback =Label(window ,text = "Feedback").grid(row = 26,column = 1)


Name = Entry(window).grid(row = 2,column = 3)
Course = Entry(window).grid(row = 4,column =3)
branch=Radiobutton(window, text="cse", variable=var, value=6, command=viewSelected).grid(row = 6,column = 3)
Radiobutton(window, text="eee", variable=var, value=8, command=viewSelected).grid(row = 8,column = 3)
Radiobutton(window, text="mech", variable=var, value=10, command=viewSelected).grid(row = 10,column = 3)
year= OptionMenu(window,clicked,*options).grid(row = 12,column = 3)
college = Entry(window).grid(row = 14,column = 3)
Interest=Entry(window).grid(row = 16,column = 3)
Email = Entry(window).grid(row = 18,column = 3)
Mobile = Entry(window).grid(row = 20,column = 3)
project1=Entry(window).grid(row = 22,column = 3)
project2=Entry(window).grid(row = 24,column = 3)
feedback=Entry(window).grid(row = 26,column = 3)

#function declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=30,column=3)
window.mainloop()
