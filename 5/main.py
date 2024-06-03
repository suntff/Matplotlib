import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)

w1 = np.arange(-5, 5, 0.1)
w2 = np.arange(-5, 5, 0.1)
W1, W2 = np.meshgrid(w1, w2)
mse = np.zeros((len(w1), len(w2)))
for i, val_1 in enumerate(w1):
    for j, val_2 in enumerate(w2):
        mse[i, j] = np.mean((val_1 * x + val_2 - y) ** 2)

ax1.plot_wireframe(W1, W2, mse)
ax2.plot_wireframe(W1, W2, np.log10(mse))
ax1.set_title('MSE(linear scale)')
ax2.set_title('MSE(log scale)')
ax1.set_xlabel('x')
ax2.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_ylabel('y')
ax1.set_zlabel('z')
ax2.set_zlabel('z')

plt.show()



