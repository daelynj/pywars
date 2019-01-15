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

class Daily_Achievements:
    def __init__(self, json):
        self.id = json['id']
        self.level = json['level']
        self.required_access = json['required_access']

    def __str__(self):
        return "ID: {0}\nLevel: {1}\nRequired_access: {2}".format(self.id, self.level, self.required_access)

class Tmrw_Daily_Achievements:
    def __init__(self, json):
        self.id = json['id']
        self.level = json['level']
        self.required_access = json['required_access']
    
    def __str__(self):
        return "ID: {0}\nLevel: {1}\nRequired_access: {2}".format(self.id, self.level, self.required_access)

class Group_Achievements:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.description = json['description']
        self.order = json['order']
        self.categories = json['categories']

    def __str__(self):
        return "ID: {0}\nName: {1}\nDescription: {2}\nOrder: {3}\nCategories: {4}".format(self.id, self.name, self.description,
                                                                                            self.order, self.categories)

class Achievements_Categories:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.description = json['description']
        self.order = json['order']
        self.icon = json['icon']
        self.achievements = json['achievements']
    
    def __str__(self):
        return "ID: {0}\nName: {1}\nDescription: {2}\nOrder: {3}\nIcon: {4}\nAchievements: {5}".format(self.id, self.name, self.description, self.order, self.icon, self.achievements)

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
                                                                                                                                
class Dungeons_Since_Reset:
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

class Account_Dyes:
    def __init__(self, json):
        self.dyes = json

    def __str__(self):
        return "Dyes:\n{0}".format(self.dyes)

class Account_Finishers:
    def __init__(self, json):
        self.id = json['id']
        self.permanent = json['permanent']
        if self.permanent == False:
            self.quantity = json['quantity']
        else:
            self.quantity = None

    def __str__(self):
        return "ID: {0}\nPermanent: {1}\nQuantity: {2}".format(self.id, self.permanent, self.quantity)

class Account_Gliders:
    def __init__(self, json):
        self.gliders = json

    def __str__(self):
        return "Gliders:\n{0}".format(self.gliders)

class Account_Cats:
    def __init__(self, json):
        self.id = json['id']

        if 'hint' in json:
            self.hint = json['hint']
        else:
            self.hint = None
    
    def __str__(self):
        return "ID: {0}\nHint: {1}".format(self.id, self.hint)

class Account_Nodes:
    def __init__(self, json):
        self.nodes = json

    def __str__(self):
        return "Nodes: {0}".format(self.nodes)

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

class Account_Mailcarriers:
    def __init__(self, json):
        self.mailcarriers = json
    
    def __str__(self):
        return "Mailcarriers: {0}".format(self.mailcarriers)

"""class Account_Masteries:                                         #This is currently bugged, receiving an Error 400 (bad request error), I'm not sure why, the URL and Headers are just fine
    def __init__(self, json):
        self.id = json['id']
        self.level = json['level']
    
    def __str__(self):
        return "ID: {0}\nLevel: {1}".format(self.id, self.level)"""

class Account_Mastery_Points:
    def __init__(self, json):
        self.totals = json['totals']
        self.unlocked = json['unlocked']

    def __str__(self):
        return "totals: {0}\nUnlocked: {1}".format(self.totals, self.unlocked)

class Account_Materials:
    def __init__(self, json):
        self.id = json['id']
        self.category = json['category']
        self.count = json['count']
        if 'binding' in json:
            self.binding = json['binding']
        else:
            self.binding = None

    def __str__(self):
        return "ID: {0}\nCategory: {1}\nBinding: {2}\nCount: {3}".format(self.id, self.category, self.binding, self.count)

class Account_Minis:
    def __init__(self, json):
        self.minis = json

    def __str__(self):
        return "Minis: {0}".format(self.minis)

class Account_Mounts_Skins:
    def __init__(self, json):
        self.mounts_skins = json
    
    def __str__(self):
        return "Mount Skins: {0}".format(self.mounts_skins)

class Account_Mount_Types:
    def __init__(self, json):
        self.mount_types = json

    def __str__(self):
        return "Mount Types: {0}".format(self.mount_types)

class Account_Outfits:
    def __init__(self, json):
        self.outfits = json

    def __str__(self):
        return "Outfits: {0}".format(self.outfits)

class Account_Pvp_Heroes:
    def __init__(self, json):
        self.pvp_heroes = json

    def __str__(self):
        return "PvP Heroes: {0}".format(self.pvp_heroes)

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