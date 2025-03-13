# Title: Team class
# Name: Yusra Hassan
# Last Updated: March 13th, 2025
# Description: Team objects include infromation about each team, including a list of season data

from season import Season
class Team:
    def __init__(self, name, abbrv, url, first_year):
        self.name = name
        self.abbrv = abbrv
        self.url = url
        self.first_year = first_year
        self.data = []

    # Add in a season-type object
    def add_data(self, season):
        self.data.append(season)
    
    def get_data(self):
        return ';\n'.join(list(map(Season.__str__, self.data)))

    def __str__(self):
        return f"{self.name} ({self.abbrv}): {self.url}"