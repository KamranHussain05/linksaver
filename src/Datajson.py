import json
import os


class Datajson:
    def __init__(self):
        self.filePath = "Data.json"
        self.properties = properties = []
        with open(self.filePath, 'r+') as self.propertiesJSON:
            properties = json.load(self.propertiesJSON)


    # Used to the check if there is a 'data.txt' file
    # Returns whether a file is present or not
    @staticmethod
    def check_file():
        return os.path.isfile('data.json')

    def createDataFile(self, dumpFile):
        with open(self.filePath, 'w') as f:
            json.dump(dumpFile, f)


    def editButton(self, buttonName, className, courselink, meetingLink):

        for course in self.properties:
            if(course['button'] == buttonName):
                course['class_name'] = className
                course['class_link'] = courselink
                course['meeting_link'] = meetingLink
            else:
                self.addButtonFunction(self,buttonName, className, courselink, meetingLink)

    def addButtonFunction(self, buttonName, className, courselink, meetingLink):

        newClass = {
            "button": f"{buttonName}",
            "class_name": f"{className}",
            "class_link": f"{courselink}",
            "meeting_link": f"{meetingLink}"
        }

        if not self.check_file("data.json"):
            self.createDataFile(newClass)
        else:
            self.propertiesJSON.append(newClass)
            self.propertiesJSON.seek(0, 0)
            js_format = json.dumps(self.properties, indent=4)
            self.propertiesJSON.write(js_format)
