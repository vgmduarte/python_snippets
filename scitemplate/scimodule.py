import numpy as np
from scipy import integrate

def scifunc(arg, *args, **kwargs):
	print(arg, 'is a placed arg')
	print(args, 'is a tuple')
	print(kwargs, 'is a dictionary')
	return sum(args)

