import pywars
import json

#https://wiki.guildwars2.com/wiki/API:Main

def main():
    with open('credentials.json') as f:
        api_key = json.load(f)['api-key']

    client = pywars.Pywars(api_key)

    account = client.get_account_info()

    guild = client.get_guild_name(account.guild_IDS[0])

    achievements = client.get_account_achievements()
    print(achievements[1])

    """ if (account is None):
        print("error")
    else:
        print(str(guild))"""
        

if __name__ == "__main__":
    main()