# Project Name:
Online Social Insurance Number (SIN) generation system.
 
# Requirements:
There are 5 actors - agents that are required in the project as given below: <br />
·	User Agent
·	Verification Agent
·	Authorization Agent
·	Database Agent
·	SIN Generator Agent

# Scope:
The scope of this project is to create a web application for immigrants and citizens to generate their Social Insurance Number (SIN) online instead of physically going to Service Canada. Any person with valid documents can do the SIN generation process online within Canada.
 
# Functionalities of individual agents and workflow:
·	Web Portal to raise an application for SIN generation.
·	A user who can login to the SIN generator portal - web portal using Email id and Date of Birth and password.
·	Once the user enters the required information on the screen, this request being transferred to the backend to create a JWT (Json Web Token) token using authorization agent
·	After authorization, it lands on another web page to submit the SIN application along with necessary personal information I.e., passport number, study permit number, and study permit expiry date.
·	Using the above provided personal information, SIN will be generated with the help of SIN agent.
·	The generated SIN along with the passport number and an expiry date will be saved in the database agent.
·	After successful insert/update, SIN pdf is displayed on the screen and the user can download the pdf from the portal.


# What We Will Be Using:
·	Python 3.7
·	Tkinter (For GUI)
·	Spade (Multi Agent System Framework)
·	MongoDB (Database Management)
·	fpdf (PDF Report Generation)
·	Pillow (Documents Operation)

# Agents and their responsibilities:
Multi-agent systems technology allows for the development of autonomous software entities (intelligent agents) which are designed to communicate with each other. In our project, we are aiming to have a multi-agent system with the following agents:
·	User Agent – Responsible for taking input from the user such given name, last name, email address, Passport number, permit number, permit expiry date, DOB, etc.
·	Verification Agent – Responsible for verifying the details of the user like passport number, permit expiry date, permit number, etc.
·	Authorization Agent – Responsible for generation of a JWT (JSON Web Token) which will be used for authentication during login or signup of the user.
·	Database Agent – Responsible for handling database related CRUD (Add/Update/Delete) operations.
·	SIN Generator Agent – Responsible for generating Social Service Number.


# Agent System Architecture:

## Roles Model:
                              
![image](https://user-images.githubusercontent.com/51778763/205141912-d79bf58c-7a19-4c22-887d-263aa4305a0f.png)


## Agents Model:

 ![image](https://user-images.githubusercontent.com/51778763/205141941-e63f11c3-640b-4fa2-9378-3cc151f38303.png)

