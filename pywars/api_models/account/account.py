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
        return "ID: {0}\nAge: {1}\nName: {2}\nWorld: {3}\nGuilds: {4}\nLeader(s) of: {5}\nCreated: {6}\nAccess: {7}\nCommander: {8}\nFractal Level: {9}\nDaily AP: {10}\nMonthly AP: {11}\nWvW Rank: {12}".format(
                                                                                                                                                                                self.id, self.age, self.name, self.world, 
                                                                                                                                                                                self.guild_IDS, self.guild_leaders, self.created, 
                                                                                                                                                                                self.access_array, self.commander, self.fractal_level,
                                                                                                                                                                                self.daily_ap, self.monthly_ap, self.wvw_rank)