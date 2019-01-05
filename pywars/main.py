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

   account_finishers = client.get_account_finishers()
   for i in range(0, len(account_finishers)):
      print(str(account_finishers[i]), "\n")

if __name__ == "__main__":
    main()