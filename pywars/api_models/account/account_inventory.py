import json

class Account_Inventory:
    def __init__(self, json):
        self.id = json['id']
        self.count = json['count']

        if 'charges' in json:
            self.charges = json['charges']
        else:
            self.charges = None
        if 'skin' in json:
            self.skin = json['skin']
        else:
            self.skin = None
        if 'upgrades' in json:
            self.upgrades = json['upgrades']
        else:
            self.upgrades = None
        if 'infusions' in json:
            self.infusions = json['infusions']
        else:
            self.infusions = None
        if 'binding' in json:
            self.binding = json['binding']
        else:
            self.binding = None
    
    def __str__(self):
        return "ID: {0}\nCount: {1}\nCharges: {2}\nSkin: {3}\nUpgrades: {4}\nInfusions: {5}\nBinding: {6}".format(self.id, self.count, self.charges, self.skin, self.upgrades, self.infusions, self.binding)