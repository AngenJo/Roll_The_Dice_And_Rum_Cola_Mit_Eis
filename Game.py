import socket
import sys

from Player import Player
from Rule import Rule
from User import User

#Game
class Game:
    player = []
    rule = None
    currentPlayer = None
    connectionList = []
    clientsList = []
    #,player
    def __init__(self):
        self.rule   = Rule()
        
    def getAction(self, index1, index2):
        ruleSet = self.rule.getRuleSet()
        tempRule = ruleSet[index1][index2]
        return tempRule

    def distributeSips(self, message):
        # to implement 
        Test = "Implement"

    def start(self):
        self.currentPlayer = self.player[0]
        currentindex = 0
        while True:
            currentindex += 1
            result1, result2 = self.currentPlayer.rollDices()
            response = self.sendMessageToAll("1"+str(result1)+str(result2))
            print(response)
            tempStart = currentindex
            while not self.player[currentindex].getJar():
                currentindex += 1
                if tempStart == currentindex:
                    return 0
                if currentindex - 1  > len(self.player):
                    currentindex = 0
            tempRule =  self.getAction(result1,result2)
            response = self.sendMessage(self.connectionList[currentindex],"2"+tempRule)
            self.distributeSips(response)

    def host(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (socket.gethostbyname(socket.gethostname()), 10000)
        print('starting up on %s port %s' % server_address)
        self.sock.bind(server_address)
        self.isHost = True
        self.sock.listen(MAX_USERS)

    def sendMessageToAll(self, message):
        message = message.encode()
        for connection in self.connectionList:
            connection.sendall(message)
            #recieve
        return "0"

    def sendMessage(self, connection, message):
        message =  message.encode()
        connection.sendall(message)
        #recieve
        return message.decode()

    def acceptClient(self):
        while True:
            connection, clientAddress = self.sock.accept()
            self.connectionList.append(connection)
            self.clientsList.append(clientAddress)
            self.player.append(Player(self.sendMessage(connection,"0")))
            print("Connected %s %s" % clientAddress)
