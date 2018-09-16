import os
import time
import re

#scanns the given directory and return all folders witch consists out of 4
#digits as an arrayself.
#
#@param sortdir		:directory to be checked
#@return			:array which contains the found folders
def checkSortDir(sortdir):
	yearfolder = []
	print("Checking "+sortdir)
	for root, dirs, files in os.walk(sortdir):
		for dir in dirs:
			if re.match("[0-9]*", dir):
				yearfolder.append(dir);
				print(dir)
	print(str(len(yearfolder)) + " folders was found.")
	return yearfolder

#scanns the given directory and return all files in an array. If a second
#parameter is givin it only adds the file to the array if the ending of the file
#match the value of the argument "ending".
#
#@param scanndir	:contains path which has to be scanned.
#@param endings		:(optional)ending of the file which shouls be returned.
#@returned			:array which contaisn related fiels.
def scannDirectory(scanndir, endings = "non"):
	filesToSort = []
	print("scanning " + scanndir)
	for root, dirs, files in os.walk(scanndir):
		for file in files:
			path = os.path.join(root, file)
			if os. path. isfile(path):
				filename, file_extension = os.path.splitext(path)
				if endings == "non":
					print("non")
					filesToSort.append(path)
				elif endings == file_extension[1:]:
					filesToSort.append(path)
	print(str(len(filesToSort)) + " files was found.")
	return filesToSort

#The subroutins move the files into the folder sortdir and sort them into the
#subdirectory to sort them by yearself.
#
#@param sortdir		:path of the folder which will contain the sorted files.
#@param yearfolder	:array which contains existing year folderself.
#@param filesToSort	:array which contains the files which have to be sorted.
def sortFiles(sortdir, yearfolder, filesToSort):
	for file in filesToSort:
		basename = os.path.basename(file)
		(year, month, day, hours, minutes, seconds, wday, ydey, test)= time.localtime(os.stat(file)[8])	#calculate cration date
		year = str(year)
		if year in yearfolder:
			print(os.path.join(sortdir,basename))
			#os.rename(file,os.path.join(os.path.join(sortdir,year),basename))
			print(os.path.join(os.path.join(sortdir,year),basename))
		else:
			os.mkdir(os.path.join(sortdir,year))
			yearfolder.append(year)
			os.rename(file,os.path.join(os.path.join(sortdir,year),basename))



scanndir = "c:\\Users\\siggi\\Downloads\\"
sortdir = "c:\\Users\\siggi\\Desktop\\sort\\"

yearfolder = checkSortDir(sortdir)
filesToSort = scannDirectory(scanndir)
sortFiles(sortdir, yearfolder, filesToSort)
