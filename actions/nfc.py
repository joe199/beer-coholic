from actions import Action

class nfc(Action):
    """client beer updating"""
    def __init__(self):
        super(nfc, self).__init__()
        self.consult = ["nfc"]

    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False

    def do(self, command):
        print "Serving beer:", " ".join(command)
        return "NFC DONE"
