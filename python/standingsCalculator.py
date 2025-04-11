# The intent of this calculator is to have a custom built solution for Capitol Alumni Network's sports standing page(s).  At this time their standings page
# does not take into account division standings, leading to a tedious process of manually keeping track of these games.  This calculator, in conjunction with
# the eventual front-end page, will ease that burden.  This feature will be integrated into a future version of that website.

class StandingsCalculator(object):
    wins = 0
    losses = 0
    divisionWins = 0
    divisionLosses = 0

    def __init__(self, name):
        self.name = name

    def winningPercentage(self, wins=0, losses=0):
        self.wins = wins
        self.losses = losses
        totalGames = wins + losses
        if totalGames == 0:
            return 0.0
        winningPercentage = round((wins / totalGames), 3)
        return winningPercentage
    
    def divisionWinningPercentage(self, divisionWins=0, divisionLosses=0):
        self.divisionWins = divisionWins
        self.divisionLosses = divisionLosses
        totalDivisionGames = divisionWins + divisionLosses
        if totalDivisionGames == 0:
            return 0.0
        winningPercentage = round((divisionWins / totalDivisionGames), 3)
        return winningPercentage
        
standingsCalculator = StandingsCalculator("Test")
    
print(standingsCalculator.winningPercentage(14, 3))
print(standingsCalculator.divisionWinningPercentage(5, 3))