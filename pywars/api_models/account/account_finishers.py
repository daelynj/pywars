import json

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
