import requests
import json


def getapiurl(endpoint: str,parameters: dict) -> str:
  
  #The base url is the url of the api which will return the specified requested data
  token = "uaHKOLCbUA35mY7wLI97jgXsmaS0xDohDasg0OwQ26Cfo29xJ3PtYmj9NbVK"
  base_url = f"https://soccer.sportmonks.com/api/v2.0/{endpoint}?api_token={token}"
  
  #Adds all the parameters into the base url
  if len(parameters) != 0:
    for key in parameters:
      base_url = base_url + f"&{key}={parameters[key]}"
  return base_url

def datatodict(url: "str") -> dict:
  #sends an HTTP request, retrives the data and converts it into a dict
  return json.loads(requests.get(url).text)

def matchgoals(fixture_id: int) -> dict:
  #gets all of the goals scored in a specific fixture
  url = getapiurl(f"fixtures/{fixture_id}",{"include":"goals"})
  data = datatodict(url)
  return data
  
def teamgoals(team_id: int, season_id: int) -> dict:
  #gets all the goals scored by all the players in a specified team (team_id) in a specified year (season_id)
  url = getapiurl(f"teams/{team_id}",{"include":"goalscorers","seasons":season_id})
  data = datatodict(url)
  return data['data']['goalscorers']['data'][0]

def player(player_id: int) -> dict:
  #gets info on players based on player_id
  url = getapiurl(f"players/{player_id}", {})
  data = datatodict(url)
  return data['data']

def topscorers(season_id: int) -> dict:
  #gets all of the top scorers for the world cup
  url = getapiurl(f"topscorers/season/{season_id}",{"include":"goalscorers.player.team"})
  data = datatodict(url)
  return data['data']