import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre
P = [legendre(i) for i in range(1,8)]
x = np.arange(-1,1,0.001)
y = [np.array(P[i](x)) for i in range(7)]
for i in range(len(y)):
    plt.plot(x, y[i],label = f"n = {i+1}")
plt.title('Полиномы Лежандра')
plt.legend()
plt.show()

