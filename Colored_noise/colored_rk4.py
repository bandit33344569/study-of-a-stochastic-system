import math
import random

from deterministic_system.runge_kutta import rk_calc


def euler_maruyama_calc(a, s_x, s_y, h):
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    sigma = math.sqrt(2 * a)
    r1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    r2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    s_x = s_x - a * s_x * h + sigma * math.sqrt(h) * r1
    s_y = s_y - a * s_y * h + sigma * math.sqrt(h) * r2
    return s_x, s_y


def runge_kutta_color_noise_calc(s0_x, s0_y, h, a):
    s_x = runge_kutta_color_noise(s0_x, h, a)
    s_y = runge_kutta_color_noise(s0_y, h, a)
    return s_x, s_y


def runge_kutta_color_noise(s0, h, a):
    """
    Модифицированный метод Рунге-Кутты 4-го порядка для стохастического дифференциального уравнения.
    Решает уравнение: ds = -a * s * dt + sqrt(2a) * dW(t).

    :param s0: начальное значение шума
    :param h: шаг метода Рунге-Кутты
    :param a: коэффициент затухания шума
    :return: новое значение s
    """
    # Коэффициент \sqrt{2a}
    sigma = math.sqrt(2 * a)

    # Генерация приращения винеровского процесса через преобразование Бокса-Мюллера
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    dW = math.sqrt(h) * math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    # Коэффициенты для детерминированной части (RK4)
    k1 = -a * s0
    k2 = -a * (s0 + 0.5 * h * k1)
    k3 = -a * (s0 + 0.5 * h * k2)
    k4 = -a * (s0 + h * k3)

    # Обновление значения s
    s_next = s0 + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4) + sigma * dW

    return s_next


def rk4_random_colored_noise(x0, y0, n, p, eps, h, a):
    '''
    Метод Рунге-Кутты 4-го порядка с аддитивным цветным шумом (процесс Орнштейна-Уленбека).
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
    xn1 = x0
    yn1 = y0

    # Начальные значения цветного шума
    s_x = 0.0  # Шум для x
    s_y = 0.0  # Шум для y

    for i in range(n):
        # Генерация белого шума через преобразование Бокса-Мюллера

        # Обновление цветного шума по уравнению (2): ds = -a s dt + \sqrt{2a} dW(t)
        s_x, s_y = runge_kutta_color_noise_calc(s_x, s_y, h, a)

        # Текущие значения
        x0 = xn1
        y0 = yn1

        # Вычисление детерминированной части методом Рунге-Кутты
        k, l = rk_calc(h, x0, y0, p)

        # Обновление координат с учетом детерминированной части и цветного шума
        xn1 = x0 + k + eps * s_x
        yn1 = y0 + l + eps * s_y

        # Условие неотрицательности (если требуется)
        if xn1 < 0:
            xn1 = 0
        if yn1 < 0:
            yn1 = 0

        # Обновление массивов
        time += h
        x.append(xn1)
        y.append(yn1)
        time_array.append(time)

    return x, y, time_array
