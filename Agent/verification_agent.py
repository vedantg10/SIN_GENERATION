from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
import application


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

                    print("Message from db after retreiving sin data for the user: ", sinData)

                    #Logic to check if SIN data exists for the user or not
                    if(sinData == "" and len(sinData) < 9):
                        msg.body = "No SIN exists"
                    else:
                        msg.body = "SIN exists"
                    # ErrorCode = AgentCommunication.SuccessAckID
                print("VerificationAgent:VerificationAgentBehaviour:run:msg:response:{message Sent}")
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