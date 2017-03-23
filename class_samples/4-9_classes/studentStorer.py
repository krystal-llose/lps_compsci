class Student(object):
	""" Encapsulates a student, their gpa, and college application list. """

	def __init__(self, name, gpa, fave_snack):
		self.name = name
		self.gpa = gpa
		self.fave_snack = fave_snack 

		self.collegeList = []

	def getSnack(self):
		return self.fave_snack

class College(object):
	""" Encapsulates a school """

	def __init__(self, name, minGPA):
		self.name = name 
		self.minGPA = minGPA

	def acceptStudent(self, studentGPA):
		if studentGPA >= self.minGPA:
			return True
		else:
			return False 

myFirstChoice = College("Columbia", 3.95)
krystalGPA = 4.0
print("Did Krystal get in?")
print(myFirstChoice.acceptStudent(krystalGPA))

# code execution starts here
myFirstStudent = Student("Jenny", 4.0, "carrots")
print(myFirstStudent.getSnack())

mySecondStudent = Student("Kelvin", 3.9, "Takis")
print(mySecondStudent.getSnack())
