import worldcup

englandgoals = worldcup.teamgoals("England", 2006)

spain_squad = worldcup.squad('Spain', 2014)
worldcup.datatocsv(spain_squad, "spain_squad.csv")

worldcup.datatocsv(worldcup.results(2018),"results.csv")
