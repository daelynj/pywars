import json

class Account:
    def __init__(self, json):
        self.id = json['id']
        self.age = json['age']
        self.name = json['name']
        self.world = json['world']
        self.guild_IDS = json['guilds']
        self.guild_leaders = json['guild_leader']
        self.created = json['created']
        self.access_array = json['access']
        self.commander = json['commander']
        self.fractal_level = json['fractal_level']
        self.daily_ap = json['daily_ap']
        self.monthly_ap = json['monthly_ap']
        self.wvw_rank = json['wvw_rank']
    
    def __str__(self):
        return "ID: {0}\nAge: {1}\nName: {2}\nWorld: {3}\nGuilds: {4}\nGuild Leaders: {5}\nCreated: {6}\nGuild Access: {7}\nCommander: {8}\nFractal Level: {9}\nDaily AP: {10}\nMonthly AP: {11}\nWvW Rank: {12}".format(
                                                                                                                                                                                self.id, self.age, self.name, self.world, 
                                                                                                                                                                                self.guild_IDS, self.guild_leaders, self.created, 
                                                                                                                                                                                self.access_array, self.commander, self.fractal_level,
                                                                                                                                                                                self.daily_ap, self.monthly_ap, self.wvw_rank)

class Achievements:
    def __init__(self, json):
        pass                               #need to do something about the massive list of achievements that gets delivered, perhaps making a list of Achievements objects
    def __str__(self):
        pass

class Bank:
    def __init__(self, json):
        pass                               #similar to Achievements, need to do something about the massive list of items that gets delivered
    def __str__(self):
        pass

class Dungeons:
    def __init__(self, json):
        pass
    def __str__(self):
        pass




class Guild:
    def __init__(self, json):
        self.level = json['level']
        self.motd = json['motd']
        self.influence = json['influence']
        self.aetherium = json['aetherium']
        self.resonance = json['resonance']
        self.favor = json['favor']
        self.id = json['id']
        self.name = json['name']
        self.tag = json['tag']
        #self.emblem

    def __str__(self):
        return "Level: {0}\nMotto: {1}\Influence: {2}\nAetherium: {3}\nResonance: {4}\nFavor: {5}\nID: {6}\nName: {7}\nTag: {8}".format(self.level, self.motd, self.influence, 
                                                                                                                                        self.aetherium, self.resonance, self.favor,
                                                                                                                                        self.id, self.name, self.tag)