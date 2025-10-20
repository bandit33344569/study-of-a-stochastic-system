import matplotlib.pyplot as plt
from deterministic_system.limitCycle import simple_cycle
from deterministic_system.runge_kutta import rk4
from stohastic_system.stoh_rk4 import rk4_random
from stohastic_system.stoh_cycle import make_rk4_stoh_cycle, strip_make_stoh, get_max_and_min_m, get_data_for_3d
from stohastic_system.ellipse import make_ellipse
from stohastic_system.ellipse import get_own_numbers
import numpy as np


def show_W_own_nubmers(x0, y0, n, p, eps, h):
    p = 0.1
    p_arr = []
    l1, l2 = [], []
    while p < 1.99:
        lambda1, lambda2 = get_own_numbers(x0, y0, n, p, eps, h)
        l1.append(lambda1)
        l2.append(lambda2)
        p_arr.append(p)
        p += 0.001
        print(p)
    print(l1, l2)
    plt.plot(p_arr, l1)
    plt.yscale('log')
    plt.xlabel('p', fontsize=10)
    plt.ylabel('λ', fontsize=10)
    plt.savefig(f"{1}.png")
    plt.close()
    plt.plot(p_arr, l2)
    plt.yscale('log')
    plt.xlabel('p', fontsize=10)
    plt.ylabel('λ', fontsize=10)
    plt.savefig(f"{2}.png")
    plt.close()


def deterministic_more_solutions(n, p, q, h):
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


def show_rk(n, p, q, h):
    '''
    :param q:
    :param n:  количество итераций метода Рунге_Кутта
    :param p:  параметр системы
    :param h:  точность
    :returns: показывает фазовую траекторию
    '''
    x, y = rk4(2, 2, n, p, q, h)
    x2, y2 = rk4(2, 3, n, p, q, h)
    x3, y3 = rk4(3, 2, n, p, q, h)
    x4, y4 = rk4(0.9, 0.9, n, p, q, h)
    plt.plot(x, y)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.title(f"p = {p}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"q = {q}.png")
    plt.close()


def show_rk_with_limit_cycle(p, delta, h, n1):
    x1, y1 = rk4(2, 2, n1, p, h)
    x2, y2 = rk4(2, 3, n1, p, h)
    x3, y3 = rk4(3, 2, n1, p, h)
    x4, y4 = rk4(0.9, 0.9, n1, p, h)
    x5, y5 = rk4(0.5, 0.5, n1, p, h)
    plt.plot(x1, y1, color="black")
    plt.plot(x2, y2, color="black")
    plt.plot(x3, y3, color="black")
    plt.plot(x4, y4, color="black")
    plt.plot(x5, y5, color="black")
    x, y, n = simple_cycle(p, delta, h)
    plt.plot(x, y)
    plt.title(f"n= {n1},h = {h},p = {p}")
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
    p = 2.1
    i = 0.8
    plt.xlim(0, 4)
    plt.ylim(0, 30)
    while p < 10:
        print(p)
        a = "{:.1f}".format(p)
        x_cycle, y_cycle, n = simple_cycle(p, delta, h)
        plt.plot(x_cycle, y_cycle, label=f"p = {a}")
        plt.legend()
        p += i
    plt.savefig(f"{p}.png")
    plt.close()


def show_stoh_cycle(p, eps, delta, h, n):
    print(p)
    x_stoh, y_stoh, x, y = make_rk4_stoh_cycle(p, eps, delta, h, n)
    plt.plot(x_stoh[10000::100], y_stoh[10000::100])
    plt.plot(x, y)
    plt.title(f"p={p}, eps={eps}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} eps={eps}.png")
    plt.close()


def show_stoh_stable_rk(x0, y0, n, p,q, eps, h):
    '''
    :param x0: асбцисса точки равновесия
    :param y0: оридната тчоки равновесия
    :param n:  количество итераций
    :param p:  параметр системы
    :param eps: шум системы
    :param h:   точность рунге
    :return: рисунок стохастической фазовой траектории
    '''
    x, y, t_arr = rk4_random(x0, y0, n, p,q, eps, h)
    plt.plot(x, y)
    plt.axis([-0.1, 20, -0.1, 20])
    plt.title(f"p={p}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} eps={eps}.png")
    plt.show()
    plt.close()


def show_strip(p, eps, delta, h, n):
    m_arr, x_band1_arr, x_band2_arr, y_band1_arr, \
    y_band2_arr = strip_make_stoh(p, eps, delta, h)
    x_stoh, y_stoh, x_cycle, y_cycle = make_rk4_stoh_cycle(p, eps, delta, h, n)
    plt.plot(x_stoh, y_stoh, color="green", linewidth=2)
    plt.plot(x_cycle, y_cycle, color="red")
    plt.plot(x_band1_arr, y_band1_arr, color="black", linewidth=2)
    plt.plot(x_band2_arr, y_band2_arr, color="black", linewidth=2)
    plt.show()
    plt.close()


def show_max_m(p, eps, delta, h):
    m_max_arr, m_min_arr, p_arr = get_max_and_min_m(p, eps, delta, h)
    # print(p_arr)
    # print(m_max_arr)
    max_m = max(m_max_arr)
    plt.plot(p_arr, m_max_arr, label="max m")
    plt.xlabel("параметр P")
    plt.legend()
    plt.savefig(f"{max_m}.png")
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
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('m(t)')

    plt.show()


def show_dispersion_ellipse(x0, y0, n, p, ep, h):
    p_arr = [p]
    for p in p_arr:
        x_arr, y_arr, x, y = make_ellipse(x0, y0, n, p, ep, h)
        plt.plot(x[200000::1000], y[200000::1000], linestyle='', marker='.')
        plt.plot(x_arr, y_arr)
        plt.xlabel('x', fontsize=10)
        plt.ylabel('y', fontsize=10)
        plt.savefig(f"n={n}, p={p}, eps={ep}, h={h}.png")
        plt.close()


def show_bifurcation_diagram(p, delta, h):
    p = 2
    y_max_arr = [1, 1]
    y_min_arr = [1, 1]
    p_arr = [0.01, 2]
    i = 0.01
    while p < 4:
        print(p)
        x_cycle, y_cycle, n = simple_cycle(p, delta, h)
        y_max_arr.append(max(x_cycle))
        y_min_arr.append(min(x_cycle))
        p_arr.append(p)
        p += i

    plt.plot(p_arr, y_max_arr, color="black")
    plt.plot(p_arr, y_min_arr, color="black")
    plt.xlabel('p', fontsize=14)
    plt.ylabel('max x', fontsize=14)

    plt.show()


def show_FSCH_cycle(eps, delta, h):
    p_arr = [1.133325]
    for p in p_arr:
        print(p)
        m_arr, x_arr, y_arr = get_data_for_3d(p, eps, delta, h)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("m(t)")
        plt.plot(x_arr, y_arr, color="orange")
        ax.plot(x_arr, y_arr, m_arr, label='', color="blue")
        print(max(m_arr))
        plt.show()
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
