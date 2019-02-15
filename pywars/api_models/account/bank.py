import json

class Bank:
    def __init__(self, json):
        self.id = json['id']
        self.count = json['count']

        if 'charges' in json:
            self.charges = json['charges']
        else:
            self.charges = None
        if 'upgrades' in json:
            self.upgrades = json['upgrades']
        else:
            self.upgrades = None
        if 'skin' in json:
            self.skin = json['skin']
        else:
            self.skin = None
        if 'infusions' in json:
            self.infusions = json['infusions']
        else:
            self.infusions = None
        if 'binding' in json:
            self.binding = json['binding']
        else:
            self.binding = None
        if 'bound_to' in json:
            self.bound_to = json['bound_to']
        else:
            self.bound_to = None

    def __str__(self):
        return "ID: {0}\nCount: {1}\nCharges: {2}\nUpgrades: {3}\nSkin: {4}\nInfusions: {5}\nBinding: {6}\nBound to: {7}".format(self.id, self.count, self.charges, self.upgrades, 
                                                                                                                                self.skin, self.infusions, self.binding, self.bound_to)