from actions import Action

class telegram(Action):
    """docstring for telegram"""
    def __init__(self):
        super(telegram, self).__init__()
        self.consult = ["telegram"]

    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False

    def do(self, command):
        return "Telegram Done"
