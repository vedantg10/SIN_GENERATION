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


class JwtAgentClass(Agent):
    class JwtAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"JwtAgentClass.JwtAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            # print("JwtAgent:JwtAgentBehaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print ("i am message from jwt", ReceivedMessage)

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
                    ApplicationData.password = ReceivedMessage[2]

                    #secret logic for jwt token
                    #appending salt with password to change the password
                    ApplicationData.password = JWT.salt + ApplicationData.password

                    payload = {
                        'email': ApplicationData.email,
                        'password': ApplicationData.password
                    }

                    encoded_jwt = jwt.encode(payload, JWT.secret, algorithm="HS256")
                    print(encoded_jwt)

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
        # print("JwtAgentClass:setup")
        b = self.JwtAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def JwtAgentStart():
    jwtAgent = JwtAgentClass(AgentCommunication.jwtAgentUserId, AgentCommunication.jwtAgentPassword)
    # wait for receiver agent to be prepared.
    jwtAgent.start().result()
    jwtAgent.web.start(hostname="127.0.0.4", port="10000")