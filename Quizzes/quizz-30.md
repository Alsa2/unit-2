# Quizz 30
## Part 1
```python
import matplotlib.pyplot as plt
import numpy as np


h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
window = 4
samples = []
samples_h = []
samples_smooth = []


x = []
for i in range(0, len(h)):
    x.append(i)


smooth_h_4_points = []
for i in range(0, len(h)-3):
    smooth_h_4_points.append((h[i]+h[i+1]+h[i+2]+h[i+3])/4)

smooth_x_4_points = []
for i in range(0, len(smooth_h_4_points)):
    smooth_x_4_points.append(i + 1.5)


for i in range(len(h)):
    samples.append(i)
for i in range(0, len(h), window//2):
    samples_smooth.append(i)
    values = h[i:i+window]
    samples_h.append(np.mean(values))


plt.subplot(1, 3, 1)
plt.plot(x, h, label='Normal Values')
plt.subplot(1, 3, 2)
plt.plot(smooth_x_4_points, smooth_h_4_points, label='4 Point Smoothed Values')
plt.subplot(1, 3, 3)
plt.plot(samples_smooth, samples_h, label='50% Point Smoothed Values')
plt.show()
```

## Part 2

```
The internet was first created in 1969 by the Advanced Research Projects Agency (ARPA) of the U.S. Department of Defense. Source: https://www.computerhope.com/issues/ch000795.html
```
“Open AI GPT-3 language model.” Elon Musk, 2020. Source: beta.openai.com