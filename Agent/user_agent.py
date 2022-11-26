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

    userAgentUserID = "agent1@jabbim.com"
    userAgentPassword = "agent@123"
    jwtAgentUserId = "agent2@jabbim.com"
    jwtAgentPasswordId = "agent@123"

    # Agent IDs
    userAgentId = "1"
    jwtAgentId = "2"
    systemDatabaseAgentId = "3"
    sinGenerationID = "4"

    #Command IDs
    UserDataCommandId = "1"


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
            # print("SenderAgent:UserAgentBehaviour:run")
            if AgentCommunication.CommunicationFlag:
                print (AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex])
                if AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.userAgentID:
                    msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.jwtAgentID:
                    print ("sending messaaage")
                    msg = Message(to=AgentCommunication.jwtAgentUserId)

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
                    print("UserAgentClass:UserAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
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
    print("fghjkl;")

    AgentCommunication.CommunicationTxBuffer = SenderAgentID + ReceiverAgentID + CommandID + ErrorCode + Data
    AgentCommunication.CommunicationFlag = True
    while AgentCommunication.CommunicationFlag:
        pass

    # if Slave Agent is not responding
    if AgentCommunication.CommunicationError:
        AgentCommunication.CommunicationRxBuffer = ""

    return AgentCommunication.CommunicationRxBuffer

def userAgentStart():
    AgentCommunication.CommunicationTxBuffer = "Deep"
    userAgent = UserAgentClass(AgentCommunication.userAgentUserID, AgentCommunication.userAgentPassword)
    # wait for receiver agent to be prepared.
    userAgent.start()
    userAgent.web.start(hostname="127.0.0.1", port="10000")
