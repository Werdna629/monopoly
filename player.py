from board import Property

class FundsError(Exception):
    print('Insufficient Funds')

class Player:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.money = 1500
        self.token = name[0].upper()
        self.properties = {}
    
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