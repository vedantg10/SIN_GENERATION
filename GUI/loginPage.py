import tkinter.messagebox
from Agent import user_agent
from Agent.user_agent import AgentCommunication
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import *
from GUI import loginPage
import application

# Form Variables
userName = ""
password = ""
firstName = ""
lastName = ""
passportNumber = ""
dateOfBirth = ""
permitNumber = ""
permitExpiry = ""

loginPageFrame = tk.Frame


class loginPage(loginPageFrame):
    # Callbacks Here
    def Button1_Callback(self, controller):
        print('LoginPage Button 1 Pressed')

    def Button2_Callback(self, controller):
        print('LoginPage Button 2 Pressed')

    def Button3_Callback(self, controller):
        print('LoginPage Button 3 Pressed')
        self.UpdateEntryData()
        # Validation Checks
        if ((not application.userName) or (not application.password)):
            tkinter.messagebox.showerror(title="Error", message="Enter Username or Password")
        else:
            # Check Username in Database if matches
            if ((application.userName == application.user1_userName) and (
                    application.password == application.user1_password)):
                CommData = ":" + application.userName + ":" + application.password

                print("Calling JWT agent with data: ", CommData)
                ReceivedData = user_agent.RequestData(AgentCommunication.userAgentID, AgentCommunication.jwtAgentID,
                                                      AgentCommunication.UserCreateJwtCommandId
                                                      , AgentCommunication.SuccessAckID, CommData)
                print("Response from JWT agent: ", ReceivedData)

                self = tk.Tk()
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
                self.Button4.configure(cursor="hand2")
                self.Button4.configure(font="-family {Segoe UI} -size 15 -weight bold")
                self.Button4.configure(highlightcolor="black")
                self.Button4.configure(text="Date of Birth")

                # DoB Entry
                self.Entry4 = DateEntry(self, selectmode='day')
                self.Entry4.place(relx=0.2, rely=0.35, height=30, relwidth=0.2)
                self.Entry4.configure(background="#ecd1ca")
                self.Entry4.configure(borderwidth="5")
                self.Entry4.configure(cursor="hand2")
                self.Entry4.configure(disabledforeground="#a3a3a3")
                self.Entry4.configure(font="-family {Courier New} -size 15")
                self.Entry4.configure(foreground="#000000")
                self.Entry4.configure(textvariable="date_of_birth")

                # Study Permit Number Entry Button
                self.Button5 = tk.Button(self)
                self.Button5.place(relx=0.025, rely=0.40, height=30, width=225)
                self.Button5.configure(background="#f1ed43")
                self.Button5.configure(borderwidth="3")
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
                self.Button6.configure(cursor="hand2")
                self.Button6.configure(font="-family {Segoe UI} -size 15 -weight bold")
                self.Button6.configure(highlightcolor="black")
                self.Button6.configure(text="Study Permit Expiry")

                # Study Permit Expiry
                self.Entry6 = DateEntry(self, selectmode='day')
                self.Entry6.place(relx=0.2, rely=0.45, height=30, relwidth=0.2)
                self.Entry6.configure(background="#ecd1ca")
                self.Entry6.configure(borderwidth="5")
                self.Entry6.configure(cursor="hand2")
                self.Entry6.configure(disabledforeground="#a3a3a3")
                self.Entry6.configure(font="-family {Courier New} -size 15")
                self.Entry6.configure(foreground="#000000")
                self.Entry6.configure(textvariable="study_permit_expiry")

                self.Button7 = tk.Button(self)
                self.Button7.place(relx=0.040, rely=0.65, height=45, width=200)
                self.Button7.configure(background="#1eee52")
                self.Button7.configure(borderwidth="3")
                self.Button7.configure(command=lambda: Submit(self))
                self.Button7.configure(cursor="hand2")
                self.Button7.configure(font="-family {Segoe UI} -size 15 -weight bold")
                self.Button7.configure(highlightcolor="black")
                self.Button7.configure(text="Submit")

            # Call here to verification agent to check data
            def Submit(self):
                global firstName
                global lastName
                global passportNumber
                global dateOfBirth
                global permitNumber
                global permitExpiry
                firstName = self.Entry1.get()
                lastName = self.Entry2.get()
                passportNumber = self.Entry3.get()
                dateOfBirth = self.Entry4.get()
                permitNumber = self.Entry5.get()
                permitExpiry = self.Entry6.get()
                print("First Name:" + firstName)
                print("Last Name:" + lastName)
                print("Passport Number:" + passportNumber)
                print("Date of Birth:" + dateOfBirth)
                print("Study Permit Number:" + permitNumber)
                print("Study Permit Expiry:" + permitExpiry)

                print(ReceivedData, "Data from jwt_agent")
                CommData = ":" + firstName + ":" + lastName

                if (ReceivedData and ReceivedData == "user authenticated"):
                    print("Calling Verification agent with data: ", CommData)

                    VerificationData = user_agent.RequestData(AgentCommunication.userAgentID,
                                                              AgentCommunication.verificationAgentID,
                                                              AgentCommunication.UserCreateVerificationCommandId
                                                              , AgentCommunication.SuccessAckID, CommData)

                    print("Response from verification agent: ", VerificationData)
                    # Database agent used to create a new account
                    if (VerificationData == "No SIN exists"):
                        userData = ":" + firstName + ":" + lastName + ":" + passportNumber + ":" + dateOfBirth + ":" + permitNumber + ":" + permitExpiry
                        print("Calling Database agent with data: ", userData)

                        dataBaseResp = user_agent.RequestData(AgentCommunication.userAgentID,
                                                              AgentCommunication.databaseAgentID,
                                                              AgentCommunication.UserCreateDatabaseCommandId
                                                              , AgentCommunication.SuccessAckID, userData)

                        print("Response from database agent: ", dataBaseResp)
                    else:
                        tkinter.messagebox.showerror(title="Error", message="SIN number already exists")
                    # sin agent call to create a sin number
                    if (dataBaseResp == "success"):
                        userData = ":" + firstName + ":" + lastName
                        print("Calling SIN agent with data: ", userData)

                        sinData = user_agent.RequestData(AgentCommunication.userAgentID, AgentCommunication.sinAgentId,
                                                         AgentCommunication.UserCreateSinCommandId
                                                         , AgentCommunication.SuccessAckID, userData)

                        print("Response from SIN agent: ", sinData)

                    if (not (sinData == "" and len(sinData) < 9)):
                        manSin = sinData
                        final_w = tk.Tk()
                        final_w.geometry(
                            "{0}x{1}+0+0".format(final_w.winfo_screenwidth(), final_w.winfo_screenheight()))
                        final_w.configure(background="#ADD8E6")
                        final_w.title("SIN Number")
                        Label(final_w,
                              text="Your SIN is : " + manSin, width=45, bg="#fff7c6", fg="black",
                              font=("bold", 32)).place(x=90, y=43)
                        final_w.mainloop()

                else:
                    tkinter.messagebox.showerror(title="Error", message="Wrong Username or Password")



    def UpdateEntryData(self):
        application.userName = self.Entry1.get()
        application.password = self.Entry2.get()
        print("Username: " + application.userName)
        print("Password: " + application.password)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title of the Project
        self.Message1 = tk.Message(self)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.203, relwidth=1.001)
        self.Message1.configure(background="#0E86D4")  # 0E86D4 #abcbf1
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(cursor="fleur")
        self.Message1.configure(font="-family {Segoe UI} -size 34 -weight bold -underline 1")
        self.Message1.configure(justify='center')
        self.Message1.configure(relief="groove")
        self.Message1.configure(text='''SIN GENERATION PORTAL''')
        self.Message1.configure(width=1538)

        # Username Textbox Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.250, rely=0.389, height=64, width=207)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(command=lambda: loginPage.Button1_Callback(self, controller))
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text="Username")

        # Username Entry
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.400, rely=0.389, height=60, relwidth=0.257)
        self.Entry1.configure(background="#ecd1ca")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(cursor="arrow")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable="userName")

        # Password TextBox Button
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.250, rely=0.503, height=64, width=207)
        self.Button2.configure(background="#f1ed43")
        self.Button2.configure(borderwidth="3")
        self.Button2.configure(command=lambda: loginPage.Button2_Callback(self, controller))
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text="password")

        # Username Entry
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.400, rely=0.503, height=60, relwidth=0.257)
        self.Entry2.configure(background="#ecd1ca")
        self.Entry2.configure(borderwidth="5")
        self.Entry2.configure(cursor="arrow")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 20")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable="Password")
        self.Entry2.configure(show="*")

        # Login Button
        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.461, rely=0.628, height=64, width=207)
        self.Button3.configure(background="#1eee52")
        self.Button3.configure(borderwidth="3")
        self.Button3.configure(command=lambda: loginPage.Button3_Callback(self, controller))
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="Login")

