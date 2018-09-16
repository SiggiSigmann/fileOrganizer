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
				print(path)
	print(str(len(filesToSort)) + " files was found.")
	return filesToSort

def sortFiles(scanndir, yearfolder, filesToSort):
	for file in filesToSort:
		(year, month, day, hours, minutes, seconds, wday, ydey, test)= time.localtime(os.stat(file)[8])	#calculate cration date
		print(str(year) + " "+ str(month) + " "+ str(day))
		if year in yearfolder:
			print("ok")
		else:
			print("false")



scanndir = "c:\\Users\\siggi\\Downloads\\";
sortdir = "c:\\Users\\siggi\\Desktop\\sort\\";

yearfolder = checkSortDir(sortdir)
filesToSort = scannDirectory(scanndir)
sortFiles(scanndir, yearfolder, filesToSort);
