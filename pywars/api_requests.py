import json
import requests

class API_Requests:
    def __init__(self, api_key, api_url_base):
        self.api_key = api_key
        self.api_url_base = api_url_base

    def _get_request(self, path):
        url = self.api_url_base + path
        headers = {'Authorization': 'Bearer {0}'.format(self.api_key)}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        elif response.status_code == 404:
            print ("Error 404")
            return None
        elif response.status_code == 400:
            print("Error 400")
            return None
        else:
            return None
    
    def _put_request(self):
        pass

    def _post_request(self):
        pass