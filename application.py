import tkinter as tk
from pymongo import MongoClient
import agentController
from Agent import user_agent
from GUI.loginPage import loginPage

# loginDATA
Curr_Frame = loginPage

# userCredentials
user1_userName = "test@user.com"
user1_password = "test"

user2_userName = "test_1@user.com"
user2_password = "test1"

user3_userName = "test_2@user.com"
user3_password = "test2"

def SaveDatabase(userData):
    try:
        dbData = []
        # print("user", userData)
        myClient = MongoClient("mongodb://localhost:27017/")
        mydb = myClient["SIN_DATABASE"]
        mycol = mydb['userDetails']
        data = mycol.find()
        print("data",data)
        dbData.append(userData)
        mycol.insert_many(dbData)
        return "success"

    except Exception:
        print("FAILED")
        return "failure"

def RetrieveDatabase(firstName, lastName):
    try:
        myClient = MongoClient("mongodb://localhost:27017/")
        mydb = myClient["SIN_DATABASE"]
        mycol = mydb['sinData']
        for data in mycol.find({"firstName": firstName, "lastName": lastName}, {"SIN": 1}):
            print(data)
            return data

    except Exception:
        print("FAILED")
    return ""

def RetrieveJWT(email):
    try:
        myClient = MongoClient("mongodb://localhost:27017/")
        mydb = myClient["SIN_DATABASE"]
        mycol = mydb['userLoginDetails']
        for data in mycol.find({"name": email}, {"jwt": 1, '_id': 0}):
            print(data)
            return data

    except Exception:
        print("FAILED")
    return "failure"

def InsertSINData(userData):
    try:
        myClient = MongoClient("mongodb://localhost:27017/")
        mydb = myClient["SIN_DATABASE"]
        mycol = mydb['sinData']
        dbData = []
        dbData.append(userData)
        mycol.insert_many(dbData)
        return "success"

    except Exception:
        print("FAILED")
    return "failure"

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
        for F in (loginPage, loginPage):
            print(F)
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        Curr_Frame = loginPage
        self.show_frame(Curr_Frame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    agentController.StartAgents()
    user_agent.userAgentStart()
    app = application()
    app.mainloop()