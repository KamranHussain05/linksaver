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
        r = ""
        s = strings[n]
        if(s.index(";") != -1):
            newString = strings[s.index(';')+1:]
            n = newString.find(";")
            return strings[s.index(';'):n]
        else:
            return ""
    def getMeetingLink(n):

    def printStrings():
        for s in strings:
            print(s)
        

