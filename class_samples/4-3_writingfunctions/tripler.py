# example
# the argument, myNum, must be a number
# returns the number multiplied by three
def tripleIt(myNum):
        trip = myNum * 3 
	return trip 
 
# testing the example
x = 8
y = 3.5
z = -2
 
print("x is " + str(x) + ", y is " + str(y) + ", z is " + str(z))
print("Triple x, y, z...")
print(tripleIt(x))
print(tripleIt(y))
print(tripleIt(z))
 
print("**************Results****************")
p = 2
q = 5
 
# example testing
if tripleIt(p) == 6 and tripleIt(q) == 15:
  print("the example passes")
else:
  print("the example fails")

