class ApplicationData:
    userName = ""
    password = ""

class AgentCommunication:
    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    userAgentUserID = "agent1@jabbim.com"
    userAgentPassword = "agent@123"
    jwtAgentUserId = "agent2@jabbim.com"
    jwtAgentPassword = "agent@123"
    sinGeneratorAgentUserId = "agent3@jabbim.com"
    sinGeneratorAgentPasswordId = "agent@123"
    verificationAgentUserId = "agent3@jabbim.com"
    verificationAgentPasswordId = "agent@123"

    UserDataCommandID = "1"
    ReportDataCommandID = "2"
    UserDataUpdateCommandID = "3"
    UserDataAddCommandID = "4"
    UserDataDeleteCommandID = "5"

     # Agent IDs
    userAgentID = "1"
    jwtAgentID = "2"
    sinAgentId = "3"
    verificationAgentId = "4"

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

class DatabaseAgentData:
    encoded_jwt = ""

class JWT:
    #jwt salt
    salt = "someSaltValue"
    
    #jwt secret
    secret = "someSecretValue"

from Agent import jwt_agent
from Agent import sin_agent
from Agent import verification_agent
def StartAgents():
    jwt_agent.JwtAgentStart()
    sin_agent.SinGeneratorAgentStart()
    verification_agent.VerificationAgentStart()