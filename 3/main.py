import time
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
delta = 0
A = 1
B = 1
fig, ax = plt.subplots()
t = np.arange(0, 2 * np.pi, 0.001)
x = A * np.sin(0 * t + delta)
y = B * np.sin(1 * t)
line, = ax.plot(x, y)
for i in range(100):
    ratio = i / 100
    x = A * np.sin(ratio * t + delta)
    y = B * np.sin(t)
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.1)
plt.ioff()
plt.show()


