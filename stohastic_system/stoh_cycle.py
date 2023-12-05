import math

import numpy as np

from deterministic_system.limitCycle import simple_cycle
from functions import fx, gx, gy, fy, g, f
from stohastic_system.stoh_rk4 import rk4_random


def P(x, y, p):
    matrix = np.array([[-g(x, y, p)],
                       [f(x, y)]])
    coef = 1 / math.sqrt(f(x, y) ** 2 + g(x, y, p) ** 2)
    return coef * matrix


def a_b_calc(x_arr, y_arr, n, p):
    a_arr = []
    b_arr = []
    S = np.array([[1, 0],
                  [0, 1]])
    for i in range(0, n):
        x = x_arr[i]
        y = y_arr[i]

        P_norm = np.array(P(x, y, p))

        P_transpon = P_norm.transpose()

        F_norm = np.array([[fx(x, y), fy(x, y)],
                           [gx(x, y, p), gy(x, y, p)]])

        F_transpon = F_norm.transpose()

        a = (P_transpon.dot(F_transpon + F_norm)).dot(P_norm).tolist()[0][0]
        b = (P_transpon.dot(S)).dot(P_norm).tolist()[0][0]

        a_arr.append(a)
        b_arr.append(b)
    return a_arr, b_arr


def alpha_beta_calc(a_arr, b_arr, n, h):
    alpha_arr = [1]
    beta_arr = [0]
    '''рассчет alpha(i)'''
    for i in range(1, n):
        alpha = alpha_arr[i - 1] * math.exp(((a_arr[i - 1] + a_arr[i]) / 2) * h)
        alpha_arr.append(alpha)
    '''рассчет beta(i)'''
    for i in range(1, n):
        beta = beta_arr[i - 1] + ((b_arr[i - 1] / alpha_arr[i - 1]) + (b_arr[i] / alpha_arr[i])) * h / 2
        beta_arr.append(beta)
    return alpha_arr, beta_arr


def calc_m(alpha_arr, beta_arr, C, n):
    m_arr = []
    for i in range(n):
        m = alpha_arr[i] * (C + beta_arr[i])
        m_arr.append(m)
    return m_arr


def calc_strip(x_arr, y_arr, eps, m_arr, p, n):
    q = 1.136
    x_band1_arr = []
    x_band2_arr = []
    y_band1_arr = []
    y_band2_arr = []
    for i in range(n):
        p1 = P(x_arr[i], y_arr[i], p).tolist()[0][0]
        p2 = P(x_arr[i], y_arr[i], p).tolist()[1][0]

        coef = q * eps * math.sqrt(2 * m_arr[i])

        x_band1 = x_arr[i] + coef * p1
        x_band2 = x_arr[i] - coef * p1
        y_band1 = y_arr[i] + coef * p2
        y_band2 = y_arr[i] - coef * p2

        x_band1_arr.append(x_band1)
        x_band2_arr.append(x_band2)
        y_band1_arr.append(y_band1)
        y_band2_arr.append(y_band2)
    return x_band1_arr, x_band2_arr, y_band1_arr, y_band2_arr


def strip_make_stoh(p, eps, delta, h):
    x_arr, y_arr, n = simple_cycle(p, delta, h)
    a_arr, b_arr = a_b_calc(x_arr, y_arr, n, p)
    alpha_arr, beta_arr = alpha_beta_calc(a_arr, b_arr, n, h)
    C = (alpha_arr[n - 1] * beta_arr[n - 1]) / (1 - alpha_arr[n - 1])
    m_arr = calc_m(alpha_arr, beta_arr, C, n)
    q = 1.136
    x_band1_arr, x_band2_arr, \
    y_band1_arr, y_band2_arr = calc_strip(x_arr, y_arr, eps, m_arr, p, n)
    return m_arr, x_band1_arr, x_band2_arr, y_band1_arr, y_band2_arr


def make_rk4_stoh_cycle(p, eps, delta, h, n):
    x_arr, y_arr, u = simple_cycle(p, delta, h)
    x2r0 = x_arr[1000]
    y2r0 = y_arr[1000]
    x2, y2, t = rk4_random(x2r0, y2r0, n, p, eps, h)
    return x2, y2


def get_max_and_min_m(p, eps, delta, h):
    p_arr = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4]
    m_max_arr = []
    m_min_arr = []
    for p in p_arr:
        print(p)
        x_arr, y_arr, n = simple_cycle(p, delta, h)
        a_arr, b_arr = a_b_calc(x_arr, y_arr, n, p)
        alpha_arr, beta_arr = alpha_beta_calc(a_arr, b_arr, n, h)
        C = (alpha_arr[n - 1] * beta_arr[n - 1]) / (1 - alpha_arr[n - 1])
        m_arr = calc_m(alpha_arr, beta_arr, C, n)
        r_m_arr = m_arr
        m_max_arr.append(max(m_arr))
        m_min_arr.append(min(m_arr))
    return m_max_arr, m_min_arr, p_arr


def get_data_for_3d(p, eps, delta, h):
    x_arr, y_arr, n = simple_cycle(p, delta, h)
    a_arr, b_arr = a_b_calc(x_arr, y_arr, n, p)
    alpha_arr, beta_arr = alpha_beta_calc(a_arr, b_arr, n, h)
    C = (alpha_arr[n - 1] * beta_arr[n - 1]) / (1 - alpha_arr[n - 1])
    print(a_arr[n - 1], b_arr[n - 1], alpha_arr[n - 1], beta_arr[n - 1], C)
    m_arr = calc_m(alpha_arr, beta_arr, C, n)
    return m_arr, x_arr, y_arr

