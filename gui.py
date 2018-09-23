import  tkinter as tk
from tkinter import ttk,filedialog


class Gui(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.setUpGui()

	def setUpGui(self):
		self.sourceDescription = tk.Label(self, text="Files to sort:")
		self.sourceLocation = tk.Entry(self, width=40)
		self.sourceLocation.bind('<Key>', self.sourceKeyListener)
		self.sourceChoos = tk.Button(self, text="Cose Folder", command=self.sourcechooser)

		self.destDescription = tk.Label(self, text="Sorted file location:")
		self.destLocation = tk.Entry(self,  width=40)
		self.destLocation.bind('<Key>', self.destKeyListener)
		self.destChoos = tk.Button(self, text="Cose Folder", command=self.destchooser)

		self.startButton = tk.Button( text="Start", command=self.startProcess)
		self.startButton .bind('<Key>', self.startKeyListener)
		self.stopButton = tk.Button( text="Stop", command=self.stopProcess)
		self.stopButton .bind('<Key>', self.stopKeyListener)

		self.progressBar = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=450)

		self.sourceDescription.grid(row=0, column=0, padx=5, pady=5)
		self.sourceLocation.grid(row=0, column=1, padx=5, pady=5)
		self.sourceChoos.grid(row=0, column=2,padx=5, pady=5)

		self.destDescription.grid(row=1, column=0, padx=5, pady=5)
		self.destLocation.grid(row=1, column=1, padx=5, pady=5)
		self.destChoos.grid(row=1, column=2,padx=5, pady=5)

		self.startButton.grid(row=3,column=0)
		self.stopButton.grid(row=3,column=2)

		self.progressBar.grid(row=4, columnspan=3, padx=5, pady=5)

	def startProcess(self):
		self.progressBar.start()

	def stopProcess(self):
		self.progressBar.stop()

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

app = Gui("sort")
app.mainloop()
