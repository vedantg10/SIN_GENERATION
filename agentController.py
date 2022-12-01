
class ApplicationData:
    userName = ""
    password = ""
    firstName = ""
    lastName = ""
    passportNumber = ""
    dateOfBirth = ""
    permitNumber = ""
    permitExpiry = ""

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
    verificationAgentUserId = "agent4@jabbim.com"
    verificationAgentPasswordId = "agent@123"
    databaseAgentUserId = "agent5@jabbim.com"
    databaseAgentPasswordId = "agent@123"

    # Command IDs
    UserCreateJwtCommandId = "2"
    UserCreateVerificationCommandId = "3"
    UserCreateDatabaseCommandId = "4"
    UserCreateSinCommandId = "5"

    # Agent IDs
    userAgentID = "1"
    jwtAgentID = "2"
    verificationAgentID = "3"
    databaseAgentID = "4"
    sinAgentId = "5"

    # Error Codes
    SuccessAckID = "0"

    # Protocol Format
    ReceiverAgentIDIndex = 1

class DatabaseAgentData:
    encoded_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAdXNlci5jb20iLCJwYXNzd29yZCI6InNvbWVTYWx0VmFsdWV0ZXN0In0.JyFt5w5AdBIH0CabY_b71ThqZsj_SDfG--8YUB04QW0"

class JWT:
    # jwt salt
    salt = "someSaltValue"

    # jwt secret
    secret = "someSecretValue"

from Agent import jwt_agent
from Agent import sin_agent
from Agent import verification_agent
from Agent import database_agent


def StartAgents():
    jwt_agent.JwtAgentStart()
    sin_agent.SinGeneratorAgentStart()
    verification_agent.VerificationAgentStart()
    database_agent.DatabaseAgentStart()