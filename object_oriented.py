# Title: Data cleaning and analysis script
# Name: Yusra Hassan
# Last Updated: March 13th, 2025
# Description: Try to find some insights on hockey teams and present with additional information

import pandas as pd
from team import Team
from season import Season
from stats import Stats

NHL = pd.read_csv("NHL.csv")
win_loss = pd.read_csv("team_wins_losses.csv")
win_loss["Team Name"] = win_loss["Team Name"].str.capitalize()

team_info = NHL.filter(regex = '^((?!link).)*$', axis = 1) # don't select columns with the word "link" in them

# Checked individual columns and found issue with montreal. Handle, then merge.
team_info.loc[:, "name"] = team_info["name"].str.capitalize().replace('Montréal', 'Montreal', regex=True)
merged = win_loss.merge(team_info, how = "inner", left_on = "Team Name", right_on = "name")
merged.to_csv("hockey_team_data.csv")

# Create team objects
teams = {}
for row in range(len(team_info)):
    teams[team_info.loc[row, "name"]] = (Team(team_info.loc[row, "name"],
                           team_info.loc[row, "abbreviation"],
                           team_info.loc[row, "officialSiteUrl"],
                           team_info.loc[row, "firstYearOfPlay"]))

# Add season data to each team that we have info on
for row in range(len(merged)): # since we're working with merged data here, we shouldn't need to worry about stuff not in teams, but some teams may not have season data
    teams[merged.loc[row, "Team Name"]].add_data(Season(merged.loc[row, "Year"],
                                                    merged.loc[row, "Wins"],
                                                    merged.loc[row, "Losses"],
                                                    merged.loc[row, "Win %"],
                                                    merged.loc[row, "+ / -"]))

# How did each team do in their first season?
for i in teams:
    if len(teams[i].data) > 0:
        print(f"{i}'s results are {teams[i].data[0]}")