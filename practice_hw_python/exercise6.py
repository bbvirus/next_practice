# Park Se-hun, Exercise6

def check(string):
	if (string == string[::-1]):
		print "same!"
	else:
		print "different!"

input_str = raw_input("input : ")
check(input_str)