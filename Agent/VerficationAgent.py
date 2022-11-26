from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from agentController import ApplicationData
from agentController import JWT
from agentController import DatabaseAgentData

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
                if not ReceivedMessage[1] == AgentCommunication.UserAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.userAgentID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.GenerateReportCommandID:
                    'Get Data from Message body'
                    ApplicationData.email = ReceivedMessage[1]

                    #Get data for the user from the cloud database
                    sinData = ""


                    #Logic to check if SIN data exists for the user or not
                    if(sinData == "" and len(sinData) <= 9):
                        return True
                    else:
                        print("SIN exists for the user")
                        return False

                    #Database agent call to get JWT for the user
                    if(DatabaseAgentData.encoded_jwt == encoded_jwt):
                        return True
                    else:
                        return False

                    # ReportGeneration.GenerateReport(ApplicationData.Name, ApplicationData.HCNo, ApplicationData.DOB,
                    #                                 ApplicationData.Dose1Type, ApplicationData.Dose1Date, ApplicationData.Dose1Address,
                    #                                 ApplicationData.Dose2Type, ApplicationData.Dose2Date, ApplicationData.Dose2Address)
                    #
                    # file_str = encode_file_to_str("CovidReport.pdf")
                    ErrorCode = AgentCommunication.SuccessAckID

                    # Send response to Webportal agent
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.UserAgentID + \
                               commandID + \
                               ErrorCode + \
                               ':'

                print("UserAgentClass:UserAgentBehaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)


    async def setup(self):
        print("VerficationAgent:setup")
        b = self.VerificationAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def JwtAgentStart():
    jwtAgent = VerificationAgentClass(AgentCommunication.verificationAgentUserId, AgentCommunication.verificationAgentPasswordId)
    # wait for receiver agent to be prepared.
    jwtAgent.start().result()
    jwtAgent.web.start(hostname="127.0.0.5", port="10000")