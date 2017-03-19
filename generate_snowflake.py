import sys
import math
from Line_Point import *

'''
purpose
	write to stdout a snowflake with the specified size number of branches and colour.
preconditions
	size is positive, and num_sides is positive
'''

#
def start_line(line, scale, sides):
	# copy line
	new_line = Line(line.point0, line.point1)

	# translate to origin
	new_line.translate(-line.point0.x, -line.point0.y)

	# the new line needs to be rotated pi/sides degrees
	# if it has an even number of sides so that one of
	# the sides does not overlap the parent line.
	if sides % 2 == 0:
		new_line.rotate(math.pi / sides)
	new_line.scale(scale)

	# translate back
	new_line.translate(line.point0.x, line.point0.y)

	# translate tail to head of root
	new_line.translate(line.point1.x - line.point0.x, line.point1.y - line.point0.y)

	return new_line

#returns deep copy of line rotated the required amount 
#given the number of sides
def copy_and_rotate(line, sides):
	new_line = Line(line.point0, line.point1)
	new_line.translate(-line.point0.x, -line.point0.y)
	new_line.rotate(2 * math.pi / sides)
	new_line.translate(line.point0.x, line.point0.y)
	return new_line

#recursively draws the snowflake
def draw(line0, scale, sides, depth):
	if depth == 0:
		return
	line0 = start_line(line0, scale, sides)
	for i in range(sides):
		print 'line', line0
		draw(line0, scale, sides, depth-1)
		line0 = copy_and_rotate(line0, sides)

# ********** process the command line arguments
if len(sys.argv) != 4:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' sides scale depth'
	sys.exit(1)
try:
	sides = int(sys.argv[1])
	scale = float(sys.argv[2])
	depth = int(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' sides scale depth'
	sys.exit(2)
#arbitrary start line; may want to make user specified.
line0 = Line(Point(0.0,0.0),Point(0.0, 80.0))
for i in range(sides):
	print 'line', line0
	draw(line0, scale, sides, depth)
	line0 = copy_and_rotate(line0, sides)



