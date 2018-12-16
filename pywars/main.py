import pywars
import json

#https://wiki.guildwars2.com/wiki/API:Main

def main():
    with open('credentials.json') as f:
        api_key = json.load(f)['api-key']

    client = pywars.Pywars(api_key)
    #client2 = pywars.Pywars()                      #TODO, to make a client without an API key

    account = client.get_account_info()
    #print(account)

    guild = client.get_guild_name(account.guild_IDS[0])
    #print(guild)

    dungeons_since_reset = client.get_account_dungeons_since_reset()
    #print(dungeons_since_reset)

    account_achievements = client.get_account_achievements()
    #print account_achievements
    """
    for i in range(0, len(account_achievements)):
       print(str(account_achievements[i]), "\n")
    """

    bank = client.get_account_bank()
    #print bank
    """
    for i in range(0, len(bank)):
       print(str(bank[i]), "\n")
    """

    #ids = [1, 5, 10]
    #pass ids into client.get_achievements(ids) to pass the ids for specific achievements
    achievements = client.get_achievements()

if __name__ == "__main__":
    main()