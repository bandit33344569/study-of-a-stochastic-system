import math
import random

from Colored_noise.colored_functions import f1, f2, f3


def rk4_random_colored_noise(x0, y0, n, p, q, eps, h, a, z0=0):
    '''
    Метод Рунге-Кутты 4-го порядка с аддитивным цветным шумом (процесс Орнштейна-Уленбека).
    :param q:
    :param z0:
    :param x0: начальная абсцисса
    :param y0: начальная ордината
    :param n: количество итераций
    :param p: параметр системы
    :param eps: интенсивность шума (аналог \varepsilon)
    :param h: шаг метода Рунге-Кутты
    :param a: коэффициент затухания шума (аналог a из формулы)
    :return: массивы координат x, y и времени
    '''
    time = 0
    time_array = [0]
    x = [x0]
    y = [y0]
    z = [z0]
    xn1 = x0
    yn1 = y0
    zn1 = z0

    for i in range(n):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)

        k1 = h * f1(xn1, yn1, zn1, eps)
        l1 = h * f2(xn1, yn1, zn1, p, q, eps)
        m1 = h * f3(xn1, yn1, zn1, p, q, a, h)
        k2 = h * f1(xn1 + k1 / 2, yn1 + l1 / 2, zn1 + m1 / 2, eps)
        l2 = h * f2(xn1 + k1 / 2, yn1 + l1 / 2, zn1 + m1 / 2, p, q, eps)
        m2 = h * f3(xn1 + k1 / 2, yn1 + l1 / 2, zn1 + m1 / 2, p, q, a, h)
        k3 = h * f1(xn1 + k2 / 2, yn1 + l2 / 2, zn1 + m2 / 2, eps)
        l3 = h * f2(xn1 + k2 / 2, yn1 + l2 / 2, zn1 + m2 / 2, p, q, eps)
        m3 = h * f3(xn1 + k2 / 2, yn1 + l2 / 2, zn1 + m2 / 2, p, q, a, h)
        k4 = h * f1(xn1 + k3, yn1 + l3, zn1 + m3, eps)
        l4 = h * f2(xn1 + k3, yn1 + l3, zn1 + m3, p, q, eps)
        m4 = h * f3(xn1 + k3, yn1 + l3, zn1 + m3, p, q, a, h)
        xn1 = xn1 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn1 = yn1 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
        zn1 = zn1 + (m1 + 2 * m2 + 2 * m3 + m4) / 6 + math.sqrt(2 * a) * math.sqrt(h) * math.sqrt(
            -2 * math.log(u1)) * math.cos(2 * math.pi * u2)

        # Условие неотрицательности (если требуется)
        if xn1 < 0:
            xn1 = 0
        if yn1 < 0:
            yn1 = 0
        # Обновление массивов
        time += h
        x.append(xn1)
        y.append(yn1)
        z.append(zn1)
        time_array.append(time)

    return x, y, z, time_array

