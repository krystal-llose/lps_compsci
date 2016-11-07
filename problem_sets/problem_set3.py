# number 4

print("Welcome to Krystal's Quest!")
print('Enter the name of your character:')
character_name = raw_input()

print('Enter strength (1-10):')
strength = int(raw_input())

print('Enter health (1-10):')
health = int(raw_input())

print('Enter luck (1-10):')
luck = int(raw_input())


if strength + health + luck > 15:
	print("You've given your character too many points!")
	print('Default vaules of 5 have been assigned, ' + character_name + '.')
	strength1 = 5
	health1 = 5
	luck1 = 5

if strength + health + luck <= 15:
	print("Your character's strength is " + str(strength) + ", health is " + str(health) + " and luck is " + str(luck) + ".")

print("character_name + ", you’ve come to a fork in the road. Do you want to go right or left? Enter 'right' or 'left'.")
