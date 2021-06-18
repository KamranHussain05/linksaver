class Data:
    strings = []
    def __init__(self, num):
        for x in range num:
            strings.append("")
    def replaceStrings(int num, String s):
		strings.pop(num)
		strings.insert(num,s)
    def getFullString(int n):
        return strings[n]
    def getCourseName(int n):
        String s = strings[n]
        if(s.index(";") != -1):
            

