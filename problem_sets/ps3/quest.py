# problem set 3  

print("Welcome to Krystal's Quest!")
print('Enter the name of your character:')
character_name = raw_input()

print("Enter strength (1-10):")
strength = int(raw_input())

print("Enter health (1-10):")
health = int(raw_input())

print("Enter luck (1-10):")
luck = int(raw_input())


if strength + health + luck > 15:
	print("You've given your character too many points!")
	print('Default vaules of 5 have been assigned, ' + character_name + '.')
	strength1 = 5
	health1 = 5
	luck1 = 5

if strength + health + luck <= 15:
	print("Your character's strength is " + str(strength) + ", health is " + str(health) + " and luck is " + str(luck) + ".")

print(str(character_name) + ", you've come to a fork in the road. Do you want to go right or left? Enter 'right or left'.")

choice = str(raw_input())

if (choice == 'right') or (choice == 'Right'):
	print("You've come across your favorite baseball team \'s home field. They are one man down and have asked you to fill in a position for the wild card game against the Los Angeles Dodgers.")
	if strength >= 7:
		print("Your high strength resulted in a walk-off grand slam that secured your team a spot in the next round!")
	if strength <7:
		print("Your strength was not enough to result in a basehit. Therefore, your team lost the wild card. Bummer.")

if (choice == 'left') or (choice == 'Left'):
	print("You're currently in line to meet your favorite musical artist at a store that they are sponsored by.")
	if luck >= 6:
		print("Your high luck has given you the final slot to meet your favorite artist! Guess those hours waiting in the cold really paid off.")
	if luck < 6:
		print("Your lack of luck stopped you from meeting your favorite artist. Guess you shouldn't have let that little girl cut you in line.")
