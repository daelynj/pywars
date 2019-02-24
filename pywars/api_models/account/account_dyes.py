import json

class Account_Dyes:
    def __init__(self, json):
        self.dyes = json

    def __str__(self):
        return "Dyes:\n{0}".format(self.dyes)