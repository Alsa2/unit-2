import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 4, 1.5, 4, 2.5, 6, 4, 3, 5.5, 5, 2]
y = [3, 4, 8, 4.5, 10, 5, 15, 9, 5, 16, 13, 3]

plt.scatter(x, y)
#label x and y axis
plt.xlabel('x')
plt.ylabel('y')


#fit a line to the data
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print("The model is: ", p)
plt.plot(x, p(x), "r--")
plt.text(1, 15, "y=%.6fx+(%.6f)"%(z[0],z[1]), fontsize=15)


topredict = 1.5
plt.scatter(topredict, p(topredict), color='gold', label=('Prediction of '+topredict))
plt.show()