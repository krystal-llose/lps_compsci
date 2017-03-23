# launch.py 

# this allows the file to be opened and read
walking_file = open("walking_instructions.txt", "r")

# this allows the user to read a line from the text file and print it one at a time while also adding something to it  
lineToPrint = walking_file.readline()
while lineToPrint != "":
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()

# this closes the file so that it cannot be touched until opened once again 
walking_file.close()
