from player import Player
from board import Board, SpaceType
from random import randint

class GoToJail(Exception):
    pass

class Game:
    def __init__(self):
        self.players = []
        self.turn = 0 #Index of player in self.players
        self.board = Board()
        self.currentLocations = dict()
        self.roll = 0
        self.doubles = False
    
    def addPlayer(self, name):
        newPlayer = Player(name)
        self.players.append(newPlayer)
        self.currentLocations[newPlayer] = 0 #Start on Go
        
    def changeTurn(self):
        self.turn = (self.turn + 1) % len(self.players)
        
    def changeLocation(self, player, amount):
        self.currentLocations[player] = (self.currentLocations[player] + self.roll) % self.board.size
    
    def roll(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        self.roll = die1 + die2
        self.doubles = (die1 == die2)
    
    def takeTurn(self, doublesCounter):
        self.roll()
        self.processSpace(self.board.spaces[self.currentLocations[self.players[self.turn]]]) #rip anyone who reads this
        if self.doubles: #This might be out of order (like it might let players take their third turn), check later
            if doublesCounter < 2:
                self.takeTurn(doublesCounter + 1)
            else:
                raise GoToJail
            
    def processSpace(self, space):
        if space.spaceType == SpaceType.BUYABLE:
            pass