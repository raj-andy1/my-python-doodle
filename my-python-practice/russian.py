#russian peasants algorithm


def russian_algo(num1, num2):
	table = {}
	total = 0
	while num1 != 0:
		table[num1] = num2
		num1 = num1//2
		num2 = num2*2
	for key in list(table):
		if (key % 2) == 0:
			del table[key]
	return (sum(table.values()))
	exit(0)

print (russian_algo(24,16))
print (russian_algo(16,24))
print (russian_algo(238,13))
print (russian_algo(357,16))






