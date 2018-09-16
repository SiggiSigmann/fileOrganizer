import os
import time
import re

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


def scannDirectory(scanndir):
	filesToSort = []
	print("scanning " + scanndir)
	for root, dirs, files in os.walk(scanndir):
		for file in files:
			path = os.path.join(root, file)
			if os. path. isfile(path):
				filesToSort.append(path)
	print(str(len(filesToSort)) + " files was found.")
	return filesToSort

def sortFiles(sortdir, yearfolder, filesToSort):
	for file in filesToSort:
		basename = os.path.basename(file)
		(year, month, day, hours, minutes, seconds, wday, ydey, test)= time.localtime(os.stat(file)[8])	#calculate cration date
		year = str(year)
		if year in yearfolder:
			print(os.path.join(sortdir,basename))
			os.rename(file,os.path.join(os.path.join(sortdir,year),basename))
		else:
			os.mkdir(os.path.join(sortdir,year))
			yearfolder.append(year)
			os.rename(file,os.path.join(os.path.join(sortdir,year),basename))



scanndir = "c:\\Users\\siggi\\Downloads\\"
sortdir = "c:\\Users\\siggi\\Desktop\\sort\\"

yearfolder = checkSortDir(sortdir)
filesToSort = scannDirectory(scanndir)
sortFiles(sortdir, yearfolder, filesToSort)
