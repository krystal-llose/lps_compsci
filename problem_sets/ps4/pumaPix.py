print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows.")
shows = 0
my_list = []
while shows < 5:
	print("Enter a show name.")
	series = str(raw_input())
	my_list.append(series)
	shows = shows + 1 	
more = ["Friends", "Criminal Minds"]
	
print("Okay, here's what you entered:")
print(my_list)

number = int(0)
all = my_list + more
all.sort()
print("We've added a couple of important ones.")

for elements in all:
	number = number + 1 
	print(str(number) + ". " + elements)
