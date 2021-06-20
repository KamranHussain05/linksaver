import json
import os


class Datajson:
    def __init__(self):
        self.filePath = "Data.json"
        properties = []
        self.properties = properties
        with open(self.filePath, 'r+') as self.propertiesJSON:
            self.properties = json.load(self.propertiesJSON)


    # Used to the check if there is a 'data.txt' file
    # Returns whether a file is present or not
    @staticmethod
    def check_file():
        return os.path.isfile('data.json')

    def createDataFile(self, dumpFile):
        with open(self.filePath, 'w') as f:
            json.dump(dumpFile, f)

    #Edits the index source with buttonName being the name of the index source,
    def editIndexSource(self, buttonName, className, courselink, meetingLink):
        print(f'editing index source{buttonName}, {className}, {courselink}, {meetingLink}')
        print(f'{self.properties} {len(self.properties)}')

        for course in self.properties:
            print('Marker 1')

            if(course['index_source'] == buttonName and self.check_file() and len(self.properties) > 0):
                print("marker2")
                course['class_name'] = className
                course['class_link'] = courselink
                course['meeting_link'] = meetingLink
            else:
                print("marker2")
                self.addButtonFunction(self,buttonName, className, courselink, meetingLink)
                return
        self.addButtonFunction(self, buttonName, className, courselink, meetingLink)

    def addIndexSource(self, buttonName, className, courselink, meetingLink):
        print(f'adding index source{buttonName}, {className}, {courselink}, {meetingLink}')
        newClass = {
            "index_source": f"{buttonName}",
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
