from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from agentController import ApplicationData
from agentController import JWT
from agentController import DatabaseAgentData
import application

import jwt
# from ReportGeneration.Encoder_Decoder import encode_file_to_str
# from ReportGeneration import ReportGeneration


class VerificationAgentClass(Agent):
    class VerificationAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"VerificationAgentClass.VerificationAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            print("VerificationAgent:VerificationAgentBehaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print ("i am message from verification agent", ReceivedMessage)

                ''' Check Agent Receiver ID'''
                if not ReceivedMessage[0] == AgentCommunication.userAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.UserCreateVerificationCommandId:
                    'Get Data from Message body'
                    firstName = ReceivedMessage[1]
                    lastName = ReceivedMessage[2]

                    sinData = application.RetrieveDatabase(firstName, lastName)



                    #Get data for the user from the cloud database
                    # sinData = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAdXNlci5jb20iLCJwYXNzd29yZCI6InNvbWVTYWx0VmFsdWV0ZXN0In0.JyFt5w5AdBIH0CabY_b71ThqZsj_SDfG-"


                    #Logic to check if SIN data exists for the user or not
                    if(sinData == "" and len(sinData) <= 9):
                        msg.body = "No SIN exists"
                    else:
                        msg.body = "SIN exists"




                    # ReportGeneration.GenerateReport(ApplicationData.Name, ApplicationData.HCNo, ApplicationData.DOB,
                    #                                 ApplicationData.Dose1Type, ApplicationData.Dose1Date, ApplicationData.Dose1Address,
                    #                                 ApplicationData.Dose2Type, ApplicationData.Dose2Date, ApplicationData.Dose2Address)
                    #
                    # file_str = encode_file_to_str("CovidReport.pdf")
                    ErrorCode = AgentCommunication.SuccessAckID

                print("UserAgentClass:UserAgentBehaviour:run:msg:response:{message Sent}")

                #send message to user agent
                print("hi",msg.body)
                await self.send(msg)


    async def setup(self):
        print("VerficationAgent:setup")
        b = self.VerificationAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def VerificationAgentStart():
    verificationAgent = VerificationAgentClass(AgentCommunication.verificationAgentUserId, AgentCommunication.verificationAgentPasswordId)
    # wait for receiver agent to be prepared.
    verificationAgent.start()
    verificationAgent.web.start(hostname="127.0.0.5", port="10000")