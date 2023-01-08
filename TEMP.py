import requests
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
plt.style.use('dark_background')

req = requests.get("http://192.168.6.142/readings")
data = req.json()
readings = data["readings"][0]
sensor_id_1 = 5
sensor_id_2 = 4
sensor_id_3 = 4
sensor_id_4 = 5
window = 12
window *= 4 # there is for sensors

samples = []
temp = []

for sample in readings:
    if sample["sensor_id"] == sensor_id_1 or sample["sensor_id"] == sensor_id_2 or sample["sensor_id"] == sensor_id_3 or sample["sensor_id"] == sensor_id_4:
        temp.append(sample["value"])

for i in range(0, len(temp), window):
    segment_mean = sum(temp[i:i+window])/window
    samples.append(segment_mean)


#line of best fit
z = np.polyfit(range(len(samples)), samples, 1)

y = []
for i in range(len(samples)):
    y.append(i*(window/4))

#polyfit of 3th degree
p = np.poly1d(np.polyfit(y, samples, 3))

# prep the graphs
fig=plt.figure(figsize=(12,12))
gs = GridSpec(4, 4, figure=fig)
ax = fig.add_subplot(gs[:,0:3])


# add title and axis names
plt.title('Humidity Predictions')
plt.xlabel('Smooth measurement number')
plt.ylabel('Humidity (%)')
# line of best fit formula
# 3th degree polynomial formula
plt.text(119, 25, """5 % of uncertainety""", fontsize=10)
plt.errorbar(y , samples, yerr=2, fmt='o', color="lightblue")
plt.axhline(y=20, color='r', linestyle='-')
plt.text(200, 19, """20 is the minimum value""", fontsize=10, color='r')


plt.grid()
plt.scatter(y, samples)

ax = fig.add_subplot(gs[0,3])
plt.scatter(y, samples)
plt.plot(y, np.polyval(z, range(len(samples))))
plt.title('Linear Regression'+str("y=%.6fx+(%.6f)"%(z[0],z[1])))

ax = fig.add_subplot(gs[1,3])
# quadratic formula
p = np.poly1d(np.polyfit(y, samples, 2))
plt.scatter(y, samples)
plt.plot(y, p(y))
plt.title('quadratic'+ str("y=%.6fx^2+(%.6f)x+(%.6f)"%(p[2],p[1],p[0])))

ax = fig.add_subplot(gs[2,3])
plt.plot(y, p(y))
plt.scatter(y, samples)
plt.title('3th degree polynomial'+ str("y=%.6fx^3+(%.6f)x^2+(%.6f)x+(%.6f)"%(p[3],p[2],p[1],p[0])))

ax = fig.add_subplot(gs[3,3])
p = np.poly1d(np.polyfit(y, samples, 6))
plt.scatter(y, samples)
plt.plot(y, p(y))
plt.title('6th degree polynomial'+ str("y=%.6fx^6+(%.6f)x^5+(%.6f)x^4+(%.6f)x^3+(%.6f)x^2+(%.6f)x+(%.6f)"%(p[6],p[5],p[4],p[3],p[2],p[1],p[0])))


plt.show()
