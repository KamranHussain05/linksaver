from FileChanger import FileChanger


class Data:
    strings = []
    def __init__(self, num):

        for x in range(num):
            self.strings.append("")

    def replaceStrings(self, pos, val):
        self.strings.pop(pos)
        self.strings.insert(pos, val)

    def returnStrings(self):
        return self.strings

    def getFullString(self, n):
        return self.strings[n]

    def getCourseName(self, n):
        s = self.strings[n]
        if (s.find(";") != -1):
            newString = self.strings[s.index(';') + 1:]
            endInd = newString.find(";")
            return self.strings[s.index(';'):endInd]
        else:
            return ""

    def getCourseLink(self, n):
        s = self.strings[n]
        r = s[s.find(";")+1:]
        rindex = r.find(";")
        if (s.find(";") != -1 and rindex != -1):
            s[s.find(';')+1: rindex]
            self.strings[s.index(';') + 1:]
            newString = self.strings[s.index(';') + 1:rindex]
            return newString
        else:
             return ""

    def getMeetingLink(self, n):
        s = self.strings[n]
        if s.find(";") != -1:
            # error here - code disappears
            newString = self.strings[s.index(';') + 1:]
            endInd = newString.find(";")
            return self.strings[endInd]
        else:
            return ""

    def printStrings(self):
        for s in self.strings:
            print(s)
