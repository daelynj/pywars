import API_Requests as API
import API_Models
import json

#this is the client
#you generate a client, holds authorization like api_key..

GUILDWARS2_URL = 'https://api.guildwars2.com/v2/'

class Pywars(API.API_Requests):

    def __init__(self, api_key):
        super().__init__(api_key, GUILDWARS2_URL)
    
    def get_account_info(self):
        response = self._get_request('/account')

        if response is not None:
            return API_Models.Account(response)
        else:
            return None

    def get_account_achievements(self):
        achievements = []
        response = self._get_request('/account/achievements')

        if response is not None:
            for achievement in response:
                achievements.append(API_Models.Achievements(achievement))
            return achievements
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
                    bank_items.append(API_Models.Bank(item))
            return bank_items
        else:
            return None

    def get_account_dungeons_since_reset(self):
        response = self._get_request('/account/dungeons')

        if response is not None:
            return API_Models.Dungeons_since_reset(response)
        else:
            return None

    
    def get_guild_name(self, guild_ID):
        response = self._get_request('/guild/{0}'.format(guild_ID))

        if response is not None:
            return API_Models.Guild(response)
        else:
            return None