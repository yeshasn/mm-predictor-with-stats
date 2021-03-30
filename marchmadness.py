# -*- coding: utf-8 -*-
#!pip install sportsreference
from sportsreference.ncaab.teams import Teams

'''
for team in Teams():
  print(team.abbreviation, team.games_played)
  '''

def find_teams():
  a = str(input("Enter worse seed team: "))
  b = str(input("Enter better seed team: "))

  for team in Teams():
    if team.abbreviation == a:
      team_one = team
    if team.abbreviation == b:
      team_two = team

  return team_one, team_two

import pandas as pd
import math

def initialize_df():
  team1, team2 = find_teams()
  df = team1.dataframe
  df2 = team2.dataframe
  df = df.append(df2, ignore_index = True)
  return df

def get_games(df):
  g1 = df.iloc[0]["games_played"]
  g2 = df.iloc[1]["games_played"]
  return g1, g2

def compare():
  df = initialize_df()
  score1 = 0
  score2 = 0
  one = []
  two = []
  n1 = df.iloc[0]["name"]
  n2 = df.iloc[1]["name"]
  g1, g2 = get_games(df)

  four_pts = "effective_field_goal_percentage"
  if df.iloc[0][four_pts] > df.iloc[1][four_pts]:
    score1 += 4
    one.append(four_pts)
  else:
    score2 += 4
    two.append(four_pts)

  three_pt_per = ["free_throw_percentage", "offensive_rating", "pace"]
  for thpp in three_pt_per:
    if df.iloc[0][thpp] > df.iloc[1][thpp]:
      score1 += 3
      one.append(thpp)
    else:
      score2 += 3
      two.append(thpp)

  three_pt_reg = ["field_goal_attempts", "free_throw_attempts"]
  for thpr in three_pt_reg:
    if df.iloc[0][thpr] > df.iloc[1][thpr]:
      score1 += 3
      one.append(thpr)
    else:
      score2 += 3
      two.append(thpr)

  two_pt_percentages = ["true_shooting_percentage", "win_percentage"]
  for tpp in two_pt_percentages:
    if df.iloc[0][tpp] > df.iloc[1][tpp]:
      score1 += 2
      one.append(tpp)
    else:
      score2 += 2
      two.append(tpp)

  two_pt_regular = ["total_rebounds", "points"]
  for tpr in two_pt_regular:
    if (df.iloc[0][tpr]/g1) > (df.iloc[1][tpr]/g2):
      score1 += 2
      one.append(tpr)
    else:
      score2 += 2
      two.append(tpr)
  
  two_pt_inverted = ["turnovers", "personal_fouls", "opp_points"]
  for tpi in two_pt_inverted:
    if (df.iloc[0][tpi]/g1) < (df.iloc[1][tpi]/g2):
      score1 += 1
      one.append(tpi)
    else:
      score2 += 1
      two.append(tpi)

  one_pt = ["assists", "blocks", "steals"]
  for o in one_pt:
    if (df.iloc[0][o]/g1) > (df.iloc[1][o]/g2):
      score1 += 1
      one.append(o)
    else:
      score2 += 1
      two.append(o)

  if df.iloc[0]["strength_of_schedule"] > df.iloc[1]["strength_of_schedule"]:
    score1 += 2
    one.append("harder_schedule")
  else:
    score2 += 2
    two.append("harder_schedule")


  return n1, score1, one, n2, score2, two, df

def easier_schedule(name1, name2, df):
  s1 = df.iloc[0]["strength_of_schedule"]
  s2 = df.iloc[1]["strength_of_schedule"]
  if s1 < s2:
    print(name1, "had easier schedule >>> ", s1, "vs", s2)
  else:
    print(name2, "had easier schedule >>> ", s2, "vs", s1)

name1, score1, one, name2, score2, two, df = compare()
print(name1, ":", score1)
print("   statistically better in:", one)
print(name2, ":", score2)
print("   statistically better in:", two)

if score1 - score2 == 0:
  easier_schedule(name1, name2, df)

