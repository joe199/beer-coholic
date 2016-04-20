class Channel(object):
    """Channel class"""
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name

    def respond(self, response):
        print "Response: ", response


class TextChannel(Channel):
    """channel class, reads file channels"""
    def __init__(self, name = "TextChannel"):
        super(TextChannel, self).__init__(name)
        self.messages = []
        with open("prova_nfc.txt","r") as f:
            for line in f:
                self.messages.append(line)

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0
