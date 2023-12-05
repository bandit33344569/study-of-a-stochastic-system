import matplotlib.pyplot as plt
import numpy as np
from deterministic_system.limitCycle import simple_cycle
from deterministic_system.runge_kutta import rk4
from stohastic_system.stoh_rk4 import rk4_random
from stohastic_system.stoh_cycle import make_rk4_stoh_cycle, strip_make_stoh, get_max_and_min_m, get_data_for_3d
from stohastic_system.ellipse import make_ellipse
from collections import Counter


def show_rk(n, p, h):
    '''
    :param x0: координаты точки с которой начинаем метод рунге_кутта
    :param y0: координаты точки с которой начинаем метод рунге_кутта
    :param n:  количество итераций метода Рунге_Кутта
    :param p:  параметр системы
    :param h:  точность
    :returns: показывает фазовую траекторию
    '''
    x, y = rk4(2, 2, n, p, h)
    x2, y2 = rk4(2, 3, n, p, h)
    x3, y3 = rk4(3, 2, n, p, h)
    x4, y4 = rk4(0.9, 0.9, n, p, h)
    plt.plot(x, y)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.show()
    plt.close()


def show_limit_cycle(p, delta, h):
    '''
    :param p: параметр системы
    :param delta: точность поиска цикла
    :param h: точность рунге
    :return: график предельного цикла
    '''
    x, y, n = simple_cycle(p, delta, h)
    plt.plot(x, y)
    plt.show()
    plt.close()


def show_some_cycles(delta, h):
    p = 1.1333309
    i = 0.000000001
    while p < 1.133331:
        print(p)
        x_cycle, y_cycle, n = simple_cycle(p, delta, h)
        plt.xlim(0, 25)
        plt.ylim(0, 25)
        plt.plot(x_cycle, y_cycle, color="black")
        plt.savefig(f"{p}.png")
        plt.close()
        p += i


def show_stoh_cycle(p, eps, delta, h, n):
    x_stoh, y_stoh = make_rk4_stoh_cycle(p, eps, delta, h, n)
    print(len(x_stoh))
    x, y, n = simple_cycle(p, delta, h)
    plt.plot(x_stoh[::1000], y_stoh[::1000])
    plt.plot(x, y)
    plt.show()


def show_stoh_stable_rk(x0, y0, n, p, eps, h):
    '''
    :param x0: асбцисса точки равновесия
    :param y0: оридната тчоки равновесия
    :param n:  количество итераций
    :param p:  параметр системы
    :param eps: шум системы
    :param h:   точность рунге
    :return: рисунок стохастической фазовой траектории
    '''
    x, y, t_arr = rk4_random(x0, y0, n, p, eps, h)
    plt.plot(x, y)
    plt.show()
    plt.close()


def show_strip(p, eps, delta, h):
    x_cycle, y_cycle, n = simple_cycle(p, delta, h)
    m_arr, x_band1_arr, x_band2_arr, y_band1_arr, \
    y_band2_arr = strip_make_stoh(p, eps, delta, h)
    x_stoh, y_stoh = make_rk4_stoh_cycle(p, eps, delta, h)
    plt.plot(x_stoh, y_stoh, color="green", linewidth=2)
    plt.plot(x_cycle, y_cycle, color="red")
    plt.plot(x_band1_arr, y_band1_arr, color="black", linewidth=2)
    plt.plot(x_band2_arr, y_band2_arr, color="black", linewidth=2)
    plt.show()
    plt.close()


def show_maxmin_m(p, eps, delta, h):
    m_max_arr, m_min_arr, p_arr = get_max_and_min_m(p, eps, delta, h)
    plt.semilogy(p_arr, m_max_arr, label="max m")
    plt.semilogy(p_arr, m_min_arr, label="min m")

    # plt.legend()
    # plt.xlabel("параметр P")
    # plt.ylabel("Степень жесткости")
    plt.show()
    plt.close()


def show_3d_m(p, eps, delta, h):
    m_arr, x_arr, y_arr = get_data_for_3d(p, eps, delta, h)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.plot(x_arr, y_arr, color="orange")
    ax.plot(x_arr, y_arr, m_arr, label='', color="blue")

    plt.show()


def show_dispersion_ellipse(x0, y0, n, p, ep, h):
    # ep = 0.5
    # while ep < 0.8:
    while ep < 0.02:
        for i in range(10):
            x_arr, y_arr, x, y = make_ellipse(x0, y0, n, p, ep, h)
            plt.plot(x[300000::], y[300000::])
            plt.plot(x_arr, y_arr)
            plt.title(label=f"n={n}, p={p}, eps={ep}, h={h}, i={i}")
            plt.savefig(f"{ep}, №{i}.png")
            plt.close()
            print(i)
        ep += 0.001
    # plt.show()


def show_bifurcation_diagram(p, delta, h):
    p = 1.1331
    x_max_arr = []
    x_min_arr = []
    p_arr = []
    i = 0.00002
    while p < 1.1345:
        print(p)
        x_cycle, y_cycle, n = simple_cycle(p, delta, h)
        x_max_arr.append(max(x_cycle))
        x_min_arr.append(min(x_cycle))
        p_arr.append(p)
        p += i
    plt.plot(p_arr, x_max_arr, color="black")
    plt.plot(p_arr, x_min_arr, color="black")
    plt.show()


def show_FSCH_cycle(eps, delta, h):
    p_arr = [3, 1.2, 1.3, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6]
    for p in p_arr:
        print(p)
        m_arr, x_arr, y_arr = get_data_for_3d(p, eps, delta, h)
        plt.plot(x_arr, m_arr)
        plt.title(label=f"p={p}, h={h}, delta={delta}")
        plt.savefig(f"{p}.png")
        plt.close()


def show_intersection_diagram(x0, y0, n, p, eps, h):
    p_arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.05]
    interval = 50
    for p in p_arr:
        x_arr, y_arr, t_arr = rk4_random(x0, y0, n, p, eps, h)
        min_x, max_x = min(x_arr), max(x_arr)
        print(min_x, max_x)
        k = (max_x - min_x) / interval
        print(k)
        new_x = []
        k_arr = []
        for i in range(interval):
            new_x.append(0)
            k_arr.append(min_x)
            for j in range(100000, len(y_arr)):
                if 1 + h >= y_arr[j] >= 1 - h and x_arr[j] < min_x + k:
                    new_x[i] += 1
            min_x += k
        print(k_arr)
        print(new_x)
        plt.bar(k_arr, new_x, width=k, linewidth=1, edgecolor='k')
        plt.savefig(f"{p}.png")
        plt.close()
