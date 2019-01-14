'''
2.1 Simulating Randomness
Learn how to use random.choice to simulate random processes such as coin flips or the roll of a die
'''

import random
a = random.choice(["H", "T"])
b = random.choice([0, 1])
print(a)
print(b)
# random dice
c = random.choice([1,2,3,4,5,6])
print(c)
print(random.choice(range(1,7)))

'''
3 dice: 1st has 6 faces, 2nd has 8 faces, 3rd has 10 faces
1 dice is rolled at one time? chosing randomly from 3 dices
'''

choice = random.choice([range(1,7),range(1,9), range(1,11)])
print(choice)

ranchoice = random.choice(random.choice([range(1,7),range(1,9), range(1,11)]))
print(ranchoice)

# select random from 1 to 4
print(random.choice(list([1,2,3,4])))
random.choice(list((1,2,3,4))) # cast the tuple as the list

'''
2.2 Examples Involving Randomness
Further explore simulations of randomness and data visualization
'''

# plot a histogram of a dice 100 times
import random
import numpy as np
rolls = []
for i in range(100):
    rolls.append(random.choice(range(1,7)))

print(len(rolls)) # check number of object
print(rolls)
import matplotlib.pyplot as plt
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))


# plot a histogram of a dice 10000 repetition
import random
import numpy as np
rolls = []
for i in range(10000):
    rolls.append(random.choice(range(1,7)))

print(len(rolls)) # check number of object
print(rolls)
import matplotlib.pyplot as plt
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))
# histogram looks flat

# roll 10 independent dices, X1-X10
# Y = X1+ X1+...+X10
# plot histogram of Y, simulation 100 times

ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)

print(len(ys))
# check if min and max value within the range
min(ys)
max(ys)
plt.hist(ys)
# Central Limit Theorem-> sum of random varibles regarless of their distribution
# will follow a normal distribution of we increase sample size. For example: height of a population


'''
2.3 Using the NumPy random module
Explore how to use the numpy.random module to simulate randomness
'''
import numpy as np
# generate number from 0 to 1
print(np.random.random())
# 5 random number from 0 to 1
print(np.random.random(5))
# 2D array: 5 rows, 3 columns
print(np.random.random((5,3)))
# standard normal distribution
print(np.random.normal(0,1))
# array of 5 numbers
print(np.random.normal(0,1,5))
# 2D array: 2 rows, 5 columns
print(np.random.normal(0,1,(2,5)))

# 
np.random.randint(1,7)
#array of 10 rows, 3 columns
X = np.random.randint(1,7,(10,3))
print(X.shape)
#sum 
#np.sum?
np.sum(X) # sum all elements
np.sum(X, axis =0) # sum all rows
np.sum(X, axis =1) # sum all columns

Y = np.sum(X, axis=1)

X = np.random.randint(1,7,(100,10))
Y = np.sum(X, axis = 1)
plt.hist(Y)


X = np.random.randint(1,7,(10000,10))
Y = np.sum(X, axis = 1)
plt.hist(Y)


X = np.random.randint(1,7,(1000000,10))
Y = np.sum(X, axis = 1)
plt.hist(Y)
# this code is faster than standard Python code as Numpy was written in C?

print(np.random.random((5,2,3)))

# dimension is 10??
print(np.sum(np.random.randint(1,7,(100,10)), axis=0))

'''
2.4 Measuring time
Learn how to measure running time using the time module
Compare the running time of a simulation written in pure Python to one written using NumPy
'''
# large dataset, how long it might take to run the code?
import time

start_time = time.clock()
end_time = time.clock()
howlong = end_time - start_time

# Pure Python runtime
start_time = time.clock()
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
end_time = time.clock()
print(end_time - start_time)

#NumPy runtime
start_time = time.clock()
X = np.random.randint(1,7,(10000,10))
Y = np.sum(X, axis = 1)
end_time = time.clock()
print(end_time - start_time)

# time different between Pure Python and Numpy: 1597 times faster
13.229479000000001 / 0.008282000000001233

'''
2.5 Random Walks
Learn how to generate random walks using NumPy
'''
# generate displacement from normal distribution (0 to 1); 2 rows, 5 columns
np.random.normal(0,1,(2,5))
delta_X = np.random.normal(0,1,(2,5))
plt.plot(delta_X[0], delta_X[1], "go")

# cumulative sum in numpy over columns (axis=1)
X = np.cumsum(delta_X, axis = 1)
print(X)
print(delta_X)


delta_X = np.random.normal(0,1,(2,5))
X = np.cumsum(delta_X, axis = 1)
plt.plot(X[0], X[1], "ro-") # red circle connected with straight lines
plt.savefig("rw.pdf")
# concatenate numpy array
X_0 = np.array([[0], [0]])
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)


# Final plot with the random walk start at location (0,0)
X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0,1,(2,5))
X = np.cumsum(delta_X, axis = 1)
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)
plt.plot(X[0], X[1], "ro-")
plt.savefig("rw2.pdf")

# run 100 times
X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0,1,(2,100))
X = np.cumsum(delta_X, axis = 1)
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)
plt.plot(X[0], X[1], "ro-")
plt.savefig("rw3.pdf")

# run 10000 times
X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0,1,(2,100))
X = np.cumsum(delta_X, axis = 1)
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)
plt.plot(X[0], X[1], "ro-")
plt.savefig("rw4.pdf")