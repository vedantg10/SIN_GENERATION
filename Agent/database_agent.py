from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from application import SaveDatabase

class DatabaseAgentClass(Agent):
    class DatabaseAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"DatabaseAgentClass.DatabaseAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            print("DatabaseAgent:DatabaseAgentBehaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("i am message from database agent", ReceivedMessage)

                ''' Check Agent Receiver ID'''
                if not ReceivedMessage[0] == AgentCommunication.userAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.UserCreateDatabaseCommandId:
                    userData = {
                        "firstName": ReceivedMessage[1],
                        "lastName": ReceivedMessage[2],
                        "passportNumber": ReceivedMessage[3],
                        "dateOfBirth": ReceivedMessage[4],
                        "permitNumber": ReceivedMessage[5],
                        "permitExpiry": ReceivedMessage[6]
                    }
                    '''Execute Save Data Query'''
                    Response = SaveDatabase(userData)

                    print("Response from the Database agent after saving data: ", Response)

                    # Send response to Webportal agent
                    msg.body = Response

                print("DatabaseAgent:DatabaseAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
                await self.send(msg)

    async def setup(self):
        print("DatabaseAgent:setup")
        b = self.DatabaseAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def DatabaseAgentStart():
    databaseAgent = DatabaseAgentClass(AgentCommunication.databaseAgentUserId, AgentCommunication.databaseAgentPasswordId)
    # wait for receiver agent to be prepared.
    databaseAgent.start().result()
    databaseAgent.web.start(hostname="127.0.0.5", port="10000")