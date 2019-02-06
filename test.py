import csv
import numpy as np

data_path = 'C:/Users/A/Desktop/bike/hour.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data)
 
k = data[:,2]
#print(k)
th = np.count_nonzero(k)
#print(th)
#print(np.unique(k))
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('TOTAL SEASONS :')
#print("Frequency of unique values of the season array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,3]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('TOTAL YEARS : 2011(0) 2012(1)')
#print("Frequency of unique values of the year array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,4]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('TOTAL MONTHS : 1 to 12')
#print("Frequency of unique values of the month array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,5]
unique_elements, counts_elements = np.unique(k, return_counts=True)
ue,ce = np.unique(k,return_counts=True)
print('TIME OF THE DAY : 0 to 23')
#print("Frequency of unique values of the hour array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,6]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('DAY IS HOLIDAY : 0 or 1')
#print("Frequency of unique values of the holiday array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,7]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('DAY OF THE WEEK : 0 to 6')
#print("Frequency of unique values of the weekday array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,9]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('WEATHER : 1 2 3 4')
#print("Frequency of unique values of the weekday array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,-3]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('Casual Biker:')
#print("Frequency of unique values of the weekday array:")
print(np.asarray((unique_elements, counts_elements)))
k = data[:,-2]
unique_elements, counts_elements = np.unique(k, return_counts=True)
print('Regular Biker:')
#print("Frequency of unique values of the weekday array:")
print(np.asarray((unique_elements, counts_elements)))
#print(np.mean(counts_elements))
k = data[:,16]
tr = np.array(k).astype(np.int)
t = np.min(tr, axis=0)
m = np.max(tr, axis=0)
print("MINIMUM:",t,"MAXIMUM :",m)
print(tr)
#print(np.mean(counts_elements))

maxv = data[(data[:,2] == '1')]
print(maxv.shape)
maxv = maxv[:,16]
maxv = np.array(maxv).astype(np.int)
print(maxv)
max1 = np.max(maxv, axis=0)
min1 = np.min(maxv, axis=0)
print("MAXIMUM in Season 1 :",max1,"\nMINIMUN in Season 1 :",min1)
print("MEAN :",np.mean(maxv))

maxv = data[(data[:,2] == '2')]
print(maxv.shape)
maxv = maxv[:,16]
maxv = np.array(maxv).astype(np.int)
print(maxv)
max1 = np.max(maxv, axis=0)
min1 = np.min(maxv, axis=0)
print("MAXIMUM in Season 2 :",max1,"\nMINIMUN in Season 2 :",min1)
print("MEAN :",np.mean(maxv))

maxv = data[(data[:,2] == '3')]
print(maxv.shape)
maxv = maxv[:,16]
maxv = np.array(maxv).astype(np.int)
print(maxv)
max1 = np.max(maxv, axis=0)
min1 = np.min(maxv, axis=0)
print("MAXIMUM in Season 3 :",max1,"\nMINIMUN in Season 3 :",min1)
print("MEAN :",np.mean(maxv))

maxv = data[(data[:,2] == '4')]
print(maxv.shape)
maxv = maxv[:,16]
maxv = np.array(maxv).astype(np.int)
print(maxv)
max1 = np.max(maxv, axis=0)
min1 = np.min(maxv, axis=0)
print("MAXIMUM in Season 4 :",max1,"\nMINIMUN in Season 4 :",min1)
print("MEAN :",np.mean(maxv))

the = data[data[:,2] == '1']
gr = the[:,-3]
results = list(map(int, gr))
#print(results)
reg = the[:,-2]
reg = list(map(int, reg))
tot = the[:,-1]
tot = list(map(int, tot))

k = 0
r = 0
t = 0
for i in results:
    k += results[i]
    r += reg[i]
    t += tot[i]
print(the.shape)
print("Total Casual Booking in Season 1: ",k)
print("Total Registered Booking in Season 1: ",r)
print("Total Booking in Season 1: ",t)

the = data[data[:,2] == '2']
gr = the[:,-3]
results = list(map(int, gr))
#print(results)
reg = the[:,-2]
reg = list(map(int, reg))
tot = the[:,-1]
tot = list(map(int, tot))

k = 0
r = 0
t = 0
for i in results:
    k += results[i]
    r += reg[i]
    t += tot[i]
print(the.shape)
print("Total Casual Booking in Season 2: ",k)
print("Total Registered Booking in Season 2: ",r)
print("Total Booking in Season 2: ",t)

the = data[data[:,2] == '3']
gr = the[:,-3]
results = list(map(int, gr))
#print(results)
reg = the[:,-2]
reg = list(map(int, reg))
tot = the[:,-1]
tot = list(map(int, tot))

k = 0
r = 0
t = 0
for i in results:
    k += results[i]
    r += reg[i]
    t += tot[i]
print(the.shape)
print("Total Casual Booking in Season 3: ",k)
print("Total Registered Booking in Season 3: ",r)
print("Total Booking in Season 3: ",t)

the = data[data[:,2] == '4']
gr = the[:,-3]
results = list(map(int, gr))
#print(results)
reg = the[:,-2]
reg = list(map(int, reg))
tot = the[:,-1]
tot = list(map(int, tot))

k = 0
r = 0
t = 0
for i in results:
    k += results[i]
    r += reg[i]
    t += tot[i]
print(the.shape)
print("Total Casual Booking in Season 4: ",k)
print("Total Registered Booking in Season 4: ",r)
print("Total Booking in Season 4: ",t)

#graph
import matplotlib.pyplot as plt
label = ['Season 1', 'Season 2', 'Season 3', 'Season 4']
no = [ 131966, 353895, 782581, 497205]
index = np.arange(len(label))
plt.bar(index, no)
plt.xlabel('Seasons', fontsize=12)
plt.ylabel('Total Bookings', fontsize=12)
plt.xticks(index, label, fontsize=12, rotation=0)
plt.title('Bike Ride Seasonal Rush')
plt.show()

labels = ['Season 1', 'Season 2', 'Season 3', 'Season 4']
sizes = [111.11456859971712, 208.34406894987526, 236.01623665480426, 198.86885633270322]
explode = (0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
plt.title('Bike Ride Seasonal Rush')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

label = ue
no = ce
index = np.arange(len(label))
plt.bar(index, no)
plt.xlabel('Seasons', fontsize=12)
plt.ylabel('Total Bookings', fontsize=12)
plt.xticks(index, label, fontsize=12, rotation=0)
plt.title('Bike Ride Seasonal Rush')
plt.show()
print(ce)
