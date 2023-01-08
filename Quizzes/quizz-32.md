## Not done
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

url = 'http://192.168.6.142/readings'
r = requests.get(url)
data = r.json()
readings = data["readings"][0]
print(len(readings))

temp9 = []
temp10 = []
for sample in readings:
  if sample["sensor_id"]==9:
    temp9.append(int(sample["value"]))
  if sample["sensor_id"]==10:
    temp10.append(int(sample["value"]))

temp_short9 = []
for i in range(0, len(temp9), 12):
    temp_short9.append(sum(temp9[i:i+12])/12)
x9 = []
for i in range(len(temp_short9)):
    x9.append(i*12)


temp_short10 = []
for i in range(0, len(temp10), 12):
    temp_short10.append(sum(temp10[i:i+12])/12)
x10 = []
for i in range(len(temp_short10)):
    x10.append(i*12)

for i in range(len(temp_short9)):
    diff = temp_short9[i] - temp_short10[i]
xdiff = []
for i in range(len(diff)):
    xdiff.append(i)

print(temp_short9)
print(temp_short10)

plt.subplot(1, 3, 1)
plt.plot(x9, temp_short9, label='Sensor 9')
plt.subplot(1, 3, 2)
plt.plot(x10, temp_short10, label='Sensor 10')
plt.subplot(1, 3, 3)
plt.plot(xdiff, diff, label='Difference')

plt.show()
