import math
import sys
import random
from Line_Point import *


'''
purpose
	convert the lines in stdin to a list of Line objects
	return the list
preconditions
	file_object is a reference to a readable file containing legal lines
'''
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Point(float(line_object[1]), float(line_object[2]))
		point1 = Point(float(line_object[3]), float(line_object[4]))
		line_object = Line(point0, point1)

		line_objects.append(line_object)
	
	return line_objects


file = open(sys.argv[1])

line_list = load_line_file(file)

for line in line_list:
	line.scale(0.1) # change 0.1 to command line input maybe?
for i in range(5): # change 5 to command line input
	x = float(random.randrange(-200,200)) # could calculate actual range
	y = float(random.randrange(-200,200))
	for line in line_list:
		line.translate(x,y)
		print 'line', line
		line.translate(-x,-y)




