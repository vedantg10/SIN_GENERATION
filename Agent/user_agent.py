import time
import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template


class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    userAgentUserID = "test@user.com"
    userAgentPassword = "test"

    # Agent IDs
    userAgentID = "1"
    systemDatabaseAgentID = "4"
    authorizationAgentID = "2"
    verificationAgentID = "3"
    sinGeneratorAgentID = "5"


    # Error Codes
    SuccessAckID = "0"
    DataNotFoundAckID = "1"
    DatabaseConnectionFailureAckID = "2"
    DataUpdateFailedAckID = "3"
    DataAddFailedAckID = "4"
    DataDeleteFailedAckID = "5"


    # Protocol Format
    SenderAgentIDIndex = 0
    ReceiverAgentIDIndex = 1
    CommandIDIndex = 2
    ErrorCodeIndex = 3
    # index reserved for :
    DataIndex = 5




class UserAgentClass(Agent):
    class UserAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"UserAgentClass.UserAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("SenderAgent:UserAgentBehaviour:run")
            if AgentCommunication.CommunicationFlag:
                if AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.userAgentID:
                    msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content
                msg.body = AgentCommunication.CommunicationTxBuffer

                  # Send Message
                await self.send(msg)
                print("userAgentClass:userAgentBehaviour:run:msg:request:\"{}\"".format(msg.body))

                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)

                if msg:
                    # Copy Received to Communication RX Buffer
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    print("WebPortalAgentClass:WebPortalAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
                    AgentCommunication.CommunicationError = False
                    AgentCommunication.CommunicationFlag = False

                else:
                    AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    print("userAgentClass:userAgentBehaviour:run:msg:response:\"No Response\"")

            # else:
                # No Messages to be sent
            #await asyncio.sleep(2)

    async def setup(self):
        print("userAgentClass:setup")
        b = self.UserAgentBehaviour()
        self.add_behaviour(b)

def RequestData(SenderAgentID, ReceiverAgentID, CommandID, ErrorCode, Data):

    AgentCommunication.CommunicationTxBuffer = SenderAgentID + ReceiverAgentID + CommandID + ErrorCode + Data
    AgentCommunication.CommunicationFlag = True
    while AgentCommunication.CommunicationFlag:
        pass

    # if Slave Agent is not responding
    if AgentCommunication.CommunicationError:
        AgentCommunication.CommunicationRxBuffer = ""

    return AgentCommunication.CommunicationRxBuffer

def userAgentStart():
    print ('user agent main start fn')
    AgentCommunication.CommunicationTxBuffer = "Deep"
    print (AgentCommunication.userAgentUserID, AgentCommunication.userAgentPassword)
    userAgent = UserAgentClass(AgentCommunication.userAgentUserID, AgentCommunication.userAgentPassword)
    print (userAgent)
    # wait for receiver agent to be prepared.
    userAgent.start().result()
    userAgent.web.start(hostname="127.0.0.1", port="10000")
