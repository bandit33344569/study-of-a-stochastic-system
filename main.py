import graphics


def main(h, eps, p, delta):
    #graphics.show_rk(100000, p, h)
    # graphics.show_limit_cycle(p, 0.0001, h)
    #graphics.show_stoh_stable_rk(1, 1, 100000, p, eps, h)
    graphics.show_strip(p, eps, delta, h)
    #graphics.show_maxmin_m(p, eps, delta, h)
    #graphics.show_3d_m(p, eps, delta, h)



if __name__ == '__main__':
    main(h=0.0001, eps=0.002, p=2.2, delta=0.001)
