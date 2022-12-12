from tkinter import *
from math import *
from numpy import *


def getABCvalues(func):
	func = list(func)
	abc = []

	# REMOVING "y = " OR "f(x) = "
	# determining if the function begins with "y = "
	if func[0:4] == ['y', ' ', '=', ' ']:
		for i in range(4):
			func.pop(0)
	# determining if the function begins with "f(x) = "
	elif func[0:7] == ['f', '(', 'x', ')', ' ', '=', ' ']: 
		for i in range(7):
			func.pop(0)

	# REMOVING SPACES 
	# finding the number of spaces
	numSpaces = 0
	for i in range(len(func)):
		if func[i] == " ":
			numSpaces += 1
	# deleting the spaces
	for i in range(len(func) - numSpaces ):
		if func[i] == " ":
			func.pop(i)
	

	# EXTRACTING A, B, AND C VALUES
	# extracting the A value
	if not '^' in func: # if "^" not in list 
		abc.append(0)
	else:
		find = func.index("^")
		find -= 1 # ax^2 's x index
		if func[find-1] == "-": # -x^2
			abc.append(-1)
		elif func[0] == "x": # x^2
			abc.append(1)
		else: #ax^2 or -ax^2
			val = func[0:find]
			newVal = ""
			for i in range(len(val)):
				newVal += val[i]
			newVal = int(newVal)
			abc.append(newVal)
		for i in range(find+3): # removes ax^2 section, keeping the next operator (+/-)
			func.pop(0)

	# extracting the B value
	if not 'x' in func or not func: # if "x" is not in list or if list is empty
		abc.append(0)
	else:
		find = func.index("x") # bx 's x index  
		if func[find-1] == "-" and func[1] == "x": # -x
			abc.append(-1)
		elif func[find-1] == "+" and func[1] == "x": # +x
			abc.append(1)
		else: # +bx or bx or -bx
			if func[0] == "+": # +bx
				val = func[1:find]
				newVal = ""
				for i in range(len(val)):
					newVal += val[i]
				newVal = int(newVal)
				abc.append(newVal)
			else: # +bx or bx
				val = func[0:find]
				newVal = ""
				for i in range(len(val)):
					newVal += val[i]
				newVal = int(newVal)
				abc.append(newVal)
		for i in range(find+1): # removes ax^2 section, keeping the next operator (+/-)
			func.pop(0)

	# extracting the c value
	if not func: # if list is empty
		abc.append(0)
	else:
		if func[0] == "-": # -c
			val = func[0:]
			newVal = ""
			for i in range(len(val)):
				newVal += val[i]
			newVal = int(newVal)
			abc.append(newVal)
		elif func[0] == "+": # +c
			val = func[1:]
			newVal = ""
			for i in range(len(val)):
				newVal += val[i]
			newVal = int(newVal)
			abc.append(newVal)
		else: # c 
			val = func[0:]
			newVal = ""
			for i in range(len(val)):
				newVal += val[i]
			newVal = int(newVal)
			abc.append(newVal)
	return abc


def TKcanvas(xDist, yDist):
	tk = Tk()
	global s
	s = Canvas(tk, width=xDist, height=yDist, background="white")
	s.pack()

	
def drawAxes(xMin, xMax, xIncrement, yMin, yMax, yIncrement):
	xDist = abs(xMax - xMin)
	yDist = abs(yMax - yMin)
	TKcanvas(xDist, yDist)
	xMid = xDist/2 - ((xMax + xMin)/2)
	yMid = yDist/2 + ((yMax + yMin)/2)
	
	s.create_line(0, yMid, xDist, yMid, width="3") # x-axis
	s.create_line(xMid, 0, xMid, yDist, width="3") # y-axis

	for i in arange(xMin, xDist, xIncrement): # x grid (vertical lines)
		i -= xMin
		s.create_line(xMid+i, 0, xMid+i, yDist, width="1", fill="aqua") # grid lines in pos
		s.create_line(xMid-i, 0, xMid-i, yDist, width="1", fill="aqua") # grid lines in neg
		
	for i in arange(yMin, yDist, yIncrement): # y grid (horizontal lines)
		s.create_line(0, yMid-i, xDist, yMid-i, width="1", fill="aqua") # grid lines in pos
		s.create_line(0, yMid+i, xDist, yMid+i, width="1", fill="aqua") # grid lines in neg

	j = 0 # counts how many times we have looped
	for i in arange(0, xDist+1, xIncrement): # x tick marks
		s.create_line(i, yMid+10, i, yMid-10) # tick
		j += 1
		if i % xIncrement == 0: 
			if j % 2 == 0:
				s.create_text(i, yMid-20, text=str(i+xMin)) # text above
			else: 
				s.create_text(i, yMid+20, text=str(i+xMin)) # text below

	j = 0 # counts how many times we have looped
	for i in arange(0, yDist+1, yIncrement): # y tick marks 
		s.create_line(xMid+10, i, xMid-10, i) #tick
		j += 1
		if i % yIncrement == 0: 
			if j % 2 == 0:
				s.create_text(xMid+20, i, text=str(yDist-i+yMin)) # text right
			else:
				s.create_text(xMid-20, i, text=str(yDist-i+yMin)) # text right
			
	
def makeTableOfValues(xMin, xMax, numPoints, abc):
	x = []
	y = []
	dis = abs(xMax - xMin) #dis between xMin & xMax
	disBetween = (dis/numPoints) #dis between each point
	
	for i in range(numPoints+1):
		x.append(xMin + i*disBetween)
		y.append(-1*(abc[0]*x[i]**2 + abc[1]*x[i] + abc[2]))
	
	return [x, y]

	
def plotPoints(xValues, yValues, xMin, xMax, xIncrement, yMin, yMax, yIncrement, numPoints, color):
	xDist = abs(xMax - xMin)
	yDist = abs(yMax - yMin)
	xMid = xDist/2 - ((xMax + xMin)/2)
	yMid = yDist/2 + ((yMax + yMin)/2)
	for i in range(numPoints):
		s.create_line(
			xValues[i]+xMid, 
			yValues[i]+yMid,
			xValues[i+1]+xMid, 			
			yValues[i+1]+yMid, 
			fill=color, width=4
		)


def graph(func, xMin, xMax, xIncrement, yMin, yMax, yIncrement, numPoints, color):
	print(func, xMin, xMax, xIncrement, yMin, yMax, yIncrement, numPoints, color)
	ABC = getABCvalues(func)
	drawAxes(xMin, xMax, xIncrement, yMin, yMax, yIncrement)
	table = makeTableOfValues(xMin, xMax, numPoints, ABC)
	xValues = table[0]
	yValues = table[1]
	plotPoints(xValues, yValues, xMin, xMax, xIncrement, yMin, yMax, yIncrement, numPoints, color)
