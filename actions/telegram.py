from actions import Action
from database.database import DataBase as db

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
        info = db().search(column, idem)
        #No se com cridar la funcio database search desde aqui
        print "searched info:  ", info
        return "Telegram Done"
