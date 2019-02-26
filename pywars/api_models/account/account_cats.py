import json

class Account_Cats:
    def __init__(self, json):
        self.id = json['id']

        if 'hint' in json:
            self.hint = json['hint']
        else:
            self.hint = None

    def __str__(self):
        return "ID: {0}\nHint: {1}".format(self.id, self.hint)