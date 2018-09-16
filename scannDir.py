import os
import time
import re
import filecmp

#scanns the given directory and return all folders witch consists out of 4
#digits as an arrayself.
#
#@param sortdir		:directory to be checked
#@return			:array which contains the found folders
def checkSortDir(sortdir):
	yearfolder = []
	print("Checking "+sortdir)
	for root, dirs, files in os.walk(sortdir):										#scann sort dir
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
	for root, dirs, files in os.walk(scanndir):										#scann dir to sort
		for file in files:
			path = os.path.join(root, file)
			if os.path.isfile(path):
				filename, file_extension = os.path.splitext(path)
				if endings == "non":												#filter by exrension
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
	originalErrorInFiles = []
	sortedErrorInFiles = []
	for file in filesToSort:
		basename = os.path.basename(file)
		(year, month, day, hours, minutes, seconds, wday, ydey, test)= time.localtime(os.stat(file)[8])	#calculate cration date
		year = str(year)
		if year in yearfolder:
			fileNew = os.path.join(os.path.join(sortdir,year),basename)				#make path to file in sorted directory
			try:
				os.rename(file, fileNew)											#move file
			except Exception:
				if filecmp.cmp(file, fileNew):										#check if the files are the same
					os.remove(file)
				else:
					originalErrorInFiles.append(file)
					sortedErrorInFiles.append(fileNew)
		else:
			os.mkdir(os.path.join(sortdir,year))
			yearfolder.append(year)
			try:
				os.rename(file, fileNew)											#move file
			except Exception:
				if filecmp.cmp(file, fileNew):										#check if the files are the same
					os.remove(file)
				else:
					originalErrorInFiles.append(file)
					sortedErrorInFiles.append(fileNew)
	return originalErrorInFiles, sortedErrorInFiles

#function with ask the user which file should be ceaptself.
#
#@param originalErrorInFiles	: contains files in the to sort location
#@param sortedErrorInFiles		: contains files in the sorted location
def askWhatToDo(originalErrorInFiles, sortedErrorInFiles):
	if originalErrorInFiles:
		print(str(len(originalErrorInFiles)) + " conflicts")
		print("0 - do nothing")
		print("type in which file should be deleted")
		for i in range(len(originalErrorInFiles)):
			acceptInput = 1
			while acceptInput:
				print("-----------------------")
				print("(1)"+originalErrorInFiles[i] + " (2)" + sortedErrorInFiles[i])
				userInput = "error"
				
				try:
					userInput = int(input("Do action: "))
				except ValueError:
					print("wrong input")

				if userInput == 0:
					acceptInput = 0
				elif userInput == 1:
					os.remove(originalErrorInFiles[i])
					acceptInput = 0
				elif userInput == 2:
					os.remove(sortedErrorInFiles[i])
					acceptInput = 0
				else:
					print("Not accepted input.")
					print("0 - do nothing")
					print("1 - delete original file ")
					print("2 - delete files in sorted location")

#The function takes two path and sorts the files in the first path and then
#copy it to argument two. The files can be filtered by the endingsself.
#
#@param scanndir	: diretory which have to be sorted
#@param sortdir		: directory which will contain the files avert being sorted
#@param endings		: (optional)the ending which can be used as a filter
def runSort(scanndir,sortdir,endings = "non"):
	yearfolder = checkSortDir(sortdir)
	filesToSort = scannDirectory(scanndir)
	originalErrorInFiles, sortedErrorInFiles = sortFiles(sortdir, yearfolder, filesToSort)
	askWhatToDo(originalErrorInFiles, sortedErrorInFiles)


scanndir = "c:\\Users\\siggi\\Downloads\\"
sortdir = "c:\\Users\\siggi\\Desktop\\sort\\"

runSort(scanndir, sortdir)

#TODO:add rename option
