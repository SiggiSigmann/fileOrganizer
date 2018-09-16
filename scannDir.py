import os
for root, dirs, files in os.walk("c:\\Users\\siggi\\Downloads\\"):
	for file in files:
		print(root +" - " +file)
