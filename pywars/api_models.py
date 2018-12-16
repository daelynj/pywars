import json

class Achievements:
    def __init__(self, json):
        #implement achievements when no ID(s) are passed in (this class likely doesn't need specific implementation for that, but just making sure to remember)
        pass

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

class Account_Achievements:
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
                                                                                                                                
class Dungeons_since_reset:
    def __init__(self, json):
        if len(json) is not 0:
            self.dungeons = "\n".join(json)
        else:
            self.dungeons = None

    def __str__(self):
        if self.dungeons == None:
            return "Dungeons done since reset: {0}".format(self.dungeons)
        else:
            return "Dungeons done since reset:\n{0}".format(self.dungeons)

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
        self.emblem = json['emblem']
        self.emblem_background = json['emblem']['background']                               #everything from here and down in this function is just there for reference if needed, it will all be printed with
        self.emblem_background_id = json['emblem']['background']['id']                      #self.emblem. OR you can print the emblem_background or emblem_foreground, OR the individual keys inside them
        self.emblem_background_colors = json['emblem']['background']['colors']
        self.emblem_foreground = json['emblem']['foreground']
        self.emblem_foreground_id = json['emblem']['foreground']['id']
        self.emblem_foreground_colors = json['emblem']['foreground']['colors']
        self.emblem_flags = json['emblem']['flags']

    def __str__(self):
        return "Level: {0}\nMotto: {1}\nInfluence: {2}\nAetherium: {3}\nResonance: {4}\nFavor: {5}\nID: {6}\nName: {7}\nTag: {8}\nEmblem background: {9}\nEmblem foreground: {10}\nEmblem flags: {11}".format(
                                                                                                                                                                    self.level, self.motd, self.influence, 
                                                                                                                                                                    self.aetherium, self.resonance, self.favor,
                                                                                                                                                                    self.id, self.name, self.tag, self.emblem_background,
                                                                                                                                                                    self.emblem_foreground, self.emblem_flags)