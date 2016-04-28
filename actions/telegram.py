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
        if info is not "ERROR":
            print "retorn de search"
            print info
            for row in info:
                src = (str(row[0]), str(row[1]), str(row[2]), str(row[3]))
                #print src
            src1= "id="+src[0]+" username="+src[1]+" tagid="+src[2]+" name="+src[3]
            print src1

            return src1
        else:
            return "ERROR loguing user"
