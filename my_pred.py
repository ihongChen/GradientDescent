# my own batch gradient descent test for a hand make y = 3x + randn 
import random
import math
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array(range(0, 100))
y1 = np.array([3*x_i + random.randint(-3,3) for x_i in x1])
data_trained = zip(x1,y1)

x0 = np.array([1]*len(x1)) # unit vector with len(x1)
theta_guess = [0,10]
theta = theta_guess
h_theta = x1*theta[1] + x0*theta[0]
alpha = 10**-7 
tol = 10-1
i = 0
while tol>10**-5:
	h_theta = x1*theta[1] + x0*theta[0]
	theta_iter0 = theta[0] + alpha*(sum((y1-h_theta)*x0))
	theta_iter1 = theta[1] + alpha*(sum((y1-h_theta)*x1))
	i+=1
	tol = math.sqrt((theta[0]-theta_iter0)**2 + (theta[1]-theta_iter1)**2)
	print (i,tol)
	theta = [theta_iter0,theta_iter1]

y_predict = theta[0]*x0 + theta[1]*x1

plt.scatter(x1,y1)
plt.plot(x1,y_predict,'r')
plt.legend(['trained data','predict'])
plt.show()
