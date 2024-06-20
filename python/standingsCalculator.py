class StandingsCalculator(object):
    wins = 0
    losses = 0
    divisionWins = 0
    divisionLosses = 0
    totalGames = 0

    def __init__(self, name):
        self.name = name

    def winningPercentage(self, wins, totalGames):
        self.wins = wins
        self.totalGames = totalGames
        return (float(wins / totalGames))
    
standingsCalculator = StandingsCalculator("Test")
    
print(standingsCalculator.winningPercentage(4, 5))