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

# tbc later

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
# this code is faster than standard Python code as Numpy was written in C 

print(np.random.random((5,2,3)))

# dimension is 10??
print(np.sum(np.random.randint(1,7,(100,10)), axis=0))

