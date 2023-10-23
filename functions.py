def f(x, y):
    return 1 - x * y


def g(x, y, p):
    # q = 0.3
    # return (p * y) * (x - (1.3 / (0.3 + y)))
    # q = 0.5
    # return (p * y) * (x - (1.5 / (0.5 + y)))
    # q = 1
    #return (p * y) * (x - (2 / (1 + y)))
    # q=0.1
    return (p * y) * (x - (1.1 / (0.1 + y)))


def fx(x, y):
    '''
    :return: производная f по x
    '''
    return -y


def fy(x, y):
    '''
    :return: производная f по y
    '''
    return -x


def gx(x, y, p):
    '''
    :return: производная g по x
    '''
    return p * y


def gy(x, y, p):
    '''
    :return: производная g по y
    '''

    # q = 1
    #return p * x - ((2 * p) / ((1 + y) ** 2))
    # q = 0.5
    # return p * x - ((3 * p) / ((1 + 2 * y) ** 2))
    # q = 0.3
    # return p * x - ((39 * p) / ((3 + 10 * y) ** 2))
    # q = 0.1
    return (p * x + 20 * p * x * y + 100 * p * x * y * y - 11 * p) / ((1 + 10 * y) ** 2)
