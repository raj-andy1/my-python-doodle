#args and kwargs

'''
def F(*args, **kwargs):
	for arg in args:
		print (arg)
	print (kwargs)
'''

def F(hair,eyes='Green'):
	print (hair, eyes)

hair_color = 'black'

F(hair_color)
F(hair_color, eyes = 'blue')
