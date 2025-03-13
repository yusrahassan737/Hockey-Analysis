# Title: Season Class
# Name: Yusra Hassan
# Last Updated: March 13th, 2025
# Description: Objects hold win/loss information for a single season/year

class Season:
    def __init__(self, year, wins, losses, win_pct, goals_ttl):
        self.year = year
        self.wins = wins
        self.losses = losses
        self.win_pct = win_pct
        self.goals_ttl = goals_ttl

    def __str__(self):
        return f"{self.year}: {self.wins} wins, {self.losses} losses, win percentage: {self.win_pct}, goals won - against: {self.goals_ttl}"