import numpy as np
from matplotlib import pyplot as plt

from deterministic_system.runge_kutta import rk4


def det_node_sol(n, p, q, h):
    '''
    :param n:
    :param p:
    :param q:
    :param h:
    :return: должен показывать точки графиков которые проходят длинную траекторию и маленькую
    '''
    for x0 in np.arange(0.1, 1, 4):
        for y0 in np.arange(0.0115 + 0.00025, 0.08, 0.0005):
            print(x0, y0)
            x, y = rk4(x0, y0, n, p, q, h)
            plt.plot(x, y, color='#ff7f0e')
        for y0 in np.arange(0.0001, 0.0115 + 0.00025, 0.0005):
            print(x0, y0)
            x, y = rk4(x0, y0, n, p, q, h)
            plt.plot(x, y, color='#1f77b4')
    # x, y = rk4(100, 100, 2000000, p, q, h)
    # plt.plot(x, y, color='k')
    # x2, y2 = rk4(0.000000001, 0.000000001, 4000000, p, q, h)
    # plt.plot(x2, y2, color='aquamarine')
    x, y = rk4(0.1, 0.01167, 200000, p, q, h)
    plt.plot(x, y, color='r', linewidth=5)
    plt.plot(1, 1, 'o', markersize=10, color='k')
    plt.title(f"p = {p}, q = {q}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"q={q},p={p}.png")
    plt.show()
    plt.close()
