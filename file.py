"new file"
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def main():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    line, = ax.plot([], [], lw=2)
    xdata, ydata = [x * 20 for x in range(30)], [x for x in range(30)]
    def init():
        line.set_data(xdata, ydata)
        return line,
    def animate(i):
        x = np.random.randint(0, 100)
        y = np.random.randint(0, 100)
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        return line,
    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=100, blit=True)
    plt.show()


if __name__ == '__main__':
    main()