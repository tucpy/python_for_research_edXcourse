#Ex2a
import math
x = (math.pi / 4)
print(x)

#Ex2b
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
    return random.uniform(-1.0,1.0)
    

print(rand())

#Ex2c
import math

def distance(x, y):
    diff1 = (y[0] - x[0]) * (y[0] - x[0])
    diff2 = (y[1] - x[1]) * (y[1] - x[1])
    dist = math.sqrt(diff1 + diff2)
    return dist
    
x = (0,0)
y = (1,1)

print(distance(x,y))

#Ex2d
import random, math

random.seed(1)

    
def in_circle(x, origin = [0]*2):
    if distance(origin, x) < 1:
        return True
    else:
        return False

x = (1,1)
origin = (0,0)
print(in_circle(x, origin))

#Ex2e
R = 10000
x = []
inside = []
origin = [0,0]
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
for j in x:
    inside.append(in_circle(origin,j))

print(sum(inside) / R)

#Ex2f
# write your code here!
diff = ((sum(inside)/R) - (math.pi/4))
print(diff)