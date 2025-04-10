import numpy as np
from matplotlib import pyplot as plt

from deterministic_system.runge_kutta import rk4, boxed_rk4


def dot_attractor(n, p, q, h):
    '''
    :param n:
    :param p:
    :param q:
    :param h:
    :return: детальный график возле аттрактора точки
    '''
    for x0 in np.arange(1, 1.5, 5):
        for y0 in np.arange(0.5, 1.5, 0.05):
            x, y = rk4(x0, y0, n, p, q, h)
            plt.plot(x, y)
    plt.title(f"p = {p}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.show()
    plt.close()


def transition_box(n, p, q, h, box_coord, step):
    '''
    :param step:
    :param n:
    :param p:
    :param q:
    :param h:
    :param box_coord: [x1,y1,x2,y2] - координаты коробки
    :return:
    '''
    vertices = [
        (box_coord[0], box_coord[1]),  # Левая нижняя
        (box_coord[2], box_coord[1]),  # Правая нижняя
        (box_coord[2], box_coord[3]),  # Правая верхняя
        (box_coord[0], box_coord[3]),  # Левая верхняя
        (box_coord[0], box_coord[1])  # Замыкающая точка (для замыкания контура)
    ]
    plt.xlim(0, 2)
    plt.ylim(0, 2)
    x_coords, y_coords = zip(*vertices)
    for x0 in np.arange(box_coord[0], box_coord[2] + step, step):
        for y0 in np.arange(box_coord[1], box_coord[3] + step, step):
            print(x0, y0)
            x, y, color = boxed_rk4(x0, y0, n, p, q, h, box_coord)
            plt.plot(x, y, color=color, marker='o', markersize=1)
    plt.plot(x_coords, y_coords, color='k', alpha=0.4)
    plt.title(f"p = {p}, q = {q}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p = {p}, q = {q}, transition.png")
    plt.show()
    plt.close()
