#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tkcalendar


# In[1]:


import tkinter as tk
from tkcalendar import DateEntry
from tkinter import *
my_w = tk.Tk()
import re     
#email
#password
#dob
#dob_reg
#first_name
#last_name
#pass_no
#std_permit_no
#std_permit_expiry


gen_sin_num = None 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
my_w.geometry("500x500")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
def validate(u_input):
    if(re.search(regex,u_input) and u_input.isalpha):
        print(True)
        b1.config(state='active')  
        return True        
    else:
        print(False)
        b1.config(state='disabled')  
        return False  
   
my_valid = my_w.register(validate)



l0=tk.Label(my_w, text="SIN Number Generator",width=20,font=("bold", 20))
l0.place(x=90,y=53)
l1=tk.Label(my_w,text='Email')
l1.place(x=95,y=130)
#l1.grid(row=1,column=1,padx=5,pady=20)
email = Entry(my_w,validate='focusout',validatecommand=(my_valid,'%P'))
email.place(x=240,y=130)
#e1.grid(row=1,column=2,padx=10)
l2=tk.Label(my_w, text="Date of Birth",width=20,font=("bold", 10))
l2.place(x=45,y=180)
#l2.grid(row=1,column=3,padx=5,pady=20)
dob =   DateEntry(my_w,selectmode='day')
dob.place(x=240,y=180)
#e2.grid(row=1,column=4)
L3 = tk.Label(my_w,text='Password') 
L3.place(x=86,y=230)
#L3.grid(row=2,column=3,padx=5,pady=20)
password = tk.Entry(my_w,width=10)
password.place(x=240,y=230)
#e3.grid(row=2,column=4)

def submit():
   # if()
  #  gen_sin_num = None
#email
#password
#dob
    print("---------------------------------------------------------------------------")
    print("Login email " + email.get()  )
    print("Login password " + password.get() )
    print("Login dob "+ dob.get())
    print("-----------------------------------------------------------------------------")
    #IF unsuccessful delete entry and ask user to enter again or if previous user give their sin number from database
    #e1.delete(0, END)
    
    if gen_sin_num is not None:      
        #If succesfull show SIN Number
        newWindow = Toplevel(my_w)
        newWindow.title("SIN Number")
        newWindow.geometry("500x500")
        Label(newWindow,
              text ="Your SIN is : "+gen_sin_num,width=35,font=("bold", 18) ).place(x=90,y=43)
        
    if gen_sin_num is None: 
        newWindow = Toplevel(my_w)
        newWindow.title("SIN Registration Form")
        newWindow.geometry("700x700")
#         Label(newWindow,
#               text ="Your SIN is : "+gen_sin_num,width=35,font=("bold", 18) ).place(x=90,y=43).pack()

        l0=tk.Label(newWindow, text="SIN Registration Generator",width=20,font=("bold", 20))
        l0.place(x=90,y=53)
        Label_1 = Label(newWindow, text="Date of Birth",width=20,font=("bold", 10)).place(x=95,y=130)
        global dob_reg
        dob_reg =   DateEntry(newWindow,selectmode='day').place(x=240,y=130)
        Label_2 = Label(newWindow,text='First Name')
        Label_2.place(x=135,y=180)
        global first_name
        first_name =  tk.Entry(newWindow,width=10).place(x=240,y=180)
        Label_3 = Label(newWindow,text='Last Name')
        Label_3.place(x=135,y=230)
        global last_name
        last_name =  tk.Entry(newWindow,width=10).place(x=240,y=230)
        Label_4 = Label(newWindow,text='Passport No')
        Label_4.place(x=135,y=280)
        global pass_no
        pass_no =  tk.Entry(newWindow,width=10).place(x=240,y=280)
        Label_5 = Label(newWindow,text='Study Permit No')
        Label_5.place(x=135,y=330)
        global std_permit_no
        std_permit_no =  tk.Entry(newWindow,width=10).place(x=240,y=330)
        Label_6 = Label(newWindow,text='Study Permit Expiry')
        Label_6.place(x=125,y=380)
        global std_permit_expiry
        std_permit_expiry =  DateEntry(newWindow,selectmode='day')
        std_permit_expiry.place(x=240,y=380)
        b2 = tk.Button(newWindow,text='Register',command=register).place(x=270,y=420)
        newWindow.mainloop()
        
def register():
    gen_sin_num = "909090998"
    print("-------------------------------------------------------------------------------------")
    print("Study Permit Expiry Date"+std_permit_expiry.get())
    #dob_reg
#first_name
#last_name
#pass_no
#std_permit_no
#std_permit_expirt
    print("--------------------------------------------------------------------------------------")
    if gen_sin_num is not None:      
        #If succesfull show SIN Number
   
        newWindow = Toplevel(my_w)
        newWindow.title("SIN Number")
        newWindow.geometry("500x500")
        Label(newWindow,
              text ="Your SIN is : "+gen_sin_num,width=35,font=("bold", 18) ).place(x=90,y=43)

b1 = tk.Button(my_w,text='Submit',command=submit)
b1.place(x=190,y=270)
#b1.grid(row=1,column=5)
my_w.mainloop()  # Keep the window open

    
#print(type(4.5))


# In[ ]:





# In[ ]:




