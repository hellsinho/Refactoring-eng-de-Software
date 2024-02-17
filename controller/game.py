from view import main

class WarGame:
    def __init__(self, countries):
        self.observers = []
        self.availableTerritory = countries

    def add_observer(self, player):
        self.observers.append(player)

    def notifyWinner(self, winnerName, countriesWon):
        for player in self.observers:
            if player.name == winnerName:
                player.countriesWon.extend(countriesWon)
                main.printNotifyWinner(winnerName, countriesWon)
            else:
                main.printNotifyLoser(player.name, winnerName)

    def getAvailableTerritory(self):
        return self.availableTerritory

class Player:
    def __init__(self, name):
        self.name = name
        self.countriesWon = []
        self.army = 7

    def getName(self):
        return self.name
    
    def getAmoutPlayerArmy(self):
        return self.army

    def subArmy(self, subAmount):
        self.army -= subAmount

class Territory:

    def __init__(self, nameTerritory, player=None):
        self.nameTerritory = nameTerritory
        self.player = player
        self.armyInTerritory = 0

    def addArmy(self, amountArmyAddTerritory, setPlayerTerritory):
        if self.player is None:
            self.armyInTerritory += amountArmyAddTerritory
            self.player = setPlayerTerritory
            main.addSucess(amountArmyAddTerritory)
            self.player.subArmy(amountArmyAddTerritory)
        else:
            main.notAvaibleTerritory()
        

