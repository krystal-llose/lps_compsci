# dictionaries
# contacts.py

print('Welcome to Contacts!' + '\n' + 'What would you like to do?' + '\n')

myContacts = {}

run = True
while run:

	print('(0) Exit the Contacts app.')
	print('(1) Add a phone number.')
	print('(2) Print the full list of contacts.')
	print("(3) Enter a name to retrieve that contact's phone number.")
	print('(4) Delete a contact.')
	print('(5) Update a contact.')
	choice = raw_input()

	if choice == '1':
		print("What is the name of your contact?")
		name = raw_input()
		print("What is the phone number of this contact?")
		number = raw_input()
		myContacts[name] = number 

# if choice 2, dictionary of contacts will appear
	elif choice == '2':
		print myContacts 

# if choice 3, number of certain person will be pulled from dictionary
	elif choice == '3': 
		print('Whose number would you like?')
		individual = raw_input()
		print('Okay, here is their number.')
		print(myContacts[individual])

# if choice 4, contact deleted
	elif choice == '4':
		print('Would you like to delete a contact? Which one?')
		deletedContact = raw_input()
		del(myContacts[deletedContact])
		print('Contact has now been deleted.') 

# if choice 5, contact will get updated
	elif choice == '5':
		print('Which contact would you like to update?')
		update = raw_input()
		print('What is the new number?')
		new = raw_input()
		myContacts[update] = new

# if 0, close program
	elif choice == '0':
		run = False

