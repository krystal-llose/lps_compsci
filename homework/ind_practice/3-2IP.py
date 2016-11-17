# number 2

# this is tells the user what the put in
print("How old are you?")
# this makes sure that python reads the data as an integer
age = int(input())

# this asks the user for their height 
print("How many inches tall are you?")
# this makes sure that python reads the data as an integer
height = int(input())

# this tells python the output based on what the user inputs
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
