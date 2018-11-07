import numpy as np
import matplotlib.pyplot as plt

print('hello world')

'''
stefano is a beautiful boy 
'''

def circumference(r):
    out=np.pi*2*r
    return out

def area(r):
	''' this is your area function to calculate the area of a cirlce!'''
	out=np.pi*r*r
	return out

def plot_circle(radius):
	x = np.linspace(-2*radius, 2*radius, 100)
	y = np.sqrt(radius**2 - x**2)
	plt.plot(x, y)
	plt.plot(x, -y)
	plt.savefig(f'circle_{radius}.png')
