import cmath
import math

from stohastic_system.stoh_rk4 import rk4_random
import numpy as np


def make_ellipse(x0, y0, n, p, eps, h):
    w_matrix = get_W_matrix(p)
    cov_matrix, x, y = get_cov_matrix(x0, y0, n, p, eps, h)
    s = [[1, 0],
         [0, 1]]
    q = math.sqrt(-math.log(0.05))
    '''бывает такое что собственное число становится меньше нуля'''
    # w - собств числа , v - собств вектора
    print(w_matrix)
    w, v = np.linalg.eig(np.array(w_matrix))
    lambda1, lambda2 = w[1], w[0]
    print(lambda1, lambda2)
    v1, v2 = v[0], v[1]
    print(v1, v2)

    i = 0
    x_arr, y_arr = [], []
    while i < 2 * math.pi:
        z1 = eps * q * math.sqrt(2 * lambda1) * math.cos(i)
        z2 = eps * q * math.sqrt(2 * lambda2) * math.sin(i)
        yf = x0 + (v2[1] * z1 - z2 * v1[1]) / (v1[0] * v2[1] - v1[1] * v2[0])
        xf = y0 + (v1[0] * z2 - z1 * v2[0]) / (v1[0] * v2[1] - v1[1] * v2[0])
        x_arr.append(xf)
        y_arr.append(yf)
        i += 0.001
    return x_arr, y_arr, x, y


def get_cov_matrix(x0, y0, n, p, eps, h):
    x, y, t = rk4_random(x0, y0, n, p, eps, h)
    sum_x = sum(x) / n
    sum_y = sum(y) / n
    a = sum(map(lambda xx: (xx - sum_x) ** 2, x)) / n
    b = sum(map(lambda xx: (xx - sum_y) ** 2, y)) / n
    temp_sum = 0
    for i in range(n):
        temp_sum += (x[i] - sum_x) * (y[i] - sum_y)
    c = temp_sum / n
    return [[a, c],
            [c, b]], x, y


def get_W_matrix(p):
    b = (-110 * p * p - 121) / (2 * p * (-10 * p + 11))
    a = 0.5 - b
    d = 1.1*(-0.5 / p - b)
    print(a, b, b, d)
    w1 = (100 * p * p + 11 * p + 121) / (22 * p - 20 * p * p)
    w2 = (-121 - 110 * p * p) / (22 * p - 20 * p * p)
    w3 = w2
    w4 = -(-121 * p * p - 11 * p - 121) / (22 * p - 20 * p * p)
    """p=0.5"""
    print(w1, w2, w3, w4)
    # w1, w2, w3, w4 = 101 / 4, -99 / 4, -99 / 4, 209 / 8
    'p=1.05'
    #w1, w2, w3, w4 = 141 / 4, 143 / 4, 143 / 4, 77 / 4
    #print(w1, w2, w3, w4)
    return [[w1, w2],
            [w3, w4]]
