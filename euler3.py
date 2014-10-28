import math
val = 13195
for divider in range(2, int(math.sqrt(val))):
	if val % divider == 0:
		print divider

