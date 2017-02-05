# drawCubes.py
#repl.it

# rhombus w 60 and 120 degree angles
# no loop bc only two times 
def makeRhombus(myTurtle):
  myTurtle.speed(5)
  myTurtle.right(30)
  myTurtle.left(60)
  myTurtle.forward(40)
  myTurtle.left(120)
  myTurtle.forward(40)
  myTurtle.left(60)
  myTurtle.forward(40)
  myTurtle.left(120)
  myTurtle.forward(40)

# top
def rhombusColor(myTurtle):
  myTurtle.color("dark red")
  myTurtle.fillcolor("dark red")
  myTurtle.begin_fill()
  makeRhombus(myTurtle)
  myTurtle.end_fill()

# left side
def drawSideOne(myTurtle):
  rhombusColor(myTurtle)
  myTurtle.left(150)
  myTurtle.color("orange")
  myTurtle.fillcolor("orange")
  myTurtle.begin_fill()
  makeRhombus(myTurtle)
  myTurtle.end_fill()

# right side
def drawSideTwo(myTurtle):
  drawSideOne(myTurtle)
  myTurtle.left(150)
  myTurtle.color("dark green")
  myTurtle.fillcolor("dark green")
  myTurtle.begin_fill()
  makeRhombus(myTurtle)
  myTurtle.end_fill()

# completes sequence / ties sides together
def makeCube(myTurtle):
  drawSideTwo(myTurtle)

def moveCube(myTurtle):
  myTurtle.right(60)
  myTurtle.forward(40)
  myTurtle.left(60)
  myTurtle.penup()
  myTurtle.forward(40)
  myTurtle.right(210)
  myTurtle.pendown()

# no loop bc only two times
def constructFirstRow(myTurtle):
  makeCube(myTurtle)
  moveCube(myTurtle)
  makeCube(myTurtle)
  moveCube(myTurtle)
  makeCube(myTurtle)
  moveCube(myTurtle)
  makeCube(myTurtle)
  moveCube(myTurtle)
  makeCube(myTurtle)
  moveCube(myTurtle)
  makeCube(myTurtle)
  moveCube(myTurtle)

def constructSecondRow(myTurtle):
  constructFirstRow(myTurtle)
  myTurtle.penup()
  myTurtle.goto(0,0)
  myTurtle.right(90)
  myTurtle.forward(60)
  myTurtle.left(90)
  myTurtle.backward(35)
  myTurtle.pendown()
  constructFirstRow(myTurtle)

def constructThirdRow(myTurtle):        
  constructSecondRow(myTurtle)
  myTurtle.penup()
  myTurtle.goto(0,0)
  myTurtle.right(90)
  myTurtle.forward(120)
  myTurtle.left(90)
  myTurtle.backward(70)
  myTurtle.pendown()
  constructFirstRow(myTurtle)

def constructFourthRow(myTurtle):
  constructThirdRow(myTurtle)
  myTurtle.penup()
  myTurtle.goto(0,0)
  myTurtle.right(90)
  myTurtle.forward(180)
  myTurtle.left(90)
  myTurtle.backward(105)
  myTurtle.pendown()
  constructFirstRow(myTurtle)

# code executes
lauren = turtle.Turtle()
constructFourthRow(lauren)

# aren't the colors nice Flax?
# retro ftw
\
