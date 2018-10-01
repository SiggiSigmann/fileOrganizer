import  tkinter as tk
from tkinter import *
from sortDir import *
from question import *
import os

class Gui(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.setUpGui()
		self.counter=0
		self.v = IntVar()



	def setUpGui(self):
		self.sourceDescription = tk.Label( text="Files to sort:")
		self.sourceLocation = tk.Entry( width=40)
		self.sourceLocation.bind('<Key>', self.sourceKeyListener)
		self.sourceChoos = tk.Button( text="Cose Folder", command=self.sourcechooser)

		self.destDescription = tk.Label( text="Sorted file location:")
		self.destLocation = tk.Entry(  width=40)
		self.destLocation.bind('<Key>', self.destKeyListener)
		self.destChoos = tk.Button( text="Cose Folder", command=self.destchooser)

		self.startButton = tk.Button( text="Start", command=self.startProcess)
		self.startButton .bind('<Key>', self.startKeyListener)
		self.stopButton = tk.Button( text="Stop", command=self.stopProcess)
		self.stopButton .bind('<Key>', self.stopKeyListener)

		self.sourceDescription.grid(row=0, column=0, padx=5, pady=5)
		self.sourceLocation.grid(row=0, column=1, padx=5, pady=5)
		self.sourceChoos.grid(row=0, column=2,padx=5, pady=5)

		self.destDescription.grid(row=1, column=0, padx=5, pady=5)
		self.destLocation.grid(row=1, column=1, padx=5, pady=5)
		self.destChoos.grid(row=1, column=2,padx=5, pady=5)

		self.startButton.grid(row=3,column=0)
		self.stopButton.grid(row=3,column=2)

		self.update()



	def startProcess(self):
		yearfolder = checkSortDir(self.destLocation.get())
		filesToSort = scannDirectory(self.sourceLocation.get())
		originalErrorInFiles, sortedErrorInFiles = sortFiles(self.destLocation.get(), yearfolder, filesToSort)
		print(type(originalErrorInFiles))
		print(type(sortedErrorInFiles))
		print("fin")

	def stopProcess(self):
		print("stop")
		self.askWhatToDo(self.counter, None, None)
		self.counter += 1

	def sourcechooser(self):
		file_path = filedialog.askdirectory()
		if file_path != "":
			self.sourceLocation.delete(0,len(self.sourceLocation.get()))
			self.sourceLocation.insert(0, file_path)

	def destchooser(self):
		file_path = filedialog.askdirectory()
		if file_path != "":
			self.destLocation.delete(0,len(self.destLocation.get()))
			self.destLocation.insert(0, file_path)

	def sourceKeyListener(self, event):
		if event.char =='\r':
			self.destLocation.focus_set()

	def destKeyListener(self, event):
		if event.char =='\r':
			self.startButton.focus_set()

	def startKeyListener(self,event):
		if event.char =='\r':
			self.startButton.invoke()

	def stopKeyListener(self,event):
		if event.char =='\r':
			self.stopButton.invoke()

	def askWhatToDo(self, number, sourceImage, destImage):
#		mul=5
#		self.seperator = tk.Canvas(width=self.windowlenghth, height=10)
#		self.seperator.grid(row=number*mul+4, column=0, columnspan=3)
#		self.seperator.create_line(0, 5, self.windowlenghth, 5, width=1, fill="gray")
#
#		self.sourcePicture = tk.Canvas(width=100, height=100, background="green")
#		self.sourcePicture.grid(row=number*mul+5, column=0, rowspan=4)
##
#		self.sourcePicture = tk.Canvas(width=100, height=100, background="blue")
#		self.sourcePicture.grid(row=number*mul+5, column=3, rowspan=4)
#
#		self.radioOption1 = tk.Radiobutton(text="1", variable=self.v, value=0)
#		self.radioOption2 = tk.Radiobutton(text="2", variable=self.v, value=1)
#		self.radioOption3 = tk.Radiobutton(text="3", variable=self.v, value=2)
#		self.radioOption4 = tk.Radiobutton(text="4", variable=self.v, value=3)
#
#		self.radioOption1.grid(row=number*mul+5, column=2)
#		self.radioOption2.grid(row=number*mul+6, column=2)
#		self.radioOption3.grid(row=number*mul+7, column=2)
#		self.radioOption4.grid(row=number*mul+8, column=2)
		print(number)
		self.question1 = Ask(self, "1.png", "2.png");
		self.question1.grid(row=number+5, column=0, columnspan=4)

app = Gui("sort")
app.mainloop()
