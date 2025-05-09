import numpy as np

from Colored_noise.color_noise_graphics import show_colored_stable_rk, \
    log_rk4_colored_max_x, log_rk4_colored_dispersion, log_rk4_colored_distribution
from graphics.deterministic_graphics import dot_attractor, transition_box
from graphics.graphics import deterministic_more_solutions, show_rk, show_stoh_stable_rk


def main(h, eps, p, q, delta, n, a):
    '''Детерминнированный случай'''
    # show_rk(n, p, q, h)
    # deterministic_more_solutions(n, p, q,h)
    # dot_attractor(n, p, q, h)
    # graphics.show_bifurcation_diagram(p, delta, h)
    # graphics.show_some_cycles(delta,h)
    # transition_box(n, p, q, h, box_coord=[0.25, 0.25, 1.75, 1.75], step=0.015)

    '''цикл в пучке жесткого случая'''
    # graphics.show_rk_with_limit_cycle(p, delta, h, n)

    '''Стохастический случай: аттрактор - точка'''
    # show_stoh_stable_rk(1, 1, n, p,q, eps, h)
    # graphics.show_dispersion_ellipse(1, 1, n, p, eps, h)
    # graphics.show_intersection_diagram(1, 1, n, p, eps, h)
    # graphics.show_W_own_nubmers(1, 1, n, p, eps, h)

    '''Стохастический случай: аттрактор - цикл'''
    # graphics.show_some_cycles(delta, h)
    # graphics.show_limit_cycle(p, delta, h)
    # graphics.show_stoh_cycle(p, eps, delta, h, n)
    # graphics.show_strip(p, eps, delta, h,n)

    # graphics.show_max_m(p, eps, delta, h)

    # graphics.show_maxmin_m(p, eps, delta, h)

    # graphics.show_3d_m(p, eps, delta, h)
    # graphics.show_FSCH_cycle(eps, delta, h)
    '''Цветной шум'''
    # show_colored_stable_rk(1, 1, n, p, q, eps, h, a)
    # log_rk4_colored_max_x(1, 1, n, p, q, eps, h, a)
    #log_rk4_colored_dispersion(1, 1, n, p, q, eps, h, a)
    log_rk4_colored_distribution(1, 1, n, p, q, eps, h, a)

    # show_rk4_colored_with_cycle(p, eps, delta, h, n, a)


if __name__ == '__main__':
    main(h=10 ** (-4), eps=10 ** (-2), p=1, q=1, delta=0.0001, n=250000, a=0.0001)
