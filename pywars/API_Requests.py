import json
import requests

import pywars

class API_Requests:
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_request(self, url):
        pass
    
    def get_account_info():







"""
def get_account_info():
    

    headers = {'Authorization': 'Bearer {0}'.format(api_key)}
    api_url = '{0}account'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    if account_info is not None:
        print (account_info['name'])
    else:
        print('[!] Request Failed')

    if account_info is not None:
        for k, v in account_info.items():
            print('{0}:{1}'.format(k, v))

account_info = get_account_info()"""