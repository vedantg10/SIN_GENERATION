import email
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from agentController import AgentCommunication
from agentController import ApplicationData
from agentController import DatabaseAgentData
from agentController import JWT
import jwt
import application

class JwtAgentClass(Agent):
    class JwtAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"JwtAgentClass.JwtAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print(ReceivedMessage[1], ReceivedMessage[2])

                ''' Check Agent Receiver ID'''
                if not ReceivedMessage[0] == AgentCommunication.userAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")

                if commandID == AgentCommunication.UserCreateJwtCommandId:
                    'Get Data from Message body'
                    ApplicationData.email = ReceivedMessage[1]
                    ApplicationData.password = ReceivedMessage[2]
                    ApplicationData.password = JWT.salt + ApplicationData.password

                    payload = {
                        'email': ApplicationData.email,
                        'password': ApplicationData.password
                    }
                    encoded_jwt = jwt.encode(payload, JWT.secret, algorithm="HS256")

                    dbencodedJwt = application.RetrieveJWT(ApplicationData.email)
                    print("Message received from db for the user: ", dbencodedJwt['jwt'])

                msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                # Database agent call to get JWT for the user
                if(dbencodedJwt['jwt'] == encoded_jwt):
                    msg.body = "user authenticated"
                else:
                    msg.body = "User Not Authenticated"

                print("JwtAgwent:JwtAgentBehaviour:run:msg:response:{user signed in}")
                await self.send(msg)


    async def setup(self):
        b = self.JwtAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def JwtAgentStart():
    jwtAgent = JwtAgentClass(AgentCommunication.jwtAgentUserId, AgentCommunication.jwtAgentPassword)
    # wait for receiver agent to be prepared.
    jwtAgent.start().result()
    jwtAgent.web.start(hostname="127.0.0.4", port="10000")