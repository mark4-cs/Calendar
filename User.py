class User:
    # id
    # mail
    # pswd
    # breakSessionRatio
    # LenSession
    # sleepStartRange
    # sleepAmountRange
    def __init__(self, id=None, mail=None, pswd=None, breakSessionRatio=0.25, LenSession=60, sleepStartRange=(22, 0),
                 sleepAmountRange=(7, 9)):
        self.id, self.mail, self.pswd = id, mail, pswd
        self.breakSessionRatio = breakSessionRatio
        self.LenSession = LenSession
        self.sleepStartRange, self.sleepAmountRange = sleepStartRange, sleepAmountRange

