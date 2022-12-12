from GraphingCalculatorToolbox import *
from time import *
from os import *


# user input
func = input("\nfunction? (in the form of \"ax^2 + bx + c\" or \"y = ...\" or \"f(x) = ...\", use integers as coefficients)\n")
xMin = int(input("\nx axis minimum value? (use integers)\n"))
xMax = int(input("\nx axis maxmum value? (use integers)\n"))
xIncrement = int(input("\nx axis increment value? (use integers)\n"))
yMin = int(input("\ny axis minimum value? (use integers)\n"))
yMax = int(input("\ny axis maxmum value? (use integers)\n"))
yIncrement = int(input("\ny axis increment value? (use integers)\n"))
numPoints = int(input("\nnumber of points? (use integers)\n"))
color = input("\ncolor of function?\n")


# loading
char = ["/", "-", "\\", "|"] 
for i in range(5):
	for j in range(4):
		print(f"Generating graph of function {func} ... {char[j]}")
		sleep(.1)
		system('clear')
system('clear')


graph(func, xMin, xMax, xIncrement, yMin, yMax, yIncrement, numPoints, color)
print(f"Finished! \n\n\n=====INFO=====\nfunction: {func}\nxMin: {xMin}\nxMax: {xMax}\nxIncrement: {xIncrement}\nyMin: {yMin}\nyMax: {yMax}\nyIncrement: {yIncrement}\nnumPoints: {numPoints}\ncolor: {color}\n")
