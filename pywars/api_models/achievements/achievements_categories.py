import json

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