def f(x, y):
    return 1 - x * y


def g(x, y, p):
    # q = 0.2
    #return (p * y) * (x - (1.2 / (0.2 + y)))
    #q = 1
    return (p * y) * (x - (2 / (1 + y)))



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
    # q = 0.2
    #return (p * x + 10 * p * x * y + 25 * p * x * y * y - 6 * p) / ((1 + 5 * y) ** 2)
    # q = 1
    return p * x - ((2 * p) / ((1 + y) ** 2))
