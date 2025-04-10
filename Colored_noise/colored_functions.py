import math
import random

from sympy import symbols, diff


def f1(x, y, z, eps):
    return 1 - x * y + eps * z


def f2(x, y, z, p, q, eps):
    return (p * y) * (x - ((1 + q) / (q + y)))


def f3(x, y, z, p, q, a, h):
    #u1 = random.uniform(0, 1)
    #u2 = random.uniform(0, 1)
    return -a * z #+ math.sqrt(2*a) * math.sqrt(h) * math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
