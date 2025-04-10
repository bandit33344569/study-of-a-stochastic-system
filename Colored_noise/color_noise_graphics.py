import numpy as np
from matplotlib import pyplot as plt

from Colored_noise.colored_cycle import make_rk4_colored_cycle
from Colored_noise.colored_rk4 import rk4_random_colored_noise
from deterministic_system.limitCycle import simple_cycle


def show_colored_stable_rk(x0, y0, n, p, q, eps, h, a):
    '''
    :param q:
    :param a:
    :param x0: асбцисса точки равновесия
    :param y0: оридната тчоки равновесия
    :param n:  количество итераций
    :param p:  параметр системы
    :param eps: шум системы
    :param h:   точность рунге
    :return: рисунок стохастической фазовой траектории
    '''
    x, y, z, t_arr = rk4_random_colored_noise(x0, y0, n, p, q, eps, h, a)
    plt.plot(x, y)
    # plt.axis([0.7, 1.3, 0.7, 1.3])
    plt.title(f"p={p},q = {q}, a={a}, eps={eps}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} q = {q} eps={eps} a={a}.png")
    # plt.show()
    plt.close()


def log_rk4_colored_dispersion(x0, y0, n, p, q, eps, h, a):
    '''
    рисует график дисперсии значений x, в кадом значении a, по логарифмическому масшатбу
    :param x0:
    :param y0:
    :param n:
    :param p:
    :param q:
    :param eps:
    :param h:
    :param a:
    :return:
    '''
    num_iterations = 40
    start = -4  # 10^1
    end = 4  # 10^3
    num_points_per_decade = 100
    total_points = num_points_per_decade * (end - start + 1)
    values = np.logspace(start, end, num=total_points)
    mean_deviation_values = []  # Для хранения математического ожидания отклонения от 1
    variance_values = []  # Для хранения дисперсии
    for a in values:

        sum_deviation = 0
        sum_deviation_squared = 0

        # Выполняем num_iterations итераций для каждого a
        for i in range(num_iterations):
            print(f"Processing a = {a}, i = {i}")
            x, y, z, t_arr = rk4_random_colored_noise(x0, y0, n, p, q, eps, h, a)
            x = np.array(x[10000:])  # Берем значения после 10000 шагов

            # Вычисляем абсолютное отклонение от 1
            deviation = np.abs(x - 1)

            # Накапливаем сумму отклонений и сумму квадратов отклонений
            sum_deviation += np.sum(deviation)
            sum_deviation_squared += np.sum(deviation ** 2)

        # Вычисляем математическое ожидание отклонения от 1
        num_points = (n-10000) * num_iterations
        E_deviation = sum_deviation / num_points

        # Вычисляем дисперсию отклонений
        variance = (sum_deviation_squared / num_points) - (E_deviation ** 2)

        # Сохраняем результаты
        mean_deviation_values.append(E_deviation)
        variance_values.append(variance)

    # Преобразуем списки в массивы NumPy
    mean_deviation_values = np.array(mean_deviation_values)
    variance_values = np.array(variance_values)

    # Находим значение a с максимальной дисперсией
    max_variance_index = np.argmax(variance_values)
    max_variance_a = values[max_variance_index]
    max_variance_value = variance_values[max_variance_index]

    print(f"Максимальная дисперсия: {max_variance_value:.6f} при a = {max_variance_a:.6f}")

    # Рисуем графики
    plt.xscale('log')  # Логарифмическая шкала по оси x

    # График математического ожидания отклонения от 1
    plt.plot(values, mean_deviation_values, color="r", label="Мат. ожидание |x - 1|")

    # Верхняя граница (E_deviation + sqrt(дисперсия))
    plt.plot(values, mean_deviation_values + np.sqrt(variance_values), color="b",
             label="E_deviation + σ")

    # Нижняя граница (E_deviation - sqrt(дисперсия))
    plt.plot(values, mean_deviation_values - np.sqrt(variance_values), color="b",
             label="E_deviation - σ")

    # Добавляем легенду
    plt.legend()
    plt.title(f"p={p}, q={q}, eps={eps}")
    plt.xlabel('a', fontsize=10)
    plt.ylabel('dispersion', fontsize=10)
    plt.savefig(f"p={p}, q={q}, eps={eps} dispersion.png")
    plt.show()
    plt.close()


def log_rk4_colored_max_x(x0, y0, n, p, q, eps, h, a):
    start = -3
    end = 3
    num_points_per_decade = 100
    total_points = num_points_per_decade * (end - start + 1)
    values = np.logspace(start, end, num=total_points)
    x_val = []
    for a in values:
        print(a)
        x, y, z, t_arr = rk4_random_colored_noise(1, 1, n, p, q, eps, h, a)
        x_val.append(max(x))
    plt.xscale('log')
    plt.plot(values, x_val, color="b")
    plt.title(f"p={p}, q={q}, eps={eps}")
    plt.xlabel('a', fontsize=10)
    plt.ylabel('x', fontsize=10)
    plt.savefig(f"p={p}, q={q}, eps={eps} dynamic.png")
    # plt.show()
    plt.close()
