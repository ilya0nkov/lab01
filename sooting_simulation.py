import random
import math
import matplotlib.pyplot as plt


def run_simulation(alpha, L, mv, sigma_v, m_alpha, sigma_alpha, num_trials, delta):
    distances = []
    hits_counter = 0

    for i in range(1, num_trials + 1):
        v = random.gauss(mv, sigma_v)
        alpha_deg = random.gauss(m_alpha, sigma_alpha)
        alpha_rad = math.radians(alpha_deg)

        range_ = (v ** 2 * math.sin(2 * alpha_rad)) / 9.8

        if L - delta / 2 <= range_ <= L + delta / 2:
            hits_counter += 1

        distances.append(range_)

    hit_probability = hits_counter / num_trials
    print(f"Всего попаданий в мишень размером {delta}: {hits_counter}, Вероятность попадания: {hit_probability:.4f}")

    return distances


def main():
    alpha = 45
    L = 1000
    mv = 100
    sigma_v = 10
    m_alpha = 45
    sigma_alpha = 5
    num_trials = 5000
    delta = 20

    distances = run_simulation(alpha, L, mv, sigma_v, m_alpha, sigma_alpha, num_trials, delta)

    # Построение графиков
    means = [sum(distances[:i]) / i for i in range(1, num_trials + 1)]
    variances = [sum((x - means[i - 1]) ** 2 for x in distances[:i]) / i for i in range(1, num_trials + 1)]

    plt.figure(figsize=(18, 5))

    plt.subplot(1, 3, 1)
    plt.plot(range(1, num_trials + 1), means, label='Средняя дальность')
    plt.xlabel('Число испытаний')
    plt.ylabel('Средняя дальность')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(range(1, num_trials + 1), variances, label='Дисперсия')
    plt.xlabel('Число испытаний')
    plt.ylabel('Дисперсия')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.hist(distances, bins=50, density=True, alpha=0.7, color='blue')
    plt.title('Гистограмма распределения дальности выстрела')
    plt.xlabel('Дальность выстрела (м)')
    plt.ylabel('Плотность вероятности')

    plt.suptitle(f"Средняя дальность выстрела: {means[-1]:.2f} м\nДисперсия: {variances[-1]:.2f}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
