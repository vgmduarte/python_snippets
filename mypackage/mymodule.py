import numpy as np

def myfunc(arg, *args, **kwargs):
	print(arg, 'is a placed arg')
	print(args, 'is a tuple')
	print(kwargs, 'is a dictionary')
	return np.array(list(args))
