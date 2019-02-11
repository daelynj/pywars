import json

class Achievements:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.description = json['description']
        self.requirement = json['requirement']
        self.locked_text = json['locked_text']
        self.type = json['type']
        self.flags = json['flags']
        self.tiers = json['tiers']
        if 'icon' in json:
            self.icon = json['icon']
        else:
            self.icon = None
        if 'prerequisites' in json:
            self.preqrequisites = json['prerequisites']
        else:
            self.preqrequisites = None
        if 'rewards' in json:
            self.rewards = json['rewards']
        else:
            self.rewards = None
        if 'bits' in json:
            self.bits = json['bits']
        else:
            self.bits = None
        if 'point_cap' in json:
            self.point_cap = json['point_cap']
        else:
            self.point_cap = None

    def __str__(self):
        return "ID: {0}\nIcon: {1}\nName: {2}\Description: {3}\nRequirement: {4}\nLocked_text: {5}\nType: {6}\nFlags: {7}\nTiers: {8}\nPrerequisites: {9}\nRewards: {10}\nBits: {11}\nPoint_cap: {12}".format(
                                                                                                                                                                                        self.id, self.icon, self.name, self.description,
                                                                                                                                                                                        self.requirement, self.locked_text, self.type,
                                                                                                                                                                                        self.flags, self.tiers, self.preqrequisites,
                                                                                                                                                                                        self.rewards, self.bits, self.point_cap)
