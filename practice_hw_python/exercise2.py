# Park Se-hun, Exercise2

def absolute(number):
	if number >= 0 :
		return number
	else:
		return -number

number = input("input number : ")
result = absolute(number)

print "Number's absolute value is %.1f \n" %result