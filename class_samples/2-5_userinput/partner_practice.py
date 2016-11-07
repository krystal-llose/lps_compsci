# number 5

print("Which month is it? Enter only the number, like 8 for August.")
month = raw_input()

print("Great, you've entered month " + month + ".")
months_left = 12 - int(month)
print("Woot, only " + str(months_left) + "months till the New Year!")
