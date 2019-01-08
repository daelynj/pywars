import api_requests as API
import api_models
import json

#this is the client
#you generate a client, holds authorization like api_key..

GUILDWARS2_URL = 'https://api.guildwars2.com/v2'

class Pywars(API.API_Requests):

    def __init__(self, api_key):
        super().__init__(api_key, GUILDWARS2_URL)
    
    def get_achievements(self, ids=None):
        achievements = []

        if ids == None:
            response = self._get_request('/achievements')               #if no ID's are provided, a list of all ids is returned
        else:
            formatted_ids = ''
            for id in ids:
                if (id is not ids[-1]):
                    formatted_ids += str(id) + ","                  #this if/else statement is only done so that the ids are formatted in such a way that a comma is not appended to the end of the last element
                else:                                               #so [1, 5, 10] doesn't get formatted as 1,5,10, instead getting formatted as 1,5,10
                    formatted_ids += str(id)
            response = self._get_request('/achievements?ids=' + formatted_ids)

        if response is not None:
            if ids == None:
                return response
            for achievement in response:
                achievements.append(api_models.Achievements(achievement))
            return achievements
        else:
            return None

    def get_daily_achievements(self):
        daily_achievements = []
        response = self._get_request('/achievements/daily')

        if response is not None:
            for achievement_type in response:
                daily_achievements.append(achievement_type + ":")
                for achievement in response[achievement_type]:
                    daily_achievements.append(api_models.Daily_Achievements(achievement))
            return daily_achievements
        else:
            return None

    def get_tmrw_daily_achievements(self):
        tmrw_daily_achievements = []
        response = self._get_request('/achievements/daily/tomorrow')

        if response is not None:
            for achievement_type in response:
                tmrw_daily_achievements.append(achievement_type + ":")
                for achievement in response[achievement_type]:
                    tmrw_daily_achievements.append(api_models.Tmrw_Daily_Achievements(achievement))
            return tmrw_daily_achievements
        else:
            return None

    def get_group_achievements(self, ids=None):
        group_achievements = []

        if ids == None:
            response = self._get_request('/achievements/groups/') 
        elif len(ids) == 1:
            response = self._get_request('/achievements/groups/' + ids[0])
        else:
            formatted_ids = ''
            for id in ids:
                if (id is not ids[-1]):
                    formatted_ids += str(id) + ","
                else:
                    formatted_ids += str(id)
            response = self._get_request('/achievements/groups?ids=' + formatted_ids)

        if response is not None:
            if ids == None:
                return response
            elif len(ids) == 1:
                return api_models.Group_Achievements(response)
            else:
                for achievement in response:
                    group_achievements.append(api_models.Group_Achievements(achievement))
                return group_achievements
        else:
            return None

    def get_achievements_categories(self, ids=None):
        achievements_categories = []
        if ids == None:
            response = self._get_request('/achievements/categories/') 
        elif len(ids) == 1:
            response = self._get_request('/achievements/categories/' + ids[0])
        else:
            formatted_ids = ''
            for id in ids:
                if (id is not ids[-1]):
                    formatted_ids += str(id) + ","
                else:
                    formatted_ids += str(id)
            response = self._get_request('/achievements/categories?ids=' + formatted_ids)

        if response is not None:
            if ids == None:
                return response
            elif len(ids) == 1:
                return api_models.Achievements_Categories(response)
            else:
                for achievement in response:
                    achievements_categories.append(api_models.Achievements_Categories(achievement))
                return achievements_categories
        else:
            return None        

    def get_account_info(self):                                 #TODO: the world variable in response is resolvable against /v2/worlds
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

    def get_account_bank(self):                                 #TODO: the skin variable in response is resolvable against /v2/skins 
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

    def get_account_dungeons_since_reset(self):                 #TODO: this is resolvable against /v2/dungeons
        response = self._get_request('/account/dungeons')

        if response is not None:
            return api_models.Dungeons_Since_Reset(response)
        else:
            return None

    def get_account_dyes(self):                                 #TODO: this is resolvable against /v2/colors
        response = self._get_request('/account/dyes')

        if response is not None:
            return api_models.Account_Dyes(response)
        else:
            return None

    def get_account_finishers(self):                            #TODO: this is resolvable against /v2/finishers
        account_finishers = []
        response = self._get_request('/account/finishers')

        if response is not None:
            for finisher in response:
                account_finishers.append(api_models.Account_Finishers(finisher))
            return account_finishers
        else:
            return None

    def get_account_gliders(self):                              #TODO: this is resolvable against /v2/gliders
        response = self._get_request('/account/gliders')

        if response is not None:
            return api_models.Account_Gliders(response)
        else:
            return None

    def get_account_cats(self):                                 #TODO: ID in response is resolvable against /v2/cats
        account_cats = []
        response = self._get_request('/account/home/cats')

        if response is not None:
            for cat in response:
                account_cats.append(api_models.Account_Cats(cat))
            return account_cats
        else:
            return None

    def get_account_nodes(self):                                #TODO: Each string in response is resolvable against /v2/nodes
        response = self._get_request('/account/home/nodes')

        if response is not None:
            return api_models.Account_Nodes(response)
        else:
            return None

    def get_account_inventory(self):
        account_inventory = []
        response = self._get_request('/account/inventory')

        if response is not None:
            for item in response:
                account_inventory.append(api_models.Account_Inventory(item))
            return account_inventory
        else:
            return None

    def get_account_mailcarriers(self):                         #TODO: can be resolved against /v2/mailcarriers
        response = self._get_request('/account/mailcarriers')

        if response is not None:
            return api_models.Account_Mailcarriers(response)
        else:
            return None

    def get_guild_details(self, guild_ID):
        response = self._get_request('/guild/{0}'.format(guild_ID))

        if response is not None:
            return api_models.Guild(response)
        else:
            return None