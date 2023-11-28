import graphics


def main(h, eps, p, delta):
    # graphics.show_rk(1000000, p, h)
    #graphics.show_limit_cycle(p, delta, h)
    # graphics.show_stoh_stable_rk(1, 1, 10000000, p, eps, h)
    # graphics.show_strip(p, eps, delta, h)
    # graphics.show_maxmin_m(p, eps, delta, h)
    # graphics.show_3d_m(p, eps, delta, h)
    # graphics.show_dispersion_ellipse(1, 1, 10000000, p, eps, h)
    # graphics.show_bifurcation_diagram(p, delta, h)

    graphics.show_stoh_cycle(p, eps, delta, h, 50000000)


if __name__ == '__main__':
    main(h=0.00001, eps=0.001, p=1.2, delta=0.00001)
