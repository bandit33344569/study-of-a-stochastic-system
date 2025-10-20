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

