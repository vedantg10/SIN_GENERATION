from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from agentController import ApplicationData
from agentController import JWT
from agentController import DatabaseAgentData

import random




# from ReportGeneration.Encoder_Decoder import encode_file_to_str
# from ReportGeneration import ReportGeneration


class SinGeneratorAgentClass(Agent):
    class SinGeneratorBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"SinGeneratorAgentClass.SinGeneratorBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            print("SinGenerator:SinGeneratorBehaviour:run")

            msg = await self.receive(timeout=10)  # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("i am message from sin generator agent", ReceivedMessage)

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
                    ApplicationData.passport = ReceivedMessage[2]

                    generatedSIN = random.randrange(100000000, 999999999)

                    print(generatedSIN)

                    # Database call to save generated SIN against the user

                    # ReportGeneration.GenerateReport(ApplicationData.Name, ApplicationData.HCNo, ApplicationData.DOB,
                    #                                 ApplicationData.Dose1Type, ApplicationData.Dose1Date, ApplicationData.Dose1Address,
                    #                                 ApplicationData.Dose2Type, ApplicationData.Dose2Date, ApplicationData.Dose2Address)
                    #
                    # file_str = encode_file_to_str("CovidReport.pdf")
                    ErrorCode = AgentCommunication.SuccessAckID

                    # Sending response to user agent with the generated SIN number
                    msg.body = "SIN generated"

                print("SinGeneratorClass:SinGeneratorBehaviour:run:msg:response:{sin number sent Sent}")
                await self.send(msg)

    async def setup(self):
        print("SinGeneratorAgent:setup")
        b = self.SinGeneratorBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


def SinGeneratorAgentStart():
    sinAgent = SinGeneratorAgentClass(AgentCommunication.sinGeneratorAgentUserId,
                                      AgentCommunication.sinGeneratorAgentPasswordId)
    # wait for receiver agent to be prepared.
    sinAgent.start()
    sinAgent.web.start(hostname="127.0.0.6", port="10000")