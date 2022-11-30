import tkinter as tk
from tkcalendar import DateEntry
#from tkinter import *

#self = tk.Tk()
import re
SinPageFrame = tk.Frame()
# email
# password
# date_of_birth self.Entry4.get()
# first_name   self.Entry1.get()
# last_name    self.Entry2.get()
# passport_number self.Entry3.get()
# study_permit_number self.Entry5.get()
# study_permit_expiry self.Entry6.get()
class SinPage(SinPageFrame):
    def __init__(self, parent, controller ):
        tk.Frame.__init__(self, parent)
        self.geometry("1536x801+-8+-8")
        self.minsize(120, 1)
        self.maxsize(3844, 1071)
        self.resizable(1, 1)
        self.title("SIN GENERATION PORTAL")
        self.configure(background="#a6a6a6")
        self.configure(highlightbackground="#efcefd")
        self.configure(highlightcolor="#fff7c6")

        self.Message1 = tk.Message(self)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.203, relwidth=1.001)
        self.Message1.configure(background="#0E86D4")  # 0E86D4 #abcbf1
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(cursor="fleur")
        self.Message1.configure(font="-family {Segoe UI} -size 34 -weight bold -underline 1")
        self.Message1.configure(justify='center')
        self.Message1.configure(relief="groove")
        self.Message1.configure(text='''SIN Registration Form''')
        self.Message1.configure(width=1300)

        # First Name Entry Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.025, rely=0.21, height=27, width=150)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        #self.Button1.configure(command=first_name_button)
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text="First Name")

        # First Name Entry
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.2, rely=0.21, height=27, relwidth=0.2)
        self.Entry1.configure(background="#ecd1ca")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(cursor="hand2")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 15")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable="first_name")

        # Last Name Entry Button
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.025, rely=0.25, height=30, width=150)
        self.Button2.configure(background="#f1ed43")
        self.Button2.configure(borderwidth="3")
        #self.Button2.configure(command=last_name_button)
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text="Last Name")

        # Last Name Entry
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.2, rely=0.25, height=30, relwidth=0.2)
        self.Entry2.configure(background="#ecd1ca")
        self.Entry2.configure(borderwidth="5")
        self.Entry2.configure(cursor="hand2")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 15")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable="last_name")

        # Passport Number Entry Button
        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.025, rely=0.30, height=30, width=200)
        self.Button3.configure(background="#f1ed43")
        self.Button3.configure(borderwidth="3")
        #self.Button3.configure(command=passport_number_button)
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="Passport Number")

        # Last Name Entry
        self.Entry3 = tk.Entry(self)
        self.Entry3.place(relx=0.2, rely=0.30, height=30, relwidth=0.2)
        self.Entry3.configure(background="#ecd1ca")
        self.Entry3.configure(borderwidth="5")
        self.Entry3.configure(cursor="hand2")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 15")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable="passport_number")

        # DoB  Entry Button
        self.Button4 = tk.Button(self)
        self.Button4.place(relx=0.025, rely=0.35, height=30, width=200)
        self.Button4.configure(background="#f1ed43")
        self.Button4.configure(borderwidth="3")
        #self.Button4.configure(command=date_of_birth_button)
        self.Button4.configure(cursor="hand2")
        self.Button4.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(text="Date of Birth")

        # DoB Entry
        #date_of_birth = (DateEntry(self,selectmode='day') )
        self.Entry4 = DateEntry(self,selectmode='day')
        self.Entry4.place(relx=0.2, rely=0.35, height=30, relwidth=0.2)
        self.Entry4.configure(background="#ecd1ca")
        self.Entry4.configure(borderwidth="5")
        self.Entry4.configure(cursor="hand2")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="-family {Courier New} -size 15")
        self.Entry4.configure(foreground="#000000")
        #self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable="date_of_birth")

        # Study Permit Number Entry Button
        self.Button5 = tk.Button(self)
        self.Button5.place(relx=0.025, rely=0.40, height=30, width=225)
        self.Button5.configure(background="#f1ed43")
        self.Button5.configure(borderwidth="3")
        #self.Button5.configure(command=study_permit_number_button)
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text="Study Permit Number")

        # Study Permit Number Entry
        self.Entry5 = tk.Entry(self)
        self.Entry5.place(relx=0.2, rely=0.40, height=30, relwidth=0.2)
        self.Entry5.configure(background="#ecd1ca")
        self.Entry5.configure(borderwidth="5")
        self.Entry5.configure(cursor="hand2")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="-family {Courier New} -size 15")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable="study_permit_number")

        # Study Permit Expiry Entry Button
        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.025, rely=0.45, height=30, width=200)
        self.Button6.configure(background="#f1ed43")
        self.Button6.configure(borderwidth="3")
        #self.Button6.configure(command=study_permit_expiry)
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(text="Study Permit Expiry")

        # Study Permit Expiry
        #date_of_birth = (DateEntry(self,selectmode='day') )
        self.Entry6 = DateEntry(self,selectmode='day')
        self.Entry6.place(relx=0.2, rely=0.45, height=30, relwidth=0.2)
        self.Entry6.configure(background="#ecd1ca")
        self.Entry6.configure(borderwidth="5")
        self.Entry6.configure(cursor="hand2")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="-family {Courier New} -size 15")
        self.Entry6.configure(foreground="#000000")
        #self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(textvariable="study_permit_expiry")

        # Login Button
        self.Button7 = tk.Button(self)
        self.Button7.place(relx=0.040, rely=0.65, height=45, width=200)
        self.Button7.configure(background="#1eee52")
        self.Button7.configure(borderwidth="3")
        #self.Button7.configure(command=Submit)
        self.Button7.configure(cursor="hand2")
        self.Button7.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(text="Submit")