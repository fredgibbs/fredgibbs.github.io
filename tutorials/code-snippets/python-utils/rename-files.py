#Python Script for HIST666
#Script Title: Archive_File_Rename_Tool_Version_3.12
#Script locates files, renames those files, and moves them to a permanent directory
#Updated: Dec 1 2014

#Import required modules
import os
import time

#Define starting variables
Date = time.strftime("%Y-%m-%d")
seperator = "_"

"""This section sets up source and target directories and file prefixes"""

#Find folder from image scans
#SubjectFolder = raw_input("Name of subject folder (Note:folder name should not contain spaces)?") 
sourceDir = "/Users/fwgibbs/Dropbox/courses/digital-methods/python/workingfiles"
print "source directory set to: " + sourceDir

#hint: don't do stuff when you're just defining stuff
#os.chdir(SubjectPath)

#Print date as string in the format "yyyymmdd"
print Date

#Request Publication Name for new Filename
#PublicationName = raw_input("Name of publication for new file name?")
PublicationName = "book1"
print "publication name set to: " + PublicationName

#Concatenate elements to create new Filename Prefix
#individual files don't need date since the date is in the parent dir?
filePrefix = PublicationName
print "filename scheme is: " + filePrefix


"""This section creates a name for the new directory which
will contain the renamed files"""

#set up a base path to always work under (like Documents, but better)
targetDirPrefix = "/Users/fwgibbs/Dropbox/courses/digital-methods/python/"

#Request Institution Name for DirectoryName
#DirectoryName = raw_input("Name of Institution for new directory/folder name?")
targetDirCore = "archive1"

#Concatenate elements to create new directory/folder name
#always use os.path.join to make paths to keep code OS agnostic
newDirectory = os.path.join(targetDirPrefix, Date + seperator + targetDirCore)
print "directory scheme set to: " + newDirectory

#get all files in source directory and sort by name
files = os.listdir( sourceDir )
files.sort()
counter=0

#iterate through files and rename/move into target directory
for file in files:
	#notice the relative, not absolute, path in what gets outputted below
	print "found: " + file
	
	#strip off file extension to preserve it for the renamed file
	origExt = os.path.splitext(file)[1]
	print "original extension is: " + origExt

	#create new file path and name
	newFile = os.path.join(newDirectory, filePrefix + seperator + str(counter) + origExt) 
	print "renaming to: " + newFile

	#each file in files is not fully pathed; create full path so renaming function can find the file
	oldFile = os.path.join(sourceDir, file)

	#actually rename (= move) the file from source to target directory with new prefixes
	#os.renames(oldFile,newFile)
	
	counter = counter + 1