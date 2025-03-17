from matplotlib import pyplot as plt

from Colored_noise.colored_cycle import make_rk4_colored_cycle
from Colored_noise.colored_rk4 import rk4_random_colored_noise
from deterministic_system.limitCycle import simple_cycle


def show_colored_stable_rk(x0, y0, n, p, eps, h, a):
    '''
    :param a:
    :param x0: асбцисса точки равновесия
    :param y0: оридната тчоки равновесия
    :param n:  количество итераций
    :param p:  параметр системы
    :param eps: шум системы
    :param h:   точность рунге
    :return: рисунок стохастической фазовой траектории
    '''
    x, y, t_arr = rk4_random_colored_noise(x0, y0, n, p, eps, h, a)
    plt.plot(x, y)
    # plt.axis([0, 10, 0, 10])
    plt.title(f"p={p}, a={a}, eps={eps}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} eps={eps} a={a}.png")
    plt.show()
    plt.close()


def show_rk4_colored_with_cycle(p, eps, delta, h, n, a):
    x_arr, y_arr, x, y = make_rk4_colored_cycle(p, eps, delta, h, n, a)
    plt.plot(x_arr, y_arr)
    plt.plot(x, y, color="orange")
    plt.title(f"p={p}, a={a}, eps={eps}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} eps={eps} a={a}.png")
    plt.show()
    plt.close()
