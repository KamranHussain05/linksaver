# Used to create a file called "data.txt" under the folder "Data" in the project directory,
# read the file on startup (or create one if there isn't one present)
# and write to it as changes occur on HomeGui/AddCourse
import os.path
import csv


class FileChanger:

    # Used to the check if there is a 'data.txt' file
    # Returns whether a file is present or not
    @staticmethod
    def check_file():
        return os.path.isfile('data.csv')

    # Create new file 'data.csv'
    # Only call if check_file() returns False
    @staticmethod
    def create_file():
        try:
            with open('data.csv', 'w', newline='') as myfile:
                return
        except Exception as e:
            print('Error Creating File: ', e)

    # Reads 'data.csv' and inputs data into program (ex: links, courses, etc)
    # Data d object needs to have 8 terms
    # pass in Data object d
    # Data object required from HomeGui to store link info
    def readFile(self, d):
        data = ''
        num = 0  # number for which line to start inputting into Data object d

        # tries to read 'data.txt' and then input it into Data object d
        try:
            with open('data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # loop through 3 values in row
                    for i in range(3):
                        data = row[i]  # row[i] is element
                        d.replaceStrings(num, data)
                        num += 1

        except Exception as e:
            print('Error Reading File: ', e)

    # Write to 'data.csv'
    # File has to be created before calling
    # param - info string list (ArrayList) being converted into 'data.csv' file
    def write_file(info):
        with open('data.csv', 'w') as file:
            try:
                # creating a csv writer object
                csvwriter = csv.writer(file)

                for i in info:
                    # writing the fields
                    csvwriter.writerow(i)
            except Exception as e:
                print('Error writing to file: ', e)
