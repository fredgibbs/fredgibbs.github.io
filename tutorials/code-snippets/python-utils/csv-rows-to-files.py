# This script reads a CSV file, creating a new text file for each row, with a filename and content derived from particular fields. In this case, two fields are joined to create the filename, and one field is used for the content.

# USAGE: csv-rows-to-files.py csvfile
# where csvfile must be a valid CSV text file with a header row (the first line of the CSV file is skipped)

import csv
import sys

inputfilename = sys.argv[1]

with open(inputfilename, 'rt', encoding='utf-8') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    # skip header row
    next(reader)

    for row in reader:
        topic = row[0] #column A: topic
        content = row[5] # column F: text

        # the timestamp contains " " and ":", but these can make tricky filenames
        # this could be handled more elegantly with date formatting functions and a different timestamp format
        date = row[7].replace(" ","-").replace(":","-") # column H: date

        # assemble filename from fields and output expected file to be created
        filename = topic + '_' + date + '.txt'
        print("creating file: " + filename)

        # create new file for writing, and write content to new file
        with open(filename,'w') as outputfile:
            outputfile.write(content)
            outputfile.close()
