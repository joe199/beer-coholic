from actions import Action
#import database as db

class telegram(Action):
    """docstring for telegram"""
    def __init__(self):
        super(telegram, self).__init__()
        self.consult = ["telegram"]


    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False


    def do(self, column, idem):
        #info = self.db.DataBase.search(idem)
        #No se com cridar la funcio database search desde aqui
        print "searched info"
        return "Telegram Done"
