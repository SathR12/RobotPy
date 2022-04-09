class Waiter():
    counter = 0
    refreshTime = 0
    isExpired = False

    def __init__(self, refreshTime):
        self.counter = 0
        self.refreshTime = refreshTime

    def increment(self):
        self.counter += 1
        if self.counter >= self.refreshTime:
            self.isExpired = True

    def getIsExpired(self):
        return self.isExpired

    def reset(self):
        self.counter = 0
        self.isExpired = False
        