import json

class Account_Nodes:
    def __init__(self, json):
        self.nodes = json

    def __str__(self):
        return "Nodes: {0}".format(self.nodes)