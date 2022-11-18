import tkinter as tk
from pymongo import MongoClient
# import AgentController
from agentController import AgentCommunication
from agentController import ApplicationData
from Agent import user_agent


#import pages
from GUI import loginPage


#loginDATA
Curr_Frame = loginPage.loginPage
userName = "test@user.com"
password = "test"


def connectDatabase():
    try:
        myClient = MongoClient("mongodb://localhost:27017/")
        mydb = myClient["SIN_DATABASE"]
        mycol = mydb['userLoginDetails']
        for data in mycol.find():
            print (data)
    except Exception:
        print ("FAIELD")


class application(tk.Tk):
   def __init__(self, *args, **Kwargs):
    tk.Tk.__init__(self, *args, **Kwargs)
    tk.Tk.wm_title(self, "BTC")

    self.geometry("1536x801+-8+-8")
    self.minsize(120, 1)
    self.maxsize(3844, 1071)
    self.resizable(1, 1)
    self.title("SIN GENERATION PORTAL")
    self.configure(background="#a6a6a6")
    self.configure(highlightbackground="#efcefd")
    self.configure(highlightcolor="#fff7c6")

    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    self.frames = {}
    print (loginPage.loginPage)
    # for F in (loginPage.loginPage):
    #     frame = F(container, self)
    #     self.frames[F] = frame
    #     frame.grid(row=0, column=0, sticky="nsew")
    Curr_Frame = loginPage.loginPage
    self.show_frame(Curr_Frame)

def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

if __name__ =='__main__':
    print ('hi')
    user_agent.userAgentStart()
    app = application()
    app.mainloop()

