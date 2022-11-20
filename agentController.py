class ApplicationData:
    userName = ""
    password = ""

class AgentCommunication:
    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    userAgentUserID = "jarvis01@jabbim.com"
    userAgentPassword = "Agentbased10"


    UserDataCommandID = "1"
    ReportDataCommandID = "2"
    UserDataUpdateCommandID = "3"
    UserDataAddCommandID = "4"
    UserDataDeleteCommandID = "5"

     # Agent IDs
    userAgentID = "1"
    SystemDatabaseAgentID = "2"

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