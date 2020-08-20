import numpy as np
from scipy import integrate

def scifunc(arg, *args, **kwargs):
	print(arg, 'is a placed arg')
	print(*args, 'are optional args')
	print(**kwargs, 'are optional args with names')
	return sum(*args)

