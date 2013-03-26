# Park Se-hun, Exercise4

import math

def distance(x1, y1, x2, y2):
	dist_x = x2-x1
	dist_y = y2-y1
	return math.sqrt(dist_x**2 + dist_y**2)

dot1_x = input("input x-coordinate of Dot1 : ")
dot1_y = input("input y-coordinate of Dot1 : ")
dot2_x = input("input x-coordinate of Dot2 : ")
dot2_y = input("input y-coordinate of Dot2 : ")

result = distance(dot1_x, dot1_y, dot2_x, dot2_y)

print "Distance of Dot1 and Dot2 is %.2f" %result