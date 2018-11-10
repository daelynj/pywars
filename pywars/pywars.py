import API_Requests as API
import API_Models

#this is the client
#you generate a client, holds authorization like api_key..

GUILDWARS2_URL = 'https://api.guildwars2.com/v2/'

class Pywars(API.API_Requests):

    def __init__(self, api_key): # constructor
        super().__init__(api_key, GUILDWARS2_URL)
    
    def get_account_info(self):
        response = self._get_request('/account')

        if response is not None:
            return API_Models.Account(response)
        else:
            return None