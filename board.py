from enum import Enum
import random

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
        self.name = name
        self.spaceType = spaceType

class Property(Space):
    def __init__(self, name: str, price: int, colorgroup: ColorGroup, improvementCost: int, rentList: []):
        Space.__init__(self, name, SpaceType.PROPERTY)
        self.name = name
        self.price = price
        self.colorgroup = colorgroup
        self.improvementCost = improvementCost
        self.rentList = rentList
        self.improvementLevel = 0
        self.mortgaged = False
        self.mortgagevalue = price/2
    
    def getCurrentRent(self):
        return self.rentList[self.improvementLevel] #TODO: Account for unimproved properties where all the color group is owned (double value)
    
    def improve(self):
        self.improvementLevel += 1
    
    def mortgage(self):
        self.mortgaged = True
    
    def unmortgage(self):
        self.mortgaged = False

class Railroad(Property):
    def __init__(self, name: str):
        Property.__init__(self, name, 200, ColorGroup.RAILROAD, 0, [200])
    
    def improve(self):
        return TypeError('Railroads cannot be improved')

class Utility(Property):
    def __init__(self, name: str):
        Property.__init__(self, name, 150, ColorGroup.UTILITY, 0, [150])
        
    def improve(self):
        return TypeError('Utilities cannot be improved')
    
class Chance(Space):
    def __init__(self):
        Space.__init__(self, "Chance", SpaceType.CHANCE)
        self.cards = []
    
    def shuffle(self):
        random.shuffle(self.cards)
        
class CommunityChest(Space):
    def __init__(self):
        Space.__init__(self, "Community Chest", SpaceType.COMMUNITYCHEST)
        cards = []
        
    def shuffle(self):
        random.shuffle(self.cards)
        
class Go(Space):
    def __init__(self):
        Space.__init__(self, "Go", SpaceType.GO)
        
class Jail(Space):
    def __init__(self):
        Space.__init__(self, "Jail", SpaceType.JAIL)
        
class FreeParking(Space):
    def __init__(self):
        Space.__init__(self, "Free Parking", SpaceType.FREEPARKING)
        
class GoToJail(Space):
    def __init__(self):
        Space.__init__(self, "Go To Jail", SpaceType.GOTOJAIL)
        
class IncomeTax(Space):
    def __init__(self):
        Space.__init__(self, "Income Tax", SpaceType.INCOMETAX)
        
class LuxuryTax(Space):
    def __init__(self):
        Space.__init__(self, "Luxury Tax", SpaceType.LUXURYTAX)
        
        
spaces = [
    Go(),
    Property("Mediterranean Avenue", 60, ColorGroup.PURPLE, 50, [2, 10, 30, 90, 160, 250]),
    Property("Baltic Avenue", 60, ColorGroup.PURPLE, 50, [4, 20, 60, 180, 320, 450]),
    IncomeTax(),
    Railroad("Reading Railroad"),
    Property("Oriental Avenue", 100, ColorGroup.LIGHTBLUE, 50, [6, 30, 90, 270, 400, 550]),
    Chance(),
    Property("Vermont Avenue", 100, ColorGroup.LIGHTBLUE, 50, [6, 30, 90, 270, 400, 550]),
    Property("Connecticut Avenue", 120, ColorGroup.LIGHTBLUE, 50, [8, 40, 100, 300, 450, 600]),
    Jail(),
    Property("St. Charles Place", 140, ColorGroup.PINK, 100, [10, 50, 150, 450, 625, 750]),
    Utility("Electric Company"),
    Property("States Avenue", 140, ColorGroup.PINK, 100, [10, 50, 150, 450, 625, 750]),
    Property("Virginia Avenue", 160, ColorGroup.PINK, 100, [12, 60, 180, 500, 700]),
    Railroad("Pennsylvania Railroad"),
    Property("St. James Place", 180, ColorGroup.ORANGE, 100, [14, 70, 200, 550, 750, 950]),
    CommunityChest(),
    Property("Tennessee Avenue", 180, ColorGroup.ORANGE, 100, [14, 70, 200, 550, 750, 950]),
    Property("New York Avenue", 200, ColorGroup.ORANGE, 100, [16, 80, 220, 600, 800, 1000]),
    FreeParking(),
    Property("Kentucky Avenue", 220, ColorGroup.RED, 150, [18, 90, 250, 700, 875, 1050]),
    Chance(),
    Property("Indiana Avenue", 220, ColorGroup.RED, 150, [18, 90, 250, 700, 875, 1050]),
    Property("Illinois Avenue", 240, ColorGroup.RED, 150, [20, 100, 300, 750, 925, 1100]),
    Railroad("B. & O. Railroad"),
    Property("Atlantic Avenue", 260, ColorGroup.YELLOW, 150, [22, 110, 330, 800, 975, 1150]),
    Property("Ventnor Avenue", 260, ColorGroup.YELLOW, 150, [22, 110, 330, 800, 975, 1150]),
    Utility("Water Works"),
    Property("Marvin Gardens", 280, ColorGroup.YELLOW, 150, [24, 120, 360, 850, 1025, 1200]),
    GoToJail(),
    Property("Pacific Avenue", 300, ColorGroup.GREEN, 200, [26, 130, 390, 900, 1100, 1275]),
    Property("North Carolina Avenue", 300, ColorGroup.GREEN, 200, [26, 130, 390, 900, 1100, 1275]),
    Property("Pennsylvania Avenue", 320, ColorGroup.GREEN, 200, [28, 150, 450, 1000, 1000, 1200, 1400]),
    Railroad("Short Line Railroad"),
    Chance(),
    Property("Park Place", 350, ColorGroup.DARKBLUE, 200, [35, 175, 500, 1100, 1300, 1500]),
    LuxuryTax(),
    Property("Boardwalk", 400, ColorGroup.DARKBLUE, 200, [50, 200, 600, 1400, 1700, 2000]),
    ]
    
'''TODO:
    -Add the rest of Space Types
    -Board Display
    -Moving/Get Spaces for some other file
    -Chance/Community Chest Cards Data Entry
    -Property Cards Data Entry
'''