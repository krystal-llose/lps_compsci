# number 2 

print("Welcome to the CSU Richmond application! What is your GPA?")
GPA = float(raw_input())

print("How many miles away do you live from CSU Richmond?")
miles = int(raw_input())

if GPA >= 2.0 and miles <= 30:
	print("You've been admitted! Thank you for choosing CSU Richmond!")
if GPA < 2.0 or miles > 30:
	print("Thank you for your interest in CSU Richmond. You are ineligible to attend CSU Richmond.")
if GPA >= 2.5 and miles > 30:
	print("What is your ACT score?")
	act_score = int(raw_input())
	if act_score >= 18: 
		print("Congrats! You've been admitted into CSU Richmond!")
	else: 
		print('You do not fit the criteria for CSU Richmond.')	 
	 
