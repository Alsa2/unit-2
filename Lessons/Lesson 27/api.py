#get json api fron 192.168.6.142/readings
import requests
import json
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


url = "http://192.168.6.142/readings"
r = requests.get(url)
data = r.json()

#json format
"""
data={
    "type": "temperature",
    "id": 1,
    "unit": "celcius",
    "name": "sensor_x1",
    "readings": [
        {
            "value": 23.022,
            "sensor_id": 1,
            "id": 1,
            "datetime": "2021-11-25T21:34:50.027731"
        },
        {
            "value": 23.022,
            "sensor_id": 1,
            "id": 2,
            "datetime": "2021-11-29T19:32:10.363180"
        }]
}
"""

print(data)

values = []
readings = data["readings"][0]
for r in readings:
    values.append(r["value"])
print(values)

sample = []
for i in range(0, len(values)):
    sample.append(values[i])

plt = plt.plot(values)
plt.show()
