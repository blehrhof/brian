#open file
#testfile=open('C://Users//bl11749//Documents//My Projects//demo.txt',"r")

# firstline=testfile.readline()
# print(firstline)
# secondline=testfile.readline()
# print(secondline)

# read all file contents
# allfilecontents=testfile.read()
# print(allfilecontents)

import csv

filename='C://Users//bl11749//Documents//My Projects//demo.txt'
accessmode='r'

with open(filename, 'r') as mycsvfile:
    # read file contents

    x = csv.reader(mycsvfile)
    # or
    # datafromfile=csvreader(mycsvfile, delimiter="|")

    # datafromfile is a list of the rows

    for currentrow in x :
        print(currentrow)
        print(currentrow[2])
        print('@ '.join(currentrow))
