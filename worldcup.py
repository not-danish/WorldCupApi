#This script was created by Danish Siddiqui for MTA's Python Event.
from typing import List, Dict
import requests
import json
import csv

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
  
def teamgoals(team_id: int, season_id: int) -> List[Dict]:
  #gets all the goals scored by all the players in a specified team (team_id) in a specified year (season_id)
  url = getapiurl(f"teams/{team_id}",{"include":"goalscorers","seasons":season_id})
  data = datatodict(url)
  return data['data']['goalscorers']['data']

def player(player_id: int) -> List[Dict]:
  #gets info on players based on player_id
  url = getapiurl(f"players/{player_id}", {})
  data = datatodict(url)
  if 'meta' in data:
    data.pop('meta')
  else:
    data = {}
  return data

def topscorers(season_id: int) -> dict:
  #gets top 25 scorers for the world cup season (season_id)
  url = getapiurl(f"topscorers/season/{season_id}",{"include":"goalscorers.player.team"})
  data = datatodict(url)
  return data['data']['goalscorers']['data']

def topassist(season_id: int) -> dict:
  #gets top 25 assisters for the world cup season (season_id)
  url = getapiurl(f"topscorers/season/{season_id}",{"include":"goalscorers.player.team"})
  data = datatodict(url)
  return data['data']

def fields(data: dict) -> list:
  #gets all of the fields for a specific dict
  fields = []
  for key in data[0]:
    fields.append(key)
  return fields

def datatocsv(data: list, filename: str) -> None:
  #converts the dict data to a csv with name filename
  columns = fields(data)
  try:
      with open(filename, 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=columns)
          writer.writeheader()  
          writer.writerows(data)
  except IOError:
      print("I/O error")
  
