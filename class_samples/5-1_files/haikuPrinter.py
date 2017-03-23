myFile = open('haiku.txt', 'r')

# print the first three lines 
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())

myFile.close()
