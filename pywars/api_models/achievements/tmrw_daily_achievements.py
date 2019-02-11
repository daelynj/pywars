import json

class Tmrw_Daily_Achievements:
    def __init__(self, json):
        self.id = json['id']
        self.level = json['level']
        self.required_access = json['required_access']
    
    def __str__(self):
        return "ID: {0}\nLevel: {1}\nRequired_access: {2}".format(self.id, self.level, self.required_access)