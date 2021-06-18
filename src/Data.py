class Data:
    strings = []
    def __init__(self, num):
        for x in range num:
            strings.append("")
    def replaceStrings( num, s):
		strings.pop(num)
		strings.insert(num,s)
    def getFullString(n):
        return strings[n]
    def getCourseName(n):
        s = strings[n]
        if(s.index(";") != -1):
            newString = strings[s.index(';')+1:]
            endInd = newString.find(";")
            return strings[s.index(';'):endInd]
        else:
            return ""
    def getMeetingLink(n):
        s = strings[n]
        if(s.index(";") != -1):
            newString = strings[s.index(';')+1:]
            endInd = newString.find(";")
            return strings[endInd]
        else:
            return ""

    def printStrings():
        for s in strings:
            print(s)
        

