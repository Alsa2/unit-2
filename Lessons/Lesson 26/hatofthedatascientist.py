import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

h=[57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0] 
low=[53.0, 54.0, 54.0, 52.0, 54.0, 51.0, 53.0, 53.0, 50.0, 51.0, 52.0, 53.0, 49.0, 50.0, 50.0, 49.0, 50.0, 47.0, 50.0]
high= [58.0, 60.0, 61.0, 57.0, 56.0, 58.0, 58.0, 57.0, 56.0, 55.0, 54.0, 57.0, 54.0, 56.0, 53.0, 56.0, 53.0, 55.0, 52.0]

samples = []
for i in range(0, len(h)):
    samples.append(i)

plt.subplot(1, 2, 1)
plt.plot(samples, h, label='data')
plt.plot(samples, low, label='low')
plt.plot(samples, high, label='high')

#ANalysing the data
mean = []
standard_deviation = []
for i in range(0, len(h)):
    mean.append(np.mean([low[i], high[i]]))
    standard_deviation.append(np.std([low[i], high[i]]))

plt.subplot(1, 2, 2)
plt.fill_between(samples, high, low, alpha=0.5, linewidth=0)
plt.errorbar(samples, mean, yerr=standard_deviation, fmt='o', color='white', ecolor='red', capsize=5, capthick=2)

plt.show
