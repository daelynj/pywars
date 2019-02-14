import json

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