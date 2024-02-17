def printNotifyWinner(winner_name, countries_won):
            for country in countries_won:
                print(f"{winner_name} conquistou o país: {country}")
            print(f"{winner_name} venceu a batalha e conquistou os países: {', '.join(countries_won)}")

def printNotifyLoser(loser_name, winner_name):
        print(f"{loser_name} perdeu a batalha para {winner_name}.")

def notAvaibleTerritory():
        print("Operação negada. Este território pertence a outro jogador.")

def addSucess(amount):
        print(f"Os {amount} exércitos adicionados com sucesso ao território")