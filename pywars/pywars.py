import api_requests as API
import api_models
import json

#this is the client
#you generate a client, holds authorization like api_key..

GUILDWARS2_URL = 'https://api.guildwars2.com/v2/'

class Pywars(API.API_Requests):

    def __init__(self, api_key):
        super().__init__(api_key, GUILDWARS2_URL)
    
    def get_achievements(self, ids=None):
        
        #TODO implement a different API call when ids are passed into get_achievements

        response = self._get_request('/achievements')

        if response is not None:
            return api_models.Achievements(response)
        else:
            return None

    def get_account_info(self):
        response = self._get_request('/account')

        if response is not None:
            return api_models.Account(response)
        else:
            return None

    def get_account_achievements(self):
        account_achievements = []
        response = self._get_request('/account/achievements')

        if response is not None:
            for achievement in response:
                account_achievements.append(api_models.Account_Achievements(achievement))
            return account_achievements
        else:
            return None

    def get_account_bank(self):
        bank_items = []
        response = self._get_request('/account/bank')

        if response is not None:
            for item in response:
                if item == None:
                    bank_items.append("None")
                else:
                    bank_items.append(api_models.Bank(item))
            return bank_items
        else:
            return None

    def get_account_dungeons_since_reset(self):
        response = self._get_request('/account/dungeons')

        if response is not None:
            return api_models.Dungeons_since_reset(response)
        else:
            return None

    
    def get_guild_name(self, guild_ID):
        response = self._get_request('/guild/{0}'.format(guild_ID))

        if response is not None:
            return api_models.Guild(response)
        else:
            return None