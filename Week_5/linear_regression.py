'''
1.1 Introduction to Statistical Learning
Learn the differences between supervised and unsupervised learning
Supervised Learning: (2 sets of data) inputs -> outputs
Unsupervised Learning: inputs only
Learn to distinguish regression (continuous outputs) and classification (categorical outputs)
Learn about the loss functions used in different settings
'''

#tbc 
'''
1.2 Generating Example Regression Data
Learn how to generate example regression data using Python
'''
import numpy as np 
import scipy.stats as ss 
import matplotlib.pyplot as plt 

n = 100
beta_0 = 5
beta_1 = 2

np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

plt.figure()
plt.plot(x,y, "o", ms=5)
xx = np.array([0, 10])
plt.plot(xx, beta_0 + beta_1 * xx)
plt.xlabel("x")
plt.ylabel("y")


# excercise
import numpy as np 
import scipy.stats as ss 
import matplotlib.pyplot as plt 
n = 100 
beta_0 = 5 
beta_1 = 2 
np.random.seed(1) 
x = 10 * ss.uniform.rvs(size=n) 
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale = 1, size = n) 
print(np.mean(x))
print(np.mean(y))


'''
1.3 Simple Linear Regression
Learn the basics of simple linear regression
'''



# excercise
def compute_rss(y_estimate, y): 
  return sum(np.power(y-y_estimate, 2)) 
def estimate_y(x, b_0, b_1): 
  return b_0 + b_1 * x 
rss = compute_rss(estimate_y(x, beta_0, beta_1), y) 
print(rss)


'''
1.4 Least Squares Estimation in Code
Learn how to use Python to compute the least squares estimate
Learn how to use Python to estimate parameter values that minimize the residual sum of squares (RSS) criterion
'''
rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
    rss.append(np.sum((y - beta_0 - slope * x)**2))

ind_min = np.argmin(rss)
print("Estimate for the slope:", slopes[ind_min])


plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")


'''
1.5 Simple Linear Regression in Code
Learn how to fit a simple linear regression model in Python
'''
import statsmodels.api as sm
mod = sm.OLS(y,x)
est = mod.fit()
print(est.summary())


X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary())



'''
1.6 Multiple Linear Regression
Learn the basics of multiple linear regression
'''






'''
1.7 scikit-learn for Linear Regression
Learn how to generate data from a simple model
Learn how to fit a linear regression model using the scikit-learn library
Learn how to evaluate the fit of a model by determining the R2 statistic 
'''




'''
1.8 Assessing Model Accuracy
Learn how to compute the mean squared error (MSE) to evaluate the performance of a regression model
Learn how to separate data into training and test datasets
Learn why both underfitting and overfitting can be problematic
'''