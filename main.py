import graphics


def main(h, eps, p, delta, n):
    '''Детерминнированный случай'''
    # graphics.show_rk(1000000, p, h)
    # graphics.show_bifurcation_diagram(p, delta, h)

    '''Стохастический случай: аттрактор - точка'''
    # graphics.show_stoh_stable_rk(1, 1, n, p, eps, h)
    # graphics.show_dispersion_ellipse(1, 1, 10000000, p, eps, h)
    # graphics.show_intersection_diagram(1, 1, n, p, eps, h)

    '''Стохастический случай: аттрактор - цикл'''
    graphics.show_some_cycles(delta, h)
    # graphics.show_limit_cycle(p, delta, h)
    # graphics.show_stoh_cycle(p, eps, delta, h, 50000000)
    # graphics.show_strip(p, eps, delta, h)
    # graphics.show_maxmin_m(p, eps, delta, h)
    # graphics.show_3d_m(p, eps, delta, h)
    # graphics.show_FSCH_cycle(eps, delta, h)


if __name__ == '__main__':
    main(h=0.0001, eps=0.005, p=0.9, delta=0.0001, n=5000000)
