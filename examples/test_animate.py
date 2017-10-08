import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivyagg')
#matplotlib.use('Gtk')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


figure, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(figure, animate, np.arange(1, 200), init_func=init,
                              interval=1, blit=True)
plt.show()