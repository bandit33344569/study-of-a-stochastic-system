from functions import f, g


def rk_calc(h, x, y, p):
    '''
    подсчет коэфицентов k и l
    '''
    k1 = h * (f(x, y))
    l1 = h * (g(x, y, p))

    k2 = h * f(x + k1 / 2, y + l1 / 2)
    l2 = h * g(x + k1 / 2, y + l1 / 2, p)

    k3 = h * f(x + k2 / 2, y + l2 / 2)
    l3 = h * g(x + k2 / 2, y + l2 / 2, p)

    k4 = h * f(x + k3, y + l3)
    l4 = h * g(x + k3, y + l3, p)

    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    L = ((l1 + 2 * l2 + 2 * l3 + l4) / 6)
    return k, L


def rk4(x0, y0, n, p, h):
    '''
    :param x0: координаты точки с которой начинаем метод рунге_кутта
    :param y0: координаты точки с которой начинаем метод рунге_кутта
    :param n:  количество итераций метода Рунге_Кутта
    :param p:  параметр системы
    :param h:
    :return: массивы координат x,y
    '''
    x = [x0]
    y = [y0]
    xn1 = x0
    yn1 = y0
    for i in range(n):
        x0 = xn1
        y0 = yn1
        k, l = rk_calc(h, x0, y0, p)

        xn1 = x0 + k
        x.append(xn1)
        yn1 = y0 + l
        y.append(yn1)

    return x, y
