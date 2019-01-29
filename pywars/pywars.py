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
                daily_achievements.append(achievement_type + ":")                           #should I be doing this? adding things to the list that aren't part of the response?
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
                tmrw_daily_achievements.append(achievement_type + ":")                      #should I be doing this? adding things to the list that aren't part of the response?
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
            return api_models.Dungeons_Since_Reset(response)
        else:
            return None

    def get_account_dyes(self):
        response = self._get_request('/account/dyes')

        if response is not None:
            return api_models.Account_Dyes(response)
        else:
            return None

    def get_account_finishers(self):
        account_finishers = []
        response = self._get_request('/account/finishers')

        if response is not None:
            for finisher in response:
                account_finishers.append(api_models.Account_Finishers(finisher))
            return account_finishers
        else:
            return None

    def get_account_gliders(self):
        response = self._get_request('/account/gliders')

        if response is not None:
            return api_models.Account_Gliders(response)
        else:
            return None

    def get_account_cats(self):
        account_cats = []
        response = self._get_request('/account/home/cats')

        if response is not None:
            for cat in response:
                account_cats.append(api_models.Account_Cats(cat))
            return account_cats
        else:
            return None

    def get_account_nodes(self):
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

    def get_account_mailcarriers(self):
        response = self._get_request('/account/mailcarriers')

        if response is not None:
            return api_models.Account_Mailcarriers(response)
        else:
            return None

    """def get_account_masteries(self):                         #This is currently bugged, receiving an Error 400 (bad request error), I'm not sure why, the URL and Headers are just fine
        account_masteries = []                                  #The ID in response is resolvable against /v2/masteries
        response = self._get_request('/account/masteries')

        if response is not None:
            for mastery in response:
                account_masteries.append(api_models.Account_Masteries(mastery))
            return account_masteries
        else:
            return None"""

    def get_account_mastery_points(self):
        response = self._get_request('/account/mastery/points')

        if response is not None:
            return api_models.Account_Mastery_Points(response)
        else:
            return None

    def get_account_materials(self):
        account_materials = []
        response = self._get_request('/account/materials')

        if response is not None:
            for material in response:
                account_materials.append(api_models.Account_Materials(material))
            return account_materials
        else:
            return None

    def get_account_minis(self):
        response = self._get_request('/account/minis')

        if response is not None:
            return api_models.Account_Minis(response)
        else:
            return None        

    def get_account_mounts_skins(self):
        response = self._get_request('/account/mounts/skins')

        if response is not None:
            return api_models.Account_Mounts_Skins(response)
        else:
            return None

    def get_account_mount_types(self):
        response = self._get_request('/account/mounts/types')

        if response is not None:
            return api_models.Account_Mount_Types(response)
        else:
            return None

    def get_account_outfits(self):
        response = self._get_request('/account/outfits')

        if response is not None:
            return api_models.Account_Outfits(response)
        else:
            return None

    def get_account_pvp_heroes(self):
        response = self._get_request('/account/pvp/heroes')

        if response is not None:
            return api_models.Account_Pvp_Heroes(response)
        else:
            return None

    def get_account_raids(self):
        response = self._get_request('/account/raids')
        
        if response is not None:
            return api_models.Account_Raids(response)
        else:
            return None

    def get_account_recipes(self):
        response = self._get_request('/account/recipes')

        if response is not None:
            return api_models.Account_Recipes(response)
        else:
            return None

    def get_account_skins(self):
        response = self._get_request('/account/skins')

        if response is not None:
            return api_models.Account_Skins(response)
        else:
            return None    

    def get_account_titles(self):
        response = self._get_request('/account/titles')

        if response is not None:
            return api_models.Account_Titles(response)
        else:
            return None

    def get_account_wallet(self):
        account_wallet = []
        response = self._get_request('/account/wallet')

        if response is not None:
            for currency in response:
                account_wallet.append(api_models.Account_Wallet(currency))
            return account_wallet
        else:
            return None

    def get_characters(self, params=None):
        if params == None:
            response = self._get_request('/characters')

        if response is not None:
            return api_models.Characters(response)
        else:
            return None

    def get_character_overview(self, character_name):
        response = self._get_request('/characters/' + character_name)

        if response is not None:
            return api_models.Character_Overview(response)
        else:
            return None

    def get_character_backstory(self, character_name):
        response = self._get_request('/characters/' + character_name + '/backstory')

        if response is not None:
            return api_models.Character_Backstory(response)
        else:
            return None

    def get_character_core(self, character_name):
        response = self._get_request('/characters/' + character_name + '/core')

        if response is not None:
            return api_models.Character_Core(response)
        else:
            return None

    def get_character_crafting(self, character_name):
        response = self._get_request('/characters/' + character_name + '/crafting')

        if response is not None:
            return api_models.Character_Crafting(response)
        else:
            return None

    def get_character_equipment(self, character_name):
        response = self._get_request('/characters/' + character_name + '/equipment')

        if response is not None:
            return api_models.Character_Equipment(response)
        else:
            return None

    def get_character_heropoints(self, character_name):
        response = self._get_request('/characters/' + character_name + '/heropoints')

        if response is not None:
            return api_models.Character_Heropoints(response)
        else:
            return None

    def get_character_inventory(self, character_name):
        response = self._get_request('/characters/' + character_name + '/inventory')

        if response is not None:
            return api_models.Character_Inventory(response)
        else:
            return None

    def get_character_recipes(self, character_name):
        response = self._get_request('/characters/' + character_name + '/recipes')

        if response is not None:
            return api_models.Character_Recipes(response)
        else:
            return None

    def get_character_Sab(self, character_name):
        response = self._get_request('/characters/' + character_name + '/Sab')

        if response is not None:
            return api_models.Character_Sab(response)
        else:
            return None

    def get_character_skills(self, character_name):
        response = self._get_request('/characters/' + character_name + '/skills')

        if response is not None:
            return api_models.Character_Skills(response)
        else:
            return None

    def get_character_specializations(self, character_name):
        response = self._get_request('/characters/' + character_name + '/specializations')

        if response is not None:
            return api_models.Character_Specializations(response)
        else:
            return None

    def get_character_training(self, character_name):
        response = self._get_request('/characters/' + character_name + '/training')

        if response is not None:
            return api_models.Character_Training(response)
        else:
            return None

    def get_guild_details(self, guild_ID):
        response = self._get_request('/guild/{0}'.format(guild_ID))

        if response is not None:
            return api_models.Guild(response)
        else:
            return None