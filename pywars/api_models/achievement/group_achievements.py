import json

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