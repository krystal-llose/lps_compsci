# teamManagerDeluxe.py

class Player(object):

	def __init__(self, name, age, goals, jersey, position):
		self.name = name
    		self.age = age
    		self.goals = goals
    		self.jersey = jersey
    		self.position = position

 	def getStats(self):
                print("Player: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jersey))
		print("Position: " + self.position)
		
 
# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(playerList, filename):
    # open the file
	giants = open(filename, 'w')
	for member in team:
		output = 'memberName' + ' memberAge' + ' memberGoals' + ' memberJersey' + ' memberPosition' 
    # write to the file
 		giants.write(output + '\n')
    # close the file
 		giants.close()
  
# takes a filename for a file of players
# returns a list of Players
def loadTeam(filename):
 
    # create empty list
 	team = []
    # open the file
 	giants = open(filename, 'r') 
    # read each line and create Player from it (use a loop)
 	baseball = giants.readline()
	while baseball != "":
        # split each line into a list of the variables
		yikes = giants.split()
		team.append(Player(yikes[1], yikes[2], yikes[3], yikes[4]))
        # read each next line
 		baseball = giants.readline()
    # close the file
 		giants.close()
    # return the completed list
 	return team


# code execution

print('Welcome to Team Manager Deluxe!')
print('Do you want to start with a new team or open an existing team?')
print('Enter the number of your choice and press Enter.')
print('(1) Start with a new team')
print('(2) Open a file for an existing team')

response = raw_input()

if response == '1':
	pass

elif response == '2':
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	fileName = raw_input()
	team = loadTeam(fileName)

# empty list for adding players
team = []

grandSlam = True

while grandSlam:
 	print('What do you want to do? Enter the number of your choice and press Enter.')
        print('(1) Add a player')
        print('(2) Print all players')
        print('(3) Print average number of goals for all players')
        print('(4) Save your player list to a file')
        print('(0) Leave the program (save first to avoid losing your data!)')

        choice = raw_input()

        if choice == '0':
                grandSlam = False

# creates a new player profile
        elif choice == '1':
                print("Player name?:")
                playerName = raw_input()
                print("Player age?:")
                playerAge = raw_input()
                print("Enter the amount of goals made:")
                playerGoals = raw_input()
                print("Player's jersey number?")
                playerJersey = raw_input()
                print("Player's postion?")
                playerPosition = raw_input()

                team.append(Player(playerName, playerAge, playerGoals, playerJersey, playerPosition))
                print('Great! Your player will now appear in the list when ran.')

# prints the entire list of players 
        elif choice == '2':
                for t in team:
                        print(t.getStats())

# prints average amount of goals as a team
        elif choice == '3':
                pass 	

# saves to a file 
        elif choice == '4':
                print('What would you like to name your file?')
                fileName = raw_input()
                saveTeam(team, fileName + ".tmd")
