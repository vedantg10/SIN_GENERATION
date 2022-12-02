from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from agentController import ApplicationData
import random
import application

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
                if not ReceivedMessage[0] == AgentCommunication.userAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.UserCreateSinCommandId:
                    'Get Data from Message body'
                    ApplicationData.email = ReceivedMessage[1]
                    ApplicationData.passport = ReceivedMessage[2]

                    generatedSIN = random.randrange(100000000, 999999999)

                    userData = {
                        "firstName": ReceivedMessage[1],
                        "lastName": ReceivedMessage[2],
                        "SIN": generatedSIN
                    }
                    dbResponse = application.InsertSINData(userData)

                    print("Response after inserting the SIN number in the Database", dbResponse)

                    print("mainsin",generatedSIN)

                    # Sending response to user agent with the generated SIN number
                    msg.body = str(generatedSIN)

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