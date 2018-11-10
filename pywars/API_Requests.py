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

        if response.status_code == 200:                                      #can add error checking in another file later on
            return json.loads(response.content.decode('utf-8'))
        else:
            return None
    
    def _put_request():
        pass

    def _post_request():
        pass