from enum import Enum

class Board:
    def __init__(self):
        self.spaces = []
        self.size = len(self.spaces)
        
class SpaceType(Enum):
    PROPERTY = 1
    CHANCE = 2
    COMMUNITYCHEST = 3
    GO = 4
    JAIL = 5
    FREEPARKING = 6
    GOTOJAIL = 7
    INCOMETAX = 8
    LUXURYTAX = 9
    
class ColorGroup(Enum):
    PURPLE = 1
    LIGHTBLUE = 2
    PINK = 3
    ORANGE = 4
    RED = 5
    YELLOW = 6
    GREEN = 7
    DARKBLUE = 8
    UTILITY = 9
    RAILROAD = 10

class Space:
    def __init__(self, name: str, spaceType: SpaceType):
        self.spaceType = spaceType

class Property(Space):
    def __init__(self, name: str, price: int, colorgroup: ColorGroup, improvementCost: int, rentList: [], mortgagevalue: int):
        Space.__init__(self, name, SpaceType.PROPERTY)
        self.name = Space.name
        self.price = price
        self.colorgroup = colorgroup
        self.improvementCost = improvementCost
        self.rentList = rentList
        self.improvementLevel = 0
        self.mortgaged = False
        self.mortgagevalue = mortgagevalue
    
    def getCurrentRent(self):
        return self.rentList[self.improvementLevel] #TODO: Account for unimproved properties where all the color group is owned (double value)
    
    def improve(self):
        self.improvementLevel += 1
    
    def mortgage(self):
        self.mortgaged = True
    
    def unmortgage(self):
        self.mortgaged = False

class Railroad(Property):
    def __init__(self, name: str, price: int, mortgagevalue: int):
        Property.__init__(self, name, price, ColorGroup.RAILROAD, 0, [price], mortgagevalue)
    
    def improve(self):
        return TypeError('Railroads cannot be improved')

class Utility(Property):
    def __init__(self, name: str, price: int, mortgagevalue: int):
        Property.__init__(self, name, price, ColorGroup.UTILITY, 0, [price], mortgagevalue)
        
    def improve(self):
        return TypeError('Utilities cannot be improved')
    
'''TODO:
    -Add the rest of Space Types
    -Board Display
    -Moving/Get Spaces for some other file
    -Chance/Community Chest Cards Data Entry
    -Property Cards Data Entry
'''