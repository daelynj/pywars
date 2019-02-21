import json

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

class Account_Raids:
    def __init__(self, json):
        self.raids = json

    def __str__(self):
        return "Raids: {0}".format(self.raids)

class Account_Recipes:
    def __init__(self, json):
        self.recipes = json

    def __str__(self):
        return "Recipes: {0}".format(self.recipes)

class Account_Skins:
    def __init__(self, json):
        self.skins = json

    def __str__(self):
        return "Skins: {0}".format(self.skins)

class Account_Titles:
    def __init__(self, json):
        self.titles = json

    def __str__(self):
        return "Titles: {0}".format(self.titles)

class Account_Wallet:
    def __init__(self, json):
        self.id = json['id']
        self.value = json['value']
    
    def __str__(self):
        return "ID: {0}\nValue: {1}".format(self.id, self.value)

class Characters:
    def __init__(self, json):
        self.characters = json

    def __str__(self):
        return "Characters: {0}".format(self.characters)

class Character_Overview:
    def __init__(self, json):
        self.name = json['name']
        self.race = json['race']
        self.gender = json['gender']
        self.profession = json['profession']
        self.level = json['level']
        self.age = json['age']
        self.created = json['created']
        self.deaths = json['deaths']
        self.crafting = json['crafting']
        self.equipment = json['equipment']
        self.backstory = json['backstory']
        self.wvw_abilities = json['wvw_abilities']
        self.specializations = json['specializations']
        self.skills = json['skills']
        self.equipment = json['equipment']
        self.recipes = json['recipes']
        self.equipment_pvp = json['equipment_pvp']
        self.training = json['training']
        self.bags = json['bags']

        if 'guild' in json:
            self.guild = json['guild']
        else:
            self.guild = None
        if 'title' in json:
            self.title = json['title']
        else:
            self.title = None
        
    #perhaps need to figure out a way to make this sentence not so long
    #I also don't know how I feel about the equipment etc. lists appearing the way they do in the print statement, but really the prints are just for testing
    def __str__(self):
        return "Name: {0}\nRace: {1}\nGender: {2}\nProfession: {3}\nLevel: {4}\nGuild: {5}\nAge: {6}\nCreated: {7}\nDeaths: {8}\nCrafting: {9}\nTitle: {10}\nBackstory: {11}\nWvW abilities: {12}\nSpecializations: {13}\nSkills: {14}\nEquipment: {15}\n Recipes: {16}\nPvP equipment: {17}\nTraining: {18}\nBags: {19}".format(self.name, self.race, self.gender, self.profession, self.level, 
                                                                                                                        self.guild, self.age, self.created, self.deaths, self.crafting, 
                                                                                                                        self.title, self.backstory, self.wvw_abilities, self.specializations,
                                                                                                                        self.skills, self.equipment, self.recipes, self.equipment_pvp, 
                                                                                                                        self.training, self.bags)

class Character_Backstory:
    def __init__(self, json):
        self.backstory = json['backstory']

    def __str__(self):
        return "Backstory: {0}".format(self.backstory)

class Character_Core:
    def __init__(self, json):
        self.name = json['name']
        self.race = json['race']
        self.gender = json['gender']
        self.profession = json['profession']
        self.level = json['level']
        self.age = json['age']
        self.created = json['created']
        self.deaths = json['deaths']

        if 'guild' in json:
            self.guild = json['guild']
        else:
            self.guild = None
        if 'title' in json:
            self.title = json['title']
        else:
            self.title = None

    def __str__str(self):
        return "Name: {0}\nRace: {1}\nGender: {2}\nProfession: {3}\nLevel: {4}\nGuild: {5}\nAge: {6}\nCreated: {7}\nDeaths: {8}\nTitle: {9}".format(self.name, self.race, self.gender, self.profession, self.level, 
                                                                                                                                                    self.guild, self.age, self.created, self.deaths, self.title)

class Character_Crafting:
    def __init__(self, json):
        self.crafting = json
        
    def __str__(self):
        return "Crafting: {0}".format(self.crafting)

class Character_Equipment:
    def __init__(self, json):
        self.equipment = json['equipment']
        
    def __str__(self):
        return "Equipment: {0}".format(self.equipment)

class Character_Heropoints:
    def __init__(self, json):
        self.heropoints = json
        
    def __str__(self):
        return "Heropoints: {0}".format(self.heropoints)

class Character_Inventory:
    def __init__(self, json):
        self.inventory = json
        
    def __str__(self):
        return "Inventory: {0}".format(self.inventory)

class Character_Recipes:
    def __init__(self, json):
        pass
        
    def __str__(self):
        pass

class Character_Sab:
    def __init__(self, json):
        pass
        
    def __str__(self):
        pass

class Character_Skills:
    def __init__(self, json):
        pass
        
    def __str__(self):
        pass

class Character_Specializations:
    def __init__(self, json):
        pass
        
    def __str__(self):
        pass

class Character_Training:
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