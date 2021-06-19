import validators
import webbrowser

class LinkOpener:
    theURL = ""

    def openLink(self, toOpen):
        theURL = toOpen
        if (self.isValid(theURL)):
            webbrowser.open(theURL)

    def isValid(self, urlStr):

        if urlStr[0] != 'h' or urlStr[1] != 't':
            urlStr = "https://" + urlStr
            self.theURL = urlStr
        valid = validators.url(urlStr)
        if (valid):
            return True
        else:
            print("this link is not valid!")
            return False

    # pass in string to open
    @staticmethod
    def openLink(s):
        webbrowser.open(s)
