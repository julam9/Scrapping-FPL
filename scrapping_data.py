import requests, json
from pprint import pprint 
import pandas as pd

base_url = "https://fantasy.premierleague.com/api/"
r = requests.get(base_url+"bootstrap-static/").json()
pprint(r, indent=2, depth=5, compact=False)