import unittest
from controller.game import Player, WarGame, Territory

class TestWarGame(unittest.TestCase):
    def setUp(self):
        self.game = WarGame(["Brasil", "Chile", "Peru"])
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")

        self.game.add_observer(self.player1)
        self.game.add_observer(self.player2)

        self.territorio1 = Territory("Território 1", self.player1)
        self.territorio2 = Territory("Território 2")
        

    def testNotifyWinner(self):
        self.game.notifyWinner(self.player2.getName(), self.game.getAvailableTerritory())

    def testGetTerritory(self):
        print(self.game.getAvailableTerritory())

    def testAddArmyPlayerOwner(self):
        self.territorio2.addArmy(5, self.player2)
        self.assertEqual(self.territorio2.armyInTerritory, 5)

    def testAddArmyPlayerNotOwner(self):
        self.territorio1.addArmy(3, self.player1)


if __name__ == "__main__":
    unittest.main()
