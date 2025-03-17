from Colored_noise.colored_rk4 import rk4_random_colored_noise
from deterministic_system.limitCycle import simple_cycle


def make_rk4_colored_cycle(p, eps, delta, h, n, a):
    x_arr, y_arr, u = simple_cycle(p, delta, h)
    x2r0 = x_arr[10]
    y2r0 = y_arr[10]
    x2, y2, t = rk4_random_colored_noise(x2r0, y2r0, n, p, eps, h, a)
    return x2, y2, x_arr, y_arr


