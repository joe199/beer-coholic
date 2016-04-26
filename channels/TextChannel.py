
from channels import Channel

class TextChannel(Channel):
    """channel class, reads file channels"""
    def __init__(self,cfg=None, name = "TextChannel"):
        super(TextChannel, self).__init__(cfg, name)
        self.prova_nfc = []
        with open("prova_nfc.txt","r") as f:
            for line in f:
                line=line.strip()
                self.prova_nfc.append(line)

    def get_msg(self):
        if self.msg_avail():
            return self.prova_nfc.pop(0)

    def msg_avail(self):
        return len(self.prova_nfc) > 0

    def respond(self, response):
        print "Response: ", response
