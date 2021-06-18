import webbrowser, validators

class LinkOpener:
    theURL = ""
    def __init__ (self, toOpen):
        theURL = toOpen
        if (self.isValid(theURL)):
            webbrowser.open(theURL)
    
    def isValid(self, urlStr):
        
        if (urlStr.index("htt") == -1):
            urlStr = "https://" + urlStr
            self.theURL = urlStr
        valid=validators.url(urlStr)   
        if (valid):
            return True
        else:
            return False





