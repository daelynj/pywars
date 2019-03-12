import json

class Account_Mailcarriers:
    def __init__(self, json):
        self.mailcarriers = json
    
    def __str__(self):
        return "Mailcarriers: {0}".format(self.mailcarriers)