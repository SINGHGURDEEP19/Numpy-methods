import pandas as pd
import numpy as np
df = pd.read_csv("/Users/gurdeepsingh/Downloads/forestfires.csv")
print(df.head())
print(df.tail())
forestfires = np.genfromtxt('/Users/gurdeepsingh/Downloads/forestfires.csv', delimiter=',')
temp = forestfires[:,8]
mean_temp = np.nanmean(temp)
std_temp = np.nanstd(temp)
max_temp = np.nanmax(temp)
min_temp = np.nanmin(temp)
print("The average of the temp column is: ",mean_temp)
print("The standard deviation of the temp column is: ",std_temp)
print("The minimum temperature in the temp column is:",min_temp)
print("The maximun temperature in the temp column is:",max_temp)
wind = forestfires[:,10]
print("The data type of values in wind column is: ",wind.dtype)
print("The size of wind column is: ",wind.size)
print("The itemsize of wind column is:",wind.itemsize)
month = forestfires[:,2]
array = np.arange(len(month)).reshape(37,14)
print(array.shape)
print(array)