import pywars

#https://wiki.guildwars2.com/wiki/API:Main

def main():
    api_key = '106CFA85-D732-4441-9916-DAC84D48B1C893FBF40E-3078-4AF2-91F7-54ABE7721755'

    client = pywars.Pywars(api_key)

    account = client.get_account_info()

    guild = client.get_guild_name(account.guild_IDS[0])
    
    achievements = client.get_account_achievements()

   """ if (account is None):
        print("error")
    else:
        print(str(guild))"""
        

if __name__ == "__main__":
    main()