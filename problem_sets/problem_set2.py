# calculateDonuts.py

print('How many people will you have at your party?')
people = int(raw_input())

print('How many donuts will you have at your party?')
donuts = int(raw_input())

donuts_people = donuts // people

print('Our party has ' + str(people)  + ' people and ' + str(donuts)  + ' donuts.') 
print('Each person at the party gets ' + str(donuts_people) + ' donuts')
