import os

filedir = "./"

for root, dirs, filenames in os.walk(filedir):
	for f in filenames:
		os.system('pandoc "%s" -o "%s"' % (f, f+'.txt' ))

