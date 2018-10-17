#Ex3a
import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]
x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

#Ex3b
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
def rand():
    return random.uniform(0,1)

R = 1000
x = []
for i in range(R):
    point = rand()
    x.append(point)
print(x)

Y = []
for i in range (0,10): 
    Y.append(moving_window_average(x, i))

print(len(Y))

#Ex3c
# write your code here!
ranges = []
for i in Y:
    range = max(i) - min(i)
    ranges.append(range)
print(ranges)