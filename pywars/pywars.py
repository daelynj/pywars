import json
import requests

from pywars.API_Requests import API_Requests

#https://wiki.guildwars2.com/wiki/API:Main

#api_key = '106CFA85-D732-4441-9916-DAC84D48B1C893FBF40E-3078-4AF2-91F7-54ABE7721755'

class Pywars:
    
    def __init__(self, api_key):
        self.api_key = api_key

