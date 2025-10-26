
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"

class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def displayTeam(self):
        print(f"Team Name: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f"  {player}")

player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

playerList = [player1, player2, player3, player4]

team = NFLTeam("San Francisco 49ers", playerList)

team.displayTeam()
