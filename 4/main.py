import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure()
ax1 = fig.add_axes([0.05, 0.6, 0.35, 0.35])
ax2 = fig.add_axes([0.6, 0.6, 0.35, 0.35])
ax_sum = fig.add_axes([0.35, 0.05, 0.35, 0.35])
x = np.arange(-10*np.pi,10*np.pi,0.1)
st_amplitude_1 = 1
st_oscillation_1=1
st_amplitude_2 = 1
st_oscillation_2 = 1
y_1 = st_amplitude_1*np.sin(st_oscillation_1*x)
y_2 = st_amplitude_2*np.sin(st_oscillation_2*x)
y_sum = y_1+y_2
l1, = ax1.plot(x,y_1)
l2, = ax2.plot(x,y_2)
l3, = ax_sum.plot(x, y_sum)
ax1_slider_amplitude = plt.axes([0.15,0.5,0.2,0.03])
ax1_slider_oscillation = plt.axes([0.15,0.45,0.2,0.03])
ax2_slider_amplitude = plt.axes([0.7,0.5,0.2,0.03])
ax2_slider_oscillation = plt.axes([0.7,0.45,0.2,0.03])
slider1_amplitude = Slider(ax1_slider_amplitude,"amplitude",0.01,5.0,valinit=st_amplitude_1)
slider1_oscillation = Slider(ax1_slider_oscillation,"oscillation",0.01,5.0,valinit=st_oscillation_1)
slider2_amplitude = Slider(ax2_slider_amplitude,"amplitude",0.01,5.0,valinit=st_amplitude_2)
slider2_oscillation = Slider(ax2_slider_oscillation,"oscillation",0.01,5.0,valinit=st_oscillation_2)
def update(val):
    amplitude_1 = slider1_amplitude.val
    oscillation_1 = slider1_oscillation.val
    amplitude_2 = slider2_amplitude.val
    oscillation_2 = slider2_oscillation.val
    l1.set_ydata(amplitude_1*np.sin(oscillation_1*x))
    l2.set_ydata(amplitude_2 * np.sin(oscillation_2 * x))
    l3.set_ydata(amplitude_2 * np.sin(oscillation_2 * x)+amplitude_1*np.sin(oscillation_1*x))
    fig.canvas.draw_idle()
slider1_amplitude.on_changed(update)
slider1_oscillation.on_changed(update)
slider2_amplitude.on_changed(update)
slider2_oscillation.on_changed(update)
ax1.set_title('ax1')
ax2.set_title('ax2')
ax_sum.set_title('ax_sum')
plt.show()
