from FileChanger import FileChanger

class Data:
    strings = []

    def __init__(self, num):
        for x in range(num):
            self.strings.append("")

    def replaceStrings(self, num, s):
        self.strings.pop(num)
        self.strings.insert(num, s)

    def returnStrings(self):
        return self.strings

    def getFullString(self, n):
        return self.strings[n]

    def getCourseName(self, n):
        s = self.strings[n]
        if (s.index(";") != -1):
            newString = self.strings[s.index(';') + 1:]
            endInd = newString.find(";")
            return self.strings[s.index(';'):endInd]
        else:
            return ""

    def getMeetingLink(self, n):
        s = self.strings[n]
        if (s.index(";") != -1):
            newString = self.strings[s.index(';') + 1:]
            endInd = newString.find(";")
            return self.strings[endInd]
        else:
            return ""

    def printStrings(self):
        for s in self.strings:
            print(s)
