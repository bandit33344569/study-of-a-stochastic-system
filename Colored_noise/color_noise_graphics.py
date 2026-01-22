import pickle

import numpy as np
from matplotlib import pyplot as plt
import csv

from Colored_noise.FSCH_color import calculate_eigen_value, find_W_color, calculate_w, get_colored_ellipse_points
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
    plt.axis([0, 25, 0, 25])
    plt.title(f"p={p},q = {q}, a={a}, eps={eps}")
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.savefig(f"p={p} q = {q} eps={eps} a={a}.png")
    # plt.show()
    plt.close()


def log_rk4_colored_distribution(x0, y0, n, p, q, eps, h, a):
    start = -4
    end = 4
    num_points_per_decade = 300
    points = 200
    step = int((n - 10000) / points)
    total_points = num_points_per_decade * (end - start + 1)
    a_range = np.logspace(start, end, num=total_points)
    results = {
        'a': [],
        'x': [],
        'y': []
    }

    # Вычисления
    for a in a_range:
        print(a)
        x, y, z, t_arr = rk4_random_colored_noise(x0, y0, n, p, q, eps, h, a)
        results['a'].append(a)
        results['x'].append(x[10000::step])  # Сохраняем только после 10000 шагов
        results['y'].append(y[10000::step])

    # Сохранение данных
    filename = f"data_p{p}_q{q}_eps{eps}.pkl"
    with open(filename, "wb") as f:
        pickle.dump(results, f)

    # График для x
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    for i, x_vals in enumerate(results['x']):
        ax1.plot([a_range[i]] * len(x_vals), x_vals, 'b.', markersize=3)
    ax1.set_xscale('log')
    ax1.set_title(f"(p={p}, q={q}, ε={eps})")
    ax1.set_xlabel('a')
    ax1.set_ylabel('x')
    fig1.tight_layout()
    fig1.savefig(f"x_p{p}_q{q}_eps{eps}_distribution.png", dpi=300, bbox_inches='tight')
    plt.close(fig1)

    # График для y
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    for i, y_vals in enumerate(results['y']):
        ax2.plot([a_range[i]] * len(y_vals), y_vals, 'r.', markersize=3)
    ax2.set_xscale('log')
    ax2.set_title(f"y vs a\n(p={p}, q={q}, ε={eps})")
    ax2.set_xlabel('a (log scale)')
    ax2.set_ylabel('y')
    fig2.tight_layout()
    fig2.savefig(f"y_p{p}_q{q}_eps{eps}_distribution.png", dpi=300, bbox_inches='tight')
    plt.close(fig2)


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
    num_iterations = 1
    start = -4
    end = 4
    num_points_per_decade = 200
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
        num_points = (n - 10000) * num_iterations
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
    # Сохраняем данные в файл CSV
    with open(f'data_p={p}_q={q}_eps={eps}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['a', 'Mean Deviation', 'Variance'])  # Заголовок
        for a_val, mean_dev, var in zip(values, mean_deviation_values, variance_values):
            writer.writerow([a_val, mean_dev, var])

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
    plt.savefig(f"p={p}, q={q}, eps={eps} dispersion2.png")
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


def paint_eigen_values_color(x0, y0, n, p, q, eps, h, a):
    start = -4
    end = 4
    num_points_per_decade = 200
    total_points = num_points_per_decade * (end - start + 1)
    values = np.logspace(start, end, num=total_points)
    lambda1_arr = []
    lambda2_arr = []
    w11_sym, w12_sym, w21_sym, w22_sym = find_W_color()
    for a in values:
        print(a)
        w11, w12, w21, w22 = calculate_w(eps, a, p, q, w11_sym, w12_sym, w21_sym, w22_sym)
        lambda1, lambda2 = calculate_eigen_value(w11, w12, w21, w22)
        lambda1_arr.append(lambda1)
        lambda2_arr.append(lambda2)

    print(max(lambda1_arr))
    print(max(lambda2_arr))
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(values, lambda1_arr, label=r'$\lambda_1$', color='blue')
    ax1.set_title(f"q={q},p={p},eps={eps}", fontsize=14)
    ax1.set_ylabel(r'$\lambda_1$', fontsize=12)
    ax1.set_xlabel(r'Параметр $a$', fontsize=12)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax1.set_xscale('log')
    ax1.legend()
    fig1.savefig(f"eigen_value_lambda1_q={q},p={p},eps={eps}.png")
    plt.close(fig1)

    # График для lambda2
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(values, lambda2_arr, label=r'$\lambda_2$', color='green')
    ax2.set_title(f'q={q},p={p},eps={eps}', fontsize=14)
    ax2.set_ylabel(r'$\lambda_2$', fontsize=12)
    ax2.set_xlabel(r'Параметр $a$', fontsize=12)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.set_xscale('log')
    ax2.legend()
    fig2.savefig(f"eigen_value_lambda2_q={q},p={p},eps={eps}.png")
    plt.close(fig2)


def compare_eigen_values(x0, y0, n, p, eps, h, ):
    q_values = [0.1, 1]
    start, end = -4, 4
    num_points_per_decade = 200
    total_points = num_points_per_decade * (end - start + 1)
    a_values = np.logspace(start, end, num=total_points)

    results = {q: {'lambda1': [], 'lambda2': []} for q in q_values}

    for q in q_values:
        w11_sym, w12_sym, w21_sym, w22_sym = find_W_color()
        for a in a_values:
            w11, w12, w21, w22 = calculate_w(eps, a, p, q, w11_sym, w12_sym, w21_sym, w22_sym)
            lambda1, lambda2 = calculate_eigen_value(w11, w12, w21, w22)
            results[q]['lambda1'].append(lambda1)
            results[q]['lambda2'].append(lambda2)

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    fig2, ax2 = plt.subplots(figsize=(10, 5))

    colors = {'0.1': 'blue', '1.0': 'red'}

    for q in q_values:
        color = colors.get(str(q), 'black')
        ax1.plot(a_values, results[q]['lambda1'], label=f'q = {q}', color=color)
        ax2.plot(a_values, results[q]['lambda2'], label=f'q = {q}', color=color)

    ax1.set_title(f'Сравнение $\lambda_1$ при разных $q$', fontsize=14)
    ax1.set_ylabel(r'$\lambda_1$', fontsize=12)
    ax1.set_xlabel(r'Параметр $a$', fontsize=12)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax1.set_xscale('log')
    ax1.legend()

    ax2.set_title(f'Сравнение $\lambda_2$ при разных $q$', fontsize=14)
    ax2.set_ylabel(r'$\lambda_2$', fontsize=12)
    ax2.set_xlabel(r'Параметр $a$', fontsize=12)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.set_xscale('log')
    ax2.legend()

    # Сохранение графиков
    fig1.savefig(f"compare_lambda1_q={q_values[0]}_vs_{q_values[1]}_p={p}_eps={eps}.png")
    fig2.savefig(f"compare_lambda2_q={q_values[0]}_vs_{q_values[1]}_p={p}_eps={eps}.png")

    plt.close(fig1)
    plt.close(fig2)


def show_colored_trajectory_with_ellipse(x0, y0, n, p, q, eps, h, a, P=0.95):
    """
    ОТДЕЛЬНАЯ функция: рисует стохастическую траекторию + доверительный эллипс.

    Использование в main():
    show_colored_trajectory_with_ellipse(1, 1, n, p, q, eps, h, a)
    """
    from Colored_noise.colored_rk4 import rk4_random_colored_noise
    from Colored_noise.FSCH_color import find_W_color, calculate_w
    import matplotlib.pyplot as plt

    # 1. Генерируем стохастическую траекторию
    x, y, z, t_arr = rk4_random_colored_noise(x0, y0, n, p, q, eps, h, a)

    # 2. Создаем график
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'b-', alpha=0.6, linewidth=0.8)

    # 3. Предварительно считаем символьные выражения (один раз)
    w_syms = find_W_color()

    # 4. Получаем координаты эллипса
    x_ell, y_ell = get_colored_ellipse_points(p, q, eps, a, center_x=1.0, center_y=1.0, P=P, w_syms=w_syms)

    # 5. Рисуем эллипс и центр
    if x_ell:
        plt.plot(x_ell, y_ell, 'r-', linewidth=1, label=f'доверительный эллипс P={P}')

    # 6. Оформление
    plt.axis([0, 25, 0, 25])
    plt.title(f'p={p}, q={q}, a={a}, eps={eps}', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.axis('equal')

    # 7. Сохранение
    plt.savefig(f"p={p}_q={q}_eps={eps}_a={a}_trajectory_ellipse.png", dpi=300, bbox_inches='tight')
    plt.close()
