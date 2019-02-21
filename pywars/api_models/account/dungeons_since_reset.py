import json

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