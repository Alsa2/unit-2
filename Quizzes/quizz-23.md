# Quizz 23
## Part 1

```python
import random
import matplotlib.pyplot as plt
plt.style.use('dark_background')


random.seed(1234)
def produce(n:int, m:int, s:int):
    print(f"|{'x'.center(10)}|{'y'.center(10)}|")
    x_out = []
    y_out = []
    for _ in range(n):
        x = random.randint(0, 100)
        x_out.append(x)
        y = x ** (1/2*((m/s)**2))
        y_out.append(y)
        print(f"|{str(x).center(10)}|{str(y).center(10)}|")

    return x_out, y_out

data_y, data_x = produce(10, 5, 2)

from matplotlib import pyplot as plt

plt.plot(data_x, data_y, 'o')
plt.xlabel('x')
plt.ylabel('$y = x^{1/2((m/s)^2)}$')

plt.show()
```
![](../Images/quizz23-proof.png)
**Fig. 1** Proof

## Part 2
Truth Table for A(A+B)
| A | B | Output |
|---|---|--------|
| 0 | 0 | F      |
| 0 | 1 | F      |
| 1 | 0 | T      |
| 1 | 1 | T      |