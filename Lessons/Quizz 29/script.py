import matplotlib.pyplot as plt
import numpy as np
import requests

url = "http://192.168.6.142/readings"
r = requests.get(url)
data = r.json()
temp = []
for sample in data:
    if sample["sensor_id"] == 1:
        temp.append(sample["value"])
print(len(temp))

#Every 12 samples calculate the mean and std
number_samples_per_hour = 12
mean_per_hour = []
std_per_hour = []
x = []
for i in range(0, len(temp), number_samples_per_hour):
    mean_per_hour.append(np.mean(temp[i:i+number_samples_per_hour]))
    std_per_hour.append(np.std(temp[i:i+number_samples_per_hour]))

    x.append(i)

fig=plt.figure(figsize=(9,6))
plt.subplot(2,1,1)
plt.plot(temp)
plt.subplot(2,1,2)
plt.plot(x,mean_per_hour)
plt.subplot(2,1,3)
#plot topperhour and minperhour
plt.plot(x,std_per_hour)
plt.show()