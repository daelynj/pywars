import pywars
import json

#https://wiki.guildwars2.com/wiki/API:Main

def main():
   with open('credentials.json') as f:
      api_key = json.load(f)['api-key']

   client = pywars.Pywars(api_key)
   #client2 = pywars.Pywars()                      #TODO, to make a client without an API key

   #account = client.get_account_info()
   #print(account)

   #guild = client.get_guild_details(account.guild_IDS[0])
   #print(guild)

   #dungeons_since_reset = client.get_account_dungeons_since_reset()
   #print(dungeons_since_reset)

   #account_achievements = client.get_account_achievements()
   #print account_achievements
   """
   for i in range(0, len(account_achievements)):
      print(str(account_achievements[i]), "\n")
   """

   #bank = client.get_account_bank()
   #print bank
   """
   for i in range(0, len(bank)):
      print(str(bank[i]), "\n")
   """

   #ids = [1, 5]
   #pass ids into client.get_achievements(ids) to pass the ids for specific achievements
   #achievements = client.get_achievements()
   """for i in range(0, len(achievements)):
      print(str(achievements[i]), "\n")"""

   #daily_achievements = client.get_daily_achievements()
   """for i in range(0, len(daily_achievements)):
      print(str(daily_achievements[i]), "\n")"""

   #tmrw_daily_achievements = client.get_tmrw_daily_achievements()
   """for i in range(0, len(tmrw_daily_achievements)):
      print(str(tmrw_daily_achievements[i]), "\n")"""
   
   #ids = ["56A82BB9-6B07-4AB0-89EE-E4A6D68F5C47"]
   #ids = ["56A82BB9-6B07-4AB0-89EE-E4A6D68F5C47","45410F60-AB66-4146-A0F7-CE99250C4CB0"]
   #group_achievements = client.get_group_achievements()
   #print(group_achievements)
   """for i in range(0, len(group_achievements)):
      print(str(group_achievements[i]), "\n")"""

   #ids = ["1", "2"]
   #achievements_categories = client.get_achievements_categories(ids)
   #print(achievements_categories)
   """for i in range(0, len(achievements_categories)):
      print(str(achievements_categories[i]), "\n")"""

   #account_dyes = client.get_account_dyes()
   #print(account_dyes)

   #account_finishers = client.get_account_finishers()
   """for i in range(0, len(account_finishers)):
      print(str(account_finishers[i]), "\n")"""

   #account_gliders = client.get_account_gliders()
   #print(account_gliders)

   #account_cats = client.get_account_cats()
   """for i in range(0, len(account_cats)):
      print(str(account_cats[i]), "\n")""" 

   #account_nodes = client.get_account_nodes()
   #print(account_nodes)

   #account_inventory = client.get_account_inventory()
   """for i in range(0, len(account_inventory)):
      print(str(account_inventory[i]), "\n")"""

   #account_mailcarriers = client.get_account_mailcarriers()
   #print(account_mailcarriers)

   account_masteries = client.get_account_masteries()
   for i in range(0, len(account_masteries)):
      print(str(account_masteries[i]), "\n")
if __name__ == "__main__":
    main()