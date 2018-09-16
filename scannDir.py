import os

scanndir = "c:\\Users\\siggi\\Downloads\\";

for root, dirs, files in os.walk(scanndir):
	for file in files:
		path = os.path.join(root, file)
		print(path)
		print(os.stat(path)[8])
		print()
