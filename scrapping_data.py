import requests, json
from pprint import pprint 
import pandas as pd

base_url = "https://fantasy.premierleague.com/api/"
r = requests.get(base_url+"bootstrap-static/").json()
#pprint(r, indent=3, depth=3, compact=False)

# take the player detail info 
players = pd.json_normalize(r["elements"])

# make player df into csv 
players.to_csv("player_data.csv", index=False)