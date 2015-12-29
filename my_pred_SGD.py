# my own stochastic gradient descent test for a hand make y = 3x + randn equation
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def in_random_order(data):
	'''generator that returns the elements of data in random set'''
	indexes = [i for i,_ in enumerate(data)]
	random.shuffle(data)
	for i in indexes:
		yield data[i]

x1 = np.array(range(0, 100))
y = np.array([3*x_i + random.randint(-3,3) for x_i in x1])
data = zip(x1,y)
theta0 = [10,100]

theta = theta0
alpha = 10**-5
min_theta,min_value = None, float("inf")
iter_no = 0

while iter_no <2000:
	for xi,yi in in_random_order(data):
		h_theta = theta[0] + xi*theta[1]
		theta_iter0 = theta[0] + alpha*(yi-h_theta)
		theta_iter1 = theta[1] + alpha*(yi-h_theta)*xi
		theta = [theta_iter0,theta_iter1]
	
	print iter_no,theta
	iter_no +=1
	

y_predict = theta[0] + theta[1]*x1

plt.scatter(x1,y)
plt.plot(x1,y_predict)
plt.legend(['trained data','predict'])
plt.title('Stochastic Gradient Descent')
plt.show()
