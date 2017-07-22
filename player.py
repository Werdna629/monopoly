from board import Property, BuyableSpace, ColorGroup

class FundsError(Exception):
    print('Insufficient Funds')

class Player:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.money = 1500
        self.token = name[0].upper()
        self.properties = {}
        
    def getColorGroupLevel(self, cg: ColorGroup):
        level = 0
        for p in self.properties:
            if p.colorgroup == cg:
                level += 1
        return level
        
    def getCompletedColorGroups(self):
        completed = []
        requiredLevels = {ColorGroup.PURPLE: 2, ColorGroup.LIGHTBLUE: 3, ColorGroup.PINK: 3, ColorGroup.ORANGE: 3, ColorGroup.RED: 3, ColorGroup.YELLOW: 3, ColorGroup.GREEN: 3, ColorGroup.DARKBLUE: 2, ColorGroup.RAILROAD: 4, ColorGroup.UTILITY: 2}
        for v in requiredLevels.items():
            if self.getColorGroupLevel(v[0]) == v[1]:
                completed.append(v[0])
        return completed
    
    def buy(self, p: Property):
        if p.price > self.money:
            raise FundsError
        self.money -= p.price
        self.properties.add(p)
        
    def mortgage(self, p: Property):
        p.mortgage()
        self.money += p.mortgagevalue
        
    def unmortgage(self, p: Property):
        p.unmortgage()
        self.money -= p.mortgagevalue*1.1
        
    def payRent(self, p: BuyableSpace):
        rent = p.getCurrentRent() if type(p) == Property else p.getCurrentRent(self.getColorGroupLevel(p.colorgroup))

        if rent > self.money:
            raise FundsError
        self.money -= p.getCurrentRent()
        return rent
    
    def receiveRent(self, amount):
        self.money += amount