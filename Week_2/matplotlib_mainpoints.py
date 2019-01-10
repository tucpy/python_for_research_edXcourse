'''
2.1
Learn how to create simple plots using matplotlib.pyplot
'''

import matplotlib.pyplot as plt
import numpy as np 
plt.plot([0,1,4,9,16]);
plt.show()

x = np.linspace(0,10,20)
y = x**2
print(x)
print(y)
plt.plot(x,y)


x = np.linspace(0,10,20)
y1 = x**2
y2 =x**1.5
plt.plot(x,y1,"bo-") # blue circle
plt.plot(x,y1,"bo-", linewidth=2, markersize =4)
plt.plot(x,y1,"bo-", linewidth=2, markersize =12)
plt.plot(x,y2,"gs-", linewidth=2, markersize =12) # green square

plt.plot([0,1,2],[0,1,4],"rd-") 

'''
2.2. Customizing your plot
Learn how to customize your plots by adding a legend, adjusting and labeling the axes, and saving your figures
- add legend: legend()
- adjust axes: axis()
- set axis labels: xlabel(), ylabel()
- save fig: savefig()

'''

x = np.linspace(0,10,20)
y1 = x**2
y2 =x**1.5
plt.plot(x,y1,"bo-", linewidth=2, markersize =12, label="First")
plt.plot(x,y2,"gs-", linewidth=2, markersize =12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$") #$ latex format?
#plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")

'''
2.3 Plotting using Logarithmic Axes
Learn how to create plots with logarithmic axes using semilogx, semilogy, and loglog
semilogx(): x scale
semilogy(): y scale
loglog(): both x and y scale
'''

x = np.logspace(-1,1,40)
y1 = x**2
y2 =x**1.5
plt.loglog(x,y1,"bo-", linewidth=2, markersize =12, label="First")
plt.loglog(x,y2,"gs-", linewidth=2, markersize =12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$") #$ latex format?
#plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("mylogplot.pdf")

x=np.logspace(0,1,10) 
y=x**2 
plt.loglog(x,y,"bo-")

'''
2.4 Generating Histograms
Learn how to generate histograms using plt.hist()
Learn how to create subplots using plt.subplot()
'''

# generate 1000 random values with normal distribution
import matplotlib.pyplot as plt
import numpy as np 
x = np.random.normal(size=1000)
plt.hist(x);
plt.hist(x, normed=True);
plt.hist(x, normed =True, bins=np.linspace(-5,5,21))

# gamma distribution
# subplot(row,column, number)
x = np.random.gamma(2,3,100000) 
plt.hist(x, bins = 30)
plt.hist(x, bins = 30, normed= True)
plt.hist(x, bins = 30, cumulative= True)
plt.hist(x, bins = 30, cumulative= True, normed=True, histtype="step")

# insert 4 histograms into 1 plot
plt.figure()
plt.subplot(221)
plt.hist(x, bins=30)
plt.subplot(222)
plt.hist(x, bins = 30, normed= True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative= True)
plt.subplot(224)
plt.hist(x, bins = 30, cumulative= True, normed=True, histtype="step")



#Which will have wider bins, np.linspace(-5,5,21) or np.linspace(-5,5,201) ?
x = np.linspace(5,-5,21)
y1 = x**2
plt.plot(x,y1,"bo-", linewidth=2, markersize =12, label="First")


x = np.linspace(5,-5,201)
y1 = x**2
plt.plot(x,y1,"bo-", linewidth=2, markersize =12, label="First")


plt.subplot(333)
plt.subplot(3, 3, 3)
