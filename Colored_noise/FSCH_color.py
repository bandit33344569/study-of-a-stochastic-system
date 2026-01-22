import numpy as np
import sympy as sp
from numpy.linalg import inv



def find_W_color():
    a, p, q = sp.symbols('a p q')

    # Матрица Якоби F
    F = sp.Matrix([
        [-1, -1],
        [p, p / (1 + q)]
    ])

    # Вектор чувствительности к шуму g
    g = sp.Matrix([1, 0])
    # Единичная матрица
    I = sp.eye(2)
    # Обратные матрицы
    inv_F_T_minus_aI = (F.T - a * I).inv()
    inv_F_minus_aI = (F - a * I).inv()
    # Члены уравнения
    term1 = (g * g.T) * inv_F_T_minus_aI
    term2 = (inv_F_minus_aI * g) * g.T

    # Матричное уравнение: F*W + W*F.T - term1 - term2 = 0
    # Определение символов для элементов матрицы W
    w11, w12, w21, w22 = sp.symbols('w11 w12 w21 w22')
    W = sp.Matrix([
        [w11, w12],
        [w21, w22]
    ])

    # Составление уравнения
    equation = F * W + W * F.T - term1 - term2

    # Решение системы уравнений
    solutions = sp.solve(equation, (w11, w12, w21, w22))

    # Извлечение решений в отдельные переменные
    w11_sol = sp.simplify(sp.factor(solutions[w11]))
    w12_sol = sp.simplify(sp.factor(solutions[w12]))
    w21_sol = sp.simplify(sp.factor(solutions[w21]))
    w22_sol = sp.simplify(sp.factor(solutions[w22]))

    print(w11_sol)
    print(w12_sol)
    print(w21_sol)
    print(w22_sol)

    # Возврат решений
    return w11_sol, w12_sol, w21_sol, w22_sol


'''
    # Вывод решений
    print("Решение для элементов матрицы W:")
    for key, value in solutions.items():
        print(f"{key} = {sp.simplify(sp.factor(value))}")
'''


def calculate_w(epsilon, a_val, p_val, q_val, w11_sym, w12_sym, w21_sym, w22_sym):
    # Определение символов
    a, p, q = sp.symbols('a p q')

    # Подстановка значений
    w11 = w11_sym.subs({a: a_val, p: p_val, q: q_val}) * epsilon ** 2
    w12 = w12_sym.subs({a: a_val, p: p_val, q: q_val}) * epsilon ** 2
    w21 = w21_sym.subs({a: a_val, p: p_val, q: q_val}) * epsilon ** 2
    w22 = w22_sym.subs({a: a_val, p: p_val, q: q_val}) * epsilon ** 2
    # Преобразование в числа
    return (
        float(w11.evalf()),
        float(w12.evalf()),
        float(w21.evalf()),
        float(w22.evalf())
    )


def calculate_eigen_value(w11, w12, w21, w22):
    W = np.array([[w11, w12], [w21, w22]])
    eigenvalues = np.linalg.eigvalsh(W)
    lambda1, lambda2 = eigenvalues
    return lambda1, lambda2


def get_colored_ellipse_points(p, q, eps, a, center_x=1.0, center_y=1.0, P=0.95, w_syms=None):
    """
    Возвращает координаты (x, y) точек доверительного эллипса.

    Параметры:
      P: доверительная вероятность (например, 0.95 для 95%).
      w_syms: результат find_W_color() (чтобы не пересчитывать каждый раз).
    """
    # 1. Если символьные решения не переданы, считаем их (это может быть долго)
    if w_syms is None:
        w_syms = find_W_color()

    w11_s, w12_s, w21_s, w22_s = w_syms

    # 2. Вычисляем числовую матрицу ковариации
    # calculate_w уже учитывает умножение на eps^2
    w11, w12, w21, w22 = calculate_w(eps, a, p, q, w11_s, w12_s, w21_s, w22_s)
    W_num = np.array([[w11, w12],
                      [w21, w22]], dtype=float)

    # 3. Собственные числа и векторы
    # Собственные числа ковариационной матрицы — это дисперсии вдоль главных осей
    vals, vecs = np.linalg.eig(W_num)

    # Сортируем для порядка (lambda1 - большее, lambda2 - меньшее)
    idx = vals.argsort()[::-1]
    lambdas = vals[idx]
    V = vecs[:, idx]

    lambda1, lambda2 = lambdas[0], lambdas[1]
    v1, v2 = V[:, 0], V[:, 1]  # Собственные векторы (столбцы)

    # Проверка на положительную определенность
    if lambda1 <= 0 or lambda2 <= 0:
        print(f"Warning: Non-positive eigenvalues: {lambda1}, {lambda2}. Ellipse cannot be built.")
        return [], []

    # 4. Масштабный множитель (квантиль хи-квадрат распределения)
    # R^2 = -2 * ln(1 - P)
    # Для P=0.95 это ~5.99, для P=0.99 это ~9.21
    scale_factor = -2 * np.log(1 - P)

    # Длины полуосей
    r1 = np.sqrt(scale_factor * lambda1)
    r2 = np.sqrt(scale_factor * lambda2)

    # 5. Генерация точек по параметрическому уравнению
    # r(theta) = Center + r1*cos(theta)*v1 + r2*sin(theta)*v2
    theta = np.linspace(0, 2 * np.pi, 200)
    x_arr = []
    y_arr = []

    for t in theta:
        point = np.array([center_x, center_y]) + \
                r1 * np.cos(t) * v1 + \
                r2 * np.sin(t) * v2
        x_arr.append(point[0])
        y_arr.append(point[1])

    return x_arr, y_arr

