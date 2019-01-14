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

import pandas as pd  
#read csv file
birddata = pd.read_csv("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_4/bird_tracking.csv")
birddata.columns

birddata.date_time[0:3]
import matplotlib.pyplot as plt
import numpy as np  
import datetime
datetime.datetime.today()
time_1 = datetime.datetime.today()
time_2 = datetime.datetime.today()
time_2 - time_1 # compute how much time has passed

date_str = birddata.date_time[0]
type(date_str)
date_str
date_str[:-3] # exclude 3 last chars of time(+00) '2013-08-15 00:18:08+00'

# format datetime, %H: hour in 24hour timestamp
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []

for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime \
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

# create new column using pandas
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
print(birddata.head())

birddata.timestamp[4] - birddata.timestamp[3] 

times = birddata.timestamp[birddata.bird_name =="Eric"]
elapsed_time = [time - times[0] for time in times]

print(elapsed_time[0])
print(elapsed_time[1000])

# how many days have passed?
elapsed_time[1000] / datetime.timedelta(days=1)
# how many hours have passed?
elapsed_time[1000] / datetime.timedelta(hours=1)

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)")
plt.savefig("timeplot.pdf")


'''
2.5 Calculating Daily Mean Speed
Learn how to calculate and plot daily mean speed
loop over all the timestamp, if not hitting next day yet,

'''
data = birddata[birddata.bird_name=="Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)


next_day = 1
inds = []
daily_mean_speed = []
#elapsed_days return a tuple with index and time
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day +=1
        inds =[]

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms.pdf")

# check data from bird Sanne
data_sanne = birddata[birddata.bird_name=="Sanne"]
data_sanne.date_time.head()

'''
2.6 Using the Cartopy Library
Learn how to download and install Cartopy, a library that provides cartographic tools for Python
Learn how to use Cartopy to plot data on a cartographic projection
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection =proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))

for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.', transform = ccrs.Geodetic(), label=name)

plt.legend(loc="upper left")
plt.savefig("map.pdf")

#surimpose a map on top of the graph
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection =proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')


for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.', transform = ccrs.Geodetic(), label=name)

plt.legend(loc="upper left")
plt.savefig("map_new.pdf")


