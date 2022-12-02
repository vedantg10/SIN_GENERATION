from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    userAgentUserID = "agent1@jabbim.com"
    userAgentPassword = "agent@123"
    jwtAgentUserId = "agent2@jabbim.com"
    jwtAgentPasswordId = "agent@123"
    sinGeneratorAgentUserId = "agent3@jabbim.com"
    sinGeneratorAgentPasswordId = "agent@123"
    verificationAgentUserId = "agent4@jabbim.com"
    verificationAgentPasswordId = "agent@123"
    databaseAgentUserId = "agent5@jabbim.com"
    databaseAgentPasswordId = "agent@123"

    # Agent IDs
    userAgentID = "1"
    jwtAgentID = "2"
    verificationAgentID = "3"
    databaseAgentID = "4"
    sinAgentId = "5"

    #Command IDs
    UserCreateJwtCommandId = "2"
    UserCreateVerificationCommandId = "3"
    UserCreateDatabaseCommandId = "4"
    UserCreateSinCommandId = "5"

    # Error Code
    SuccessAckID = "0"

    # Protocol Format
    ReceiverAgentIDIndex = 1

class UserAgentClass(Agent):
    class UserAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"UserAgentClass.UserAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            if AgentCommunication.CommunicationFlag:
                print(AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex])
                if AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.userAgentID:
                    msg = Message(to=AgentCommunication.userAgentUserID)  # Instantiate the message
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.jwtAgentID:
                    print("Sending message to jwt agent")
                    msg = Message(to=AgentCommunication.jwtAgentUserId)
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.verificationAgentID:
                    print("Sending message to Verification agent")
                    msg = Message(to=AgentCommunication.verificationAgentUserId)
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.databaseAgentID:
                    print("Sending message to Database agent")
                    msg = Message(to=AgentCommunication.databaseAgentUserId)
                else:
                    print("Sending message to SIN agent")
                    msg = Message(to=AgentCommunication.sinGeneratorAgentUserId)

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content
                msg.body = AgentCommunication.CommunicationTxBuffer

                # Send Message
                await self.send(msg)
                print("userAgentClass:userAgentBehaviour:run:msg:request:\"{}\"".format(msg.body))

                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)
                print (msg)

                if msg:
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    print("UserAgentClass:UserAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
                    AgentCommunication.CommunicationError = False
                    AgentCommunication.CommunicationFlag = False

                else:
                    AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    print("userAgentClass:userAgentBehaviour:run:msg:response:\"No Response\"")

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
    AgentCommunication.CommunicationTxBuffer = "SIN Generation portal"
    userAgent = UserAgentClass(AgentCommunication.userAgentUserID, AgentCommunication.userAgentPassword)
    # wait for receiver agent to be prepared.
    userAgent.start()
    userAgent.web.start(hostname="127.0.0.1", port="10000")
