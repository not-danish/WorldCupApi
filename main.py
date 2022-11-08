import worldcup

#the season_id for the 2018 world cup is 892

#gets all the players who scored goals for a specific team (team_id) for a specific year (season_id)
#goals = worldcup.teamgoals(18647,892)
#print(goals)
#worldcup.datatocsv(goals,"goals.csv")

print("----------------------------------------")
print("----------------------------------------")

#get information on a specific player based on their player_id

print("----------------------------------------")
print("----------------------------------------")

englandgoals = worldcup.teamgoals("England", 2006)
print(englandgoals)