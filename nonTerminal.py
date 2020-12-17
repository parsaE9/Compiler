class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""
        # self.type =

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value

