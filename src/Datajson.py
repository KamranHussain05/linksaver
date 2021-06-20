import json
import os


class Datajson:
    def __init__(self):
        self.filePath = "Data.json"
        self.properties = properties = []
        with open(self.filePath, 'r+') as propertiesJSON:
            properties = json.load(propertiesJSON)



    # Used to the check if there is a 'data.txt' file
    # Returns whether a file is present or not
    @staticmethod
    def check_file():
        return os.path.isfile('data.json')

    def createDataFile(self, dumpFile):
        with open(self.filePath, 'w') as f:
            json.dump(dumpFile, f)

    def addButtonFunction(self, buttonName, className, courselink, meetingLink):

        newClass = {
            "Button": f"{buttonName}",
            "Class_Name": f"{className}",
            "Class_Link": f"{courselink}",
            "Meeting_Link": f"{meetingLink}"
        }

        if not self.check_file("data.json"):
            self.createDataFile(newClass)
        else:

