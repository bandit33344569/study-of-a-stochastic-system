from stoh_rk4 import rk4_random
import numpy as np


def make_ellipse(x0, y0, n, p, eps, h):
    cov_matrix = get_cov_matrix(x0, y0, n, p, eps, h)
    w_matrix = get_W_matrix(p)
    s = [[1, 0],
         [0, 1]]
    # w - собств числа , v - собств вектора
    w, v = np.eig(np.array(w_matrix))
    print(w)
    print(v)


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
            [c, b]]


def get_W_matrix(p):
    w1 = (11 + 221 * p) / (22 - 20 * p)
    w2 = (-231 * p) / (22 - 20 * p)
    w3 = (2541 * p * p + 110 * p - 121) / (220 * p - 200 * p * p)
    return [[w1, w2],
            [w2, w3]]
