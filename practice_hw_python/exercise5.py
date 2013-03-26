# Park Se-hun, Exercise5

string = "next people"

def num_of_e(string):
	count = 0
	for e in string:
		if (e == 'e'):
			count += 1
	return count

result = num_of_e(string)

print '%d' %result