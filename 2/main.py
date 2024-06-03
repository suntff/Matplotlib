import numpy as np
import matplotlib.pyplot as plt
delta = 0
A = 1
B = 1
a = [3, 3, 5, 5]
b = [2, 4, 4, 6]
t = np.arange(0, 2 * np.pi, 0.001)
fig, axes = plt.subplots(1, 4, figsize=(20, 20))

for i in range(4):
    x = A * np.sin(a[i] * t + delta)
    y = B * np.sin(b[i] * t)
    axes[i].plot(x, y)
    axes[i].set_title(f'a:b = {a[i]}:{b[i]}')
    axes[i].set_aspect('equal')
    axes[i].grid(True)
plt.show()
