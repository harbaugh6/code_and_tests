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

    def winningPercentage(self, wins, losses):
        self.wins = wins
        self.losses = losses
        return (round((wins / (wins + losses)), 3))
    
    def divisionWinningPercentage(self, divisionWins, divisionLosses):
        self.divisionWins = divisionWins
        self.divisionLosses = divisionLosses
        return (round((divisionWins / (divisionWins + divisionLosses)), 3))
    
standingsCalculator = StandingsCalculator("Test")
    
print(standingsCalculator.winningPercentage(14, 3))
print(standingsCalculator.divisionWinningPercentage(5, 1))