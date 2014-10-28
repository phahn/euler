def isPalindrom(number):
	stringNumber = str(number)
	for i in range(0, len(stringNumber) / 2):
		if stringNumber[i] != stringNumber[(len(stringNumber) - 1) - i]:
			return False
	return True

#for i in reversed(range (1, 999 * 999)):
#	if isPalindrom(i):
#		print i
		

