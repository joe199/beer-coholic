from actions import Action

class nfc(Action):
    """client beer updating"""
    def __init__(self, datab):
        super(nfc, self).__init__(datab, datac)
        self.consult = ["nfc"]

    def is_for_you(self, word):
        if word in self.consult:
            print "is for you nfc"
            return True
        return False

    def do(self, amount, beer):
        print "Serving", amount,"of",beer
        print "NFC Done"
        return "NFC DONE"
