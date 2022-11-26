# Quizz 27
Program 
```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

sensorA = [16, 24, 24, 9, 23, 26, 26, 23, 25, 24]
sensorB = [2, 19, 25, 10, 11, 24, 17, 7, 24, 17]
sensorC = [15, 11, 24, 21, 6, 2, 18, 27, 1, 16]

x = []

for i in range(0, len(sensorA)):
    x.append(i)

plt.subplot(1, 3, 1)
plt.plot(x, sensorA, label='data')
plt.subplot(1, 3, 2)
plt.plot(x, sensorB, label='data')
plt.subplot(1, 3, 3)
plt.plot(x, sensorC, label='data')

meanA = []
standard_deviationA = []
for i in range(0, len(sensorA)):
    meanA.append(np.mean([sensorA[i]]))
    standard_deviationA.append(np.std([sensorA[i]]))

meanB = []
standard_deviationB = []
for i in range(0, len(sensorB)):
    meanB.append(np.mean([sensorB[i]]))
    standard_deviationB.append(np.std([sensorB[i]]))

meanC = []
standard_deviationC = []
for i in range(0, len(sensorC)):
    meanC.append(np.mean([sensorC[i]]))
    standard_deviationC.append(np.std([sensorC[i]]))

plt.subplot(1, 3, 1)
plt.errorbar(x, meanA, yerr=standard_deviationA, fmt='o', color='white', ecolor='red', capsize=5, capthick=2)
plt.subplot(1, 3, 2)
plt.errorbar(x, meanB, yerr=standard_deviationB, fmt='o', color='white', ecolor='red', capsize=5, capthick=2)
plt.subplot(1, 3, 3)
plt.errorbar(x, meanC, yerr=standard_deviationC, fmt='o', color='white', ecolor='red', capsize=5, capthick=2)

plt.show()
```