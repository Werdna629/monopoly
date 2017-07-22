from player import Player
from board import Board, SpaceType, BuyableSpace
from random import randint

class GoToJail(Exception):
    pass

class Game:
    def __init__(self):
        self.players = []
        self.turn = 0 #Index of player in self.players
        self.board = Board()
        self.currentLocations = dict() #Player:index (int)
        self.roll = 0
        self.doubles = False
    
    def addPlayer(self, name):
        newPlayer = Player(name)
        self.players.append(newPlayer)
        self.currentLocations[newPlayer] = 0 #Start on Go
        
    def getCurrentPlayer(self) -> Player:
        return self.players[self.turn]
    
    def getSpaceOwner(self, s: BuyableSpace):
        for player in self.players:
            if s in player.properties:
                return player
        return None
        
    def changeTurn(self):
        self.turn = (self.turn + 1) % len(self.players)
        
    def exchangeRent(self, s: BuyableSpace, payer: Player, payee: Player):
        payee.receiveRent(payer.payRent(s))
        
    def changeLocation(self, player, amount):
        self.currentLocations[player] = (self.currentLocations[player] + self.roll) % self.board.size
    
    def roll(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        self.roll = die1 + die2
        self.doubles = (die1 == die2)
    
    def takeTurn(self, doublesCounter):
        self.roll()
        if self.doubles: #This might be out of order (like it might let players take their third turn), check later
            if doublesCounter < 2:
                self.takeTurn(doublesCounter + 1)
            else:
                raise GoToJail
        self.processSpace(self.board.spaces[self.currentLocations[self.getCurrentPlayer()]]) #rip anyone who reads this
            
    def processSpace(self, space):
        intent = True #Signifies whether player wants to buy space. For now this is always true, need to figure out a good solution for this later
        if space.spaceType == SpaceType.BUYABLE:
            if space.isOwned:
                self.exchangeRent(space, self.getCurrentPlayer(), self.getSpaceOwner(space))
            else:
                if intent:
                    if space.price > self.getCurrentPlayer().money:
                        break #TODO: Mortgage
                    else:
                        self.getCurrentPlayer().buy(space)
        else:
            #TODO: Community Chest/Chance whatever
            pass