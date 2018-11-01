class Model:
    def __init__(self):
        self.scoredb = []

    def setScoreDB(self, scoredb):
        self.scoredb = scoredb

    def getScoreDB(self):
        return self.scoredb

    def addRecord(self, record):
        self.scoredb += [record]
