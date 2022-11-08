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

#gets all of the top scorers for the 2018 world cup
#topscorers = worldcup.topscorers(892)
#print(topscorers)
#worldcup.datatocsv(topscorers, "scorers.csv")

#topassist = worldcup.topassist(892)
#worldcup.datatocsv(topassist, "assists.csv")

#england_goals = worldcup.teamgoals('England',892)
#worldcup.datatocsv(england_goals, "england_goals.csv")

worldcup.getseason_id(2018)
