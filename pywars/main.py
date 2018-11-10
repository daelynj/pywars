import pywars

#https://wiki.guildwars2.com/wiki/API:Main

def main():
    api_key = '106CFA85-D732-4441-9916-DAC84D48B1C893FBF40E-3078-4AF2-91F7-54ABE7721755'

    client = pywars.Pywars(api_key)
    account = client.get_account_info()

    if (account is None):
        print("error")
    else:
        print(str(account))

if __name__ == "__main__":
    main()