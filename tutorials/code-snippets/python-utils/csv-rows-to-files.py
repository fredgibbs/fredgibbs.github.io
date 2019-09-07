# This script reads a CSV file, creating a new text file for each row, with a filename and content derived from particular fields. In this case, two fields are joined to create the filename, and one field is used for the content.

# USAGE: csv-rows-to-files.py csvfile
# where csvfile must be a valid CSV text file with a header row (the first line of the CSV file is skipped)

import csv

inputfilename = sys.argv[1]

with open(inputfilename, 'rb') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    # skip header row
    next(reader)

    for row in reader:
        topic = row[0] #column A: topic
        content = row[5] # column F: text

        # the date string has a space in it, but that's no good for a filename.
        date = row[7].replace(" ","-") # column H: date

        # assemble filename from fields and output expected file to be created
        filename = topic + '_' + date + '.txt'
        print("creating file: " + filename)

        # create new file for writing, and write content to new file
        with open(filename,'w') as outputfile:
            outputfile.write(content)
            outputfile.close()
