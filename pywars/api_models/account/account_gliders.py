import json

class Account_Gliders:
    def __init__(self, json):
        self.gliders = json

    def __str__(self):
        return "Gliders:\n{0}".format(self.gliders)