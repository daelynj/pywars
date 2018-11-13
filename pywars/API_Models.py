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
        self.id = json['id']
        self.current = json['current']
        self.max = json['max']
        self.done = json['done']

        if 'bits' in json:
            self.bits = json['bits']
        else:
            self.bits = None
        if 'repeated' in json:
            if (json['repeated'] == 1):
                self.repeated = json['repeated']
                self.repeated = str(self.repeated) + " time"
            else:
                self.repeated = json['repeated']
                self.repeated = str(self.repeated) + " times"
        else: self.repeated = "Never repeated"
        if 'unlocked' in json:
            if (json['unlocked'] == True):
                self.unlocked = "Yes"
            else:
                self.unlocked = "No"
        else:
            self.unlocked = "Not applicable"         #is it possible to have progress in a locked achievement? I don't understand Arena Net saying this: 
                                                     #Shows whether or not the achievement is unlocked. Note that if this property does not exist, the achievement is unlocked as well.
                                                     #so if it's unlocked, unlocked = True, and if it's not there, unlocked = True
                                                     #but you can't have progress in a locked achievement, and this API call does not return locked achievements (ie. achievements with no progress)
                                                     #so unlocked might as well always be set to Yes

    def __str__(self):
        return "ID: {0}\nCurrent: {1}\nMax: {2}\nDone: {3}\nBits: {4}\nRepeated: {5}\nUnlocked: {6}".format(self.id, self.current, self.max, self.done, self.bits, self.repeated, self.unlocked)

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