import math
import random

from deterministic_system.runge_kutta import rk_calc


def rk4_random(x0, y0, n, p, eps, h):
    '''
    :param x0: асбцисса точки равновесия
    :param y0: оридната тчоки равновесия
    :param n:  количество итераций
    :param p:  параметр системы
    :param eps: шум системы
    :param h:   точность рунге
    :return: массивы координат стохастической фазовой траектории
    и времени
    '''
    time = 0
    time_array = [0]
    x = [x0]
    y = [y0]
    xn1 = x0
    yn1 = y0
    for i in range(n):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)

        x0 = xn1
        y0 = yn1

        k, l = rk_calc(h, x0, y0, p)

        xn1rk = x0 + k
        r1 = math.sqrt(-2 * math.log(a)) * math.cos(2 * math.pi * b)
        xn1 = xn1rk + eps * math.sqrt(h) * r1
        x.append(xn1)

        yn1rk = y0 + l
        r2 = math.sqrt(-2 * math.log(a)) * math.sin(2 * math.pi * b)
        yn1 = yn1rk + eps * math.sqrt(h) * r2
        y.append(yn1)
        time += h
        time_array.append(time)
    return x, y, time_array
