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

		self.scroll = tk.Scrollbar()

		self.sourceDescription.grid(row=0, column=0, padx=5, pady=5)
		self.sourceLocation.grid(row=0, column=1, padx=5, pady=5)
		self.sourceChoos.grid(row=0, column=2,padx=5, pady=5)

		self.destDescription.grid(row=1, column=0, padx=5, pady=5)
		self.destLocation.grid(row=1, column=1, padx=5, pady=5)
		self.destChoos.grid(row=1, column=2,padx=5, pady=5)

		self.startButton.grid(row=3,column=0)
		self.stopButton.grid(row=3,column=2)

		self.scroll.grid(row=4, column=3)

		self.listbox = tk.Canvas(yscrollcommand=self.scroll.set, height=100, background="yellow")
		self.listbox.grid(row=4, column=0, columnspan=2)

		self.scroll.config(command=self.listbox.yview)

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
		Ask(self.listbox, "1.png", "2.png").grid(row=1+number, column=2)
		#self.question1 = Ask(self, "1.png", "2.png");
		#self.question1.grid(row=number+5, column=0, columnspan=4)

app = Gui("sort")
app.mainloop()
