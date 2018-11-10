import json

class Account:
    def __init__(self, json):
        self.id = json['id']
        self.age = json['age']
        self.name = json['name']
        self.world = json['world']
        self.guild_IDs = json['guilds']
        self.guild_leaders = json['guild_leader']
        self.created = json['created']
        self.access_array = json['access']
        self.commander = json['commander']
        self.fractal_level = json['fractal_level']
        self.daily_ap = json['daily_ap']
        self.monthly_ap = json['monthly_ap']
        self.wvw_rank = json['wvw_rank']
    
    def __str__(self):
        return "ID: {0}\nAge: {1}\nName: {2}\nWorld: {3}\nGuild Leader: {4}\nCreated: {5}\nCommander: {6}\nFractal Level: {7}\nDaily AP: {8}\nMonthly AP: {9}\nWvW Rank: {10}".format(self.id, self.age, self.name, self.world, 
                                                                                                                                                                                self.guild_leader, self.created, self.commander, 
                                                                                                                                                                                self.fractal_level, self.daily_ap, self.monthly_ap, 
                                                                                                                                                                                self.wvw_rank)

class Guild:
    def __init__(self, json):
        self.name = json['name']

    def __str__(self):
        return "Guild name: {0}".format(self.name)