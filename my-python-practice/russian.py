#russian peasants algorithm
import time

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

def test_russian_algo(num1,num2):
	start_time = time.time()
	print (russian_algo(num1,num2))
	print ('Time it took to run the russian peasants algorithm in seconds: %f' % (time.time() - start_time))



test_russian_algo(16,24)
test_russian_algo(238,13)
test_russian_algo(357,16)







