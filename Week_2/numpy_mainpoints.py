'''
2.1 Learn how to import NumPy
Learn how to create simple NumPy arrays, including vectors and matrices of zeros and ones
'''

'''
NumPy is Python module for scientific computation
NumPy Arrays: fixed size, contain float number, 2 dimensional table
'''
import numpy as np

zero_vector = np.zeros(5) # 5 elements in the vector, all are 0.0
zero_matrix = np.zeros((5,3)) # 5 rows, 3 columns

print(zero_vector)
print(zero_matrix)

print(np.ones(2)) # array of 1 element
# create empty array
print(np.empty(10)) # gabbage values from memory, haha, allocate space for array but not initialize it

#one dimensional array
x = np.array([1,2,3])
y = np.array([2,4,6])

A = np.array([[1,3], [5,9]]) # embedded 2 list in the array
print(A)
#transpose array
print(A.transpose())

'''
2.2 Learn how to slice NumPy arrays
'''

X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[2,4,6],[8,10,12]])

# slide x array from 0 to 1(not until index 2)
print(x[0:2])

z = x + y # combine value of 2 array if size are the same
print(z)

# slide 2 dimensional array, 1st column 
print(X[:,1])
print(Y[:,1])
print(X[:,1] + Y[:,1])

# 1st row of array
print(X[1,:])
print(X[1])

# Concatenate 2 list 
aa = [2,4] + [6,8]
print(aa)
bb = np.array([2,4]) + np.array([6,8]) # add values of 2 array
print(bb)

'''
2.3 Learn how to index NumPy arrays with other arrays or sequence-like objects
Learn an important distinction between slicing an array and indexing an array
'''

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1 
print(z1)
print(z2)

# index
ind = [0,2,3] # list of indexes
print(z1[ind])

# you can index NumPy array either by using other lists or other NumPy array
ind1 = np.array([0,2,3])
print(z1[ind1])

# construct a Boolean array (logical array)
z1 = np.array([1,3,5,7,9])

print(z1 > 6)

print(z1[z1 > 6])

print(z2[z1 > 6])

ind = z1 > 6
z1[ind]
z2[ind]

w = z1[0:3]
print(w)
# modify 1st element of w, also change in z1 arrat
w[0] = 3
print(w)
print(z1)

# not modify original z1 array, because w is a copy of original data
ind = np.array([0,1,2])
w = z1[ind]
w[0] = 5
print(w)
print(z1)

'''
2.4 Building and Examining Numpy array
Learn how to construct NumPy arrays using np.linspace() and np.logspace
Learn how to check the shape and size of an array
Learn how to determine whether the elements of an array fulfill a logical condition using np.any() and np.all()
'''

# construct array with fixed start and end
np.linspace(0,100,0) # 10 elements in array, uniformly space between each element

np.logspace(1,2,10) # start from 10 to 100, log10(10) = 1, log10(100) = 2

# array of 10 logarithmically spaced elements (100, 250)
t = np.logspace(np.log10(250), np.log10(500), 10)
print (t)


# Check shape of an array
X = np.array([[1,2,3],[4,5,6]])
print(X.shape) # 2 rows, 3 columns
print(X.size) # 6 elements in array

x = np.random.random(10)
print(np.any(x > 0.9)) # check if any element > 0.09
print(np.all(x >= 0.1)) # check if all elements > 0.1

print(x)

# check if x is prime number
x=20 
not np.any([x%i == 0 for i in range(2, x)])


