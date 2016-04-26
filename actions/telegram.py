from actions import Action

class telegram(Action):
    """docstring for telegram"""
    def __init__(self, datab):
        super(telegram, self).__init__(datab)
        self.consult = ["telegram"]


    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False


    def do(self, column, idem):
        info = self.database.search(column, idem)
        print info
        #No se com cridar la funcio database search desde aqui
        print "searched info"
        return "Telegram Done"
