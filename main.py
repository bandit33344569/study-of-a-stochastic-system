import graphics
from Colored_noise.color_noise_graphics import show_colored_stable_rk, show_rk4_colored_with_cycle


def main(h, eps, p, delta, n, a):
    '''Детерминнированный случай'''
    # graphics.show_rk(n, p, h)
    # graphics.show_bifurcation_diagram(p, delta, h)
    # graphics.show_some_cycles(delta,h)

    '''цикл в пучке жесткого случая'''
    # graphics.show_rk_with_limit_cycle(p, delta, h, n)

    '''Стохастический случай: аттрактор - точка'''
    # graphics.show_stoh_stable_rk(1, 1, n, p, eps, h)
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
    #show_colored_stable_rk(1, 1, n, p, eps, h, a)
    show_rk4_colored_with_cycle(p, eps, delta, h, n, a)

if __name__ == '__main__':
    main(h=0.0001, eps=0.001, p=12, delta=0.0001, n=3000000, a=10000)
