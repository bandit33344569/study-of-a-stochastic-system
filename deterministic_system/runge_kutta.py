from functions import f, g


def rk_calc(h, x, y, p, q):
    '''
    подсчет коэфицентов k и l
    '''
    k1 = h * (f(x, y))
    l1 = h * (g(x, y, p, q))

    k2 = h * f(x + k1 / 2, y + l1 / 2)
    l2 = h * g(x + k1 / 2, y + l1 / 2, p, q)

    k3 = h * f(x + k2 / 2, y + l2 / 2)
    l3 = h * g(x + k2 / 2, y + l2 / 2, p, q)

    k4 = h * f(x + k3, y + l3)
    l4 = h * g(x + k3, y + l3, p, q)

    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    L = (l1 + 2 * l2 + 2 * l3 + l4) / 6
    return k, L


def rk4(x0, y0, n, p, q, h):
    '''
    :param q: параметр системы
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
        k, l = rk_calc(h, x0, y0, p, q)

        xn1 = x0 + k
        x.append(xn1)
        yn1 = y0 + l
        y.append(yn1)

    return x, y


def boxed_rk4(x0, y0, n, p, q, h, box_coord):
    '''
    :param x0:
    :param y0:
    :param n:
    :param p:
    :param q:
    :param h:
    :param box_coord: [x1,y1,x2,y2] - координаты коробки, x1<x2,y1<y2
    :return:
    '''
    x = [x0]
    y = [y0]
    xn1 = x0
    yn1 = y0
    for i in range(n):
        x0 = xn1
        y0 = yn1
        k, l = rk_calc(h, x0, y0, p, q)
        xn1 = x0 + k
        yn1 = y0 + l
        if box_coord[2] > xn1 > box_coord[0]:
            x.append(xn1)
        else:
            return x[0], y[0], 'r'
        if box_coord[3] > xn1 > box_coord[1]:
            y.append(yn1)
        else:
            return x[0], y[0], 'r'

    return x[0], y[0], 'g'
