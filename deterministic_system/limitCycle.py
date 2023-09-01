import math

from deterministic_system.runge_kutta import rk_calc


def simple_cycle(p, delta, h):
    '''
    :param p: параметр системы
    :param delta: точнсть поиска цикла
    :param h: точность рунге-кутты
    :return: массивы координат точек цикла и количество точек в нем
    '''
    x_prev = 200
    y_prev = 200
    xn, yn = x_prev, y_prev
    x_intersection_prev = 100
    ''''''
    while True:
        x_prev = xn
        y_prev = yn
        k, l = rk_calc(h, x_prev, y_prev, p)
        xn = x_prev + k
        yn = y_prev + l

        if x_prev > 1 and xn > 1 and ((yn - 1) * (y_prev - 1)) < 0:
            k = (y_prev - yn) / (x_prev - xn)
            b = y_prev - k * xn
            x_intersection = (1 - b) / k
            # print(x_intersection)
            # x_intersection = x_prev + ((1 - y_prev) * (x_prev - xn) / (y_prev - yn))
            if math.fabs(x_intersection - x_intersection_prev) >= delta:
                x_intersection_prev = x_intersection
            else:
                break

    '''снова строим траекторию до первого выполнения условия'''
    x_arr = [xn]
    y_arr = [yn]
    n = 1
    while True:
        x_prev = xn
        y_prev = yn
        k, l = rk_calc(h, x_prev, y_prev, p)
        xn = x_prev + k
        yn = y_prev + l
        if x_prev > 1 and xn > 1 and ((yn - 1) * (y_prev - 1)) < 0:
            break
        n += 1
        x_arr.append(xn)
        y_arr.append(yn)
    n += 1
    x_arr.append(x_arr[0])
    y_arr.append(y_arr[0])

    return x_arr, y_arr, n
