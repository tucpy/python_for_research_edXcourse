'''
2.1 Learn how GPS data can be used to track bird migration patterns
'''

'''
track 3 birds, csv file contain latitude, longtitude, altitude and time stamps
'''

import pandas as pd  
#read csv file
birddata = pd.read_csv("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_4/bird_tracking.csv")

birddata.info()

print(birddata.head())

'''
2.2 Learn how to plot latitude and longitude on a simple 2D plot
'''
import matplotlib.pyplot as plt
import numpy as np  

ix = birddata.bird_name =="Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]

plt.figure(figsize = (7,7))

plt.plot(x,y,".")

# plot 3 birds on the same plot
bird_names = pd.unique(birddata.bird_name)

plt.figure(figsize = (7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,".", label =bird_name)
plt.xlabel("Longtitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")

'''
2.3 Examining Flight Speed
Learn how to examine 2D flight speed of the birds
Learn how to deal with data entries that are not numeric
'''
ix = birddata.bird_name =="Eric"
speed = birddata.speed_2d[ix]
#plt.hist(speed)
# check if there is non number value in speed
speed[:10]
plt.hist(speed[:10])

print(np.isnan(speed))

np.isnan(speed).any() # check if there is at least 1 NA in our array

np.sum(np.isnan(speed)) # 85 of them are NA?

# find position of NA elements in the array
ind = np.isnan(speed)

print(ind)

# take the complement of ind vector (turn true to false and vice versa)
#~ind

# plot the new vector - orginal code
ix = birddata.bird_name =="Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind]) # only include if ind is not equal to True
plt.savefig("hist.pdf")


# plot the new vector - modified
# How fast Eric flies
plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name=="Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed = True) # only include if ind is not equal to True
plt.xlabel("2D speed (m/s")
plt.ylabel("Frequency");


#using Pandas to draw so dont need to deal with NAs 
birddata.speed_2d.plot(kind='hist', range=[0,30])
plt.xlabel("2D speed");
plt.savefig("pd_hist.pdf")

'''
2.4 Using Datetime
Learn how deal with timestamped data using datetime
Learn how to measure elapsed time
'''

birddata.columns

birddata.date_time[0:3]

import datetime
datetime.datetime.today()
time_1 = datetime.datetime.today()
time_2 = datetime.datetime.today()
time_2 - time_1 # compute how much time has passed

date_str = birddata.date_time[0]
type(date_str)
date_str
date_str[:-3] # exclude 3 last chars of time

# format datetime, %H: hour in 24hour timestamp
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []

for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime \
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

# create new column using pandas
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
birddata.head()

birddata.timestamp[4] - birddata.timestamp[3] 

times = birddata.timestamp[birddata.bird_name =="Eric"]
elapsed_time = [time - time[0] for time in times]

elapsed_time[0]
elapsed_time[1000]

# how many days have passed?
elapsed_time[1000] / datetime.timedelta(days=1)
# how many hours have passed?
elapsed_time[1000] / datetime.timedelta(hours=1)

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)");
plt.savefig("timeplot.pdf")




