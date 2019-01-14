'''
1.1 Getting started with Pandas
Learn how to use Pandas Series
Learn how to use Pandas DataFrames
Scotch whiskies based on their flavor characteristic
'''

# Pandas - 2 data structure: Series(1 demensional) and Data Frames (2 dimensional)

import pandas as pd

########
# Series
########
# create object x contain 4 numbers
x = pd.Series([6,3,8,6])
print(x)
#define indexes corresponding to value
x = pd.Series([6,3,8,6], index=["q","w","e","r"])
print(x)

print(x["w"])

print(x[["r","w"]])
#define a dictionary
age = {"Tim":29,"Jim":31,"Pam":27,"Sam":35}

x = pd.Series(age)
print(x)

########
# Data Frame
########

data ={'name': ['Tim', 'Jim', 'Pam', 'Sam'],
        'age': [29, 31, 27, 35],
        'ZIP': ['02115','02130','67700','00100']}

# construct a Data Frames from dictionary
x = pd.DataFrame(data, columns = ["name","age","ZIP"])
print(x)

# retrieve a column
print(x["name"])
print(x.name)

# re-index a Series or a Data Frame object
x = pd.Series([6,3,8,6], index=["q","w","e","r"])
print(x.index)
sorted(x.index)

x.reindex(sorted(x.index))

# add 2 Series object
x = pd.Series([6,3,8,6], index=["q","w","e","r"])
y = pd.Series([7,3,5,2], index=["e","q","r","t"])

print(x + y) # if indexes were different -> NAN in t and w
'''
Index(['q', 'w', 'e', 'r'], dtype='object')
e    15.0
q     9.0
r    11.0
t     NaN
w     NaN
'''
# Pandas can be used to summarize data, compute correlations,
# hanle missing data, use hierachical indexing...


'''
1.2 Loading and inspecting data
Learn how to load a CSV file using Pandas
Learn how to view the beginning and end of a Pandas DataFrame
Learn how to index a Pandas DataFrame by location
'''

import numpy as np 
import pandas as pd 

whisky = pd.read_csv("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_4/whiskies.txt")

whisky["Region"] = pd.read_csv("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_4/regions.txt")

whisky.head()
whisky.tail()

whisky.iloc[0:10] # row 0 to 10

whisky.iloc[5:10, 0:5] # row 5 to 10 and column 0 to 5

whisky.columns

flavors = whisky.iloc[:, 2:14] # include column 13

print(flavors)

'''
1.3 Exploring Correlations
Learn how to explore correlations in your data
Learn how to plot a correlation matrix
'''
# Pearson correlation for linear data
corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

import matplotlib.pyplot as plt 
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

#heavy body is associated with smokiness
#a floral flavor is the opposite of full body

'''
Whiskies are made by different distilleries,
so this is correlation bt different distilleries in terms of the flavor 
profiles of the whiskies that they produce
'''
corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.savefig("corr_whisky.pdf")

#90 by 90 correlation matrix, but we only has 86x86
# modify the axis to 86 by "tight"
corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky_tight.pdf")

'''
1.4 Clustering Whiskies by Flavor Profile
Learn how to use spectral co-clustering to cluster whiskies based on their flavor profiles
'''
# using spectral co-clustering method from scikit-learn machine learning module
# goal is to find a sets of words and sets of documents that often go together
# each cluster consist of both words and documents

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)

print(model.rows_)

np.sum(model.rows_, axis = 1)
np.sum(model.rows_, axis = 0)

# 6 clusters (from 0 to 5)
print(model.row_labels_)

'''
1.5 Comparing Correlation Matrices
Learn how to compare correlation matrices
'''
whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)

whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())

correlations = np.array(correlations)


plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")



import pandas as pd 
data = pd.Series([1,2,3,4])
print(data)
data = data.ix[[3,0,1,2]]
print(data)
print(data[0])


data = pd.Series([1,2,3,4])
print(data)
data = data.ix[[3,0,1,2]]
print(data)
data = data.reset_index(drop=True)
print(data)
print(data[0])