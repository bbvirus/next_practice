# Park Se-hun, Exercise3

def odd_cal(number):
	if (number>0 and number<10):
		return number+10
	elif (number>=10 and number<100):
		return number*0.1
	else:
		return False

number = input("input number : ")
result = odd_cal(number)

print "%.1f" %result