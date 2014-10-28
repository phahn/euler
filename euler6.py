import math

def sum(f, to):
	sum = 0
	for i in range(f, to + 1):
		sum += i
	return sum


result = 0
for i in range(1, 100):
	result += i * sum(i+1, 100)

print(result *2)


