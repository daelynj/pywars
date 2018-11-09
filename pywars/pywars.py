import json
import requests

api_key = '106CFA85-D732-4441-9916-DAC84D48B1C893FBF40E-3078-4AF2-91F7-54ABE7721755'
api_url_base = 'https://api.guildwars2.com/v2/'

headers = {'Authorization': 'Bearer {0}'.format(api_key)}

def get_account_info():
    api_url = '{0}account'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

account_info = get_account_info()

#if account_info is not None:
#    for k, v in account_info.items():
#        print('{0}:{1}'.format(k, v))

if account_info is not None:
    print (account_info['name'])

else:
    print('[!] Request Failed')