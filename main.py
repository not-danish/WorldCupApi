import requests
import json

#enter endpoint here
endpoint = "players/31000"
#enter parameters here
parameters = {}

#The base url is the url of the api which will return the specified requested data
token = "uaHKOLCbUA35mY7wLI97jgXsmaS0xDohDasg0OwQ26Cfo29xJ3PtYmj9NbVK"
base_url = f"https://soccer.sportmonks.com/api/v2.0/{endpoint}?api_token={token}"

#Adds all the parameters into the base url
if len(parameters) != 0:
  for key in parameters:
    base_url = base_url + f"&{key}={parameters[key]}"

#requests the data and converts the json to a python dictionary
data = json.loads(requests.get(base_url).text)


print(data)
