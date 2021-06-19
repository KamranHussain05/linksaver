import webbrowser, validators

class LinkOpener:
    theURL = ""
    def __init__ (self, toOpen):
        theURL = toOpen
        if (self.isValid(theURL)):
            webbrowser.open(theURL)
    
    def isValid(self, urlStr):
        
        if (urlStr[0] != 'h' or urlStr[1] != 't'):
            urlStr = "https://" + urlStr
            self.theURL = urlStr
        valid=validators.url(urlStr)   
        if (valid):
            return True
        else:
            print("this link is not valid!")
            return False

    def openLink(self):




