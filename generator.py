import math
import time
import random

class LinearCongruentialGenerator:

    def __init__(self, seed, k, b, m):
        self.r = seed
        self.k = k
        self.b = b
        self.m = m

    def generate(self, n):
        random_numbers = []

        for _ in range(n):
            self.r = (self.k * self.r + self.b) % self.m
            random_numbers.append(self.r / self.m)

        return random_numbers

def getMean(random_numbers, n):
    # Вычисление математического ожидания
    return sum(random_numbers) / n

def getVariance(random_numbers, mean, n):
    # Вычисление дисперсии
    return sum((x - mean) ** 2 for x in random_numbers) / n

def getCountInterval(random_numbers, x1, x2):
    # Вычисление количества чисел, попавших в интервал [0, 0.5]
    return sum(1 for x in random_numbers if x1 <= x <= x2)

def GSPH(random_numbers):
    # Определение длины периода ГСПЧ

    period_length = 0
    seen = set()
    for num in random_numbers:
        period_length += 1
        if num in seen:
            print(f'Был обнаружен повтор: {num}')
            break
        seen.add(num)

    return period_length

def compare_with_builtin_generator(n):
    random.seed(int(time.time()))
    random_numbers = [random.random() for _ in range(n)]

    print('[Генерация при помощи встроенной бибтиотеки]')

    # Вычисление математического ожидания
    mean = getMean(random_numbers, n)
    print("Математическое ожидание:", mean)

    # Вычисление дисперсии
    variance = getVariance(random_numbers, mean, n)
    print("Дисперсия:", variance)

    # Вычисление среднеквадратичного отклонения
    std_division = math.sqrt(variance)
    print("Среднеквадратическое отклонение:", std_division)

    # Вычисление количества чисел, попавших в интервал [0, 0.5]
    count_in_interval = getCountInterval(random_numbers, 0, 0.5)
    print(f"Процент чисел в интервале [0, 0.5]: {count_in_interval / n * 100}%")

    # Прохождении частотного теста
    count_in_interval = getCountInterval(random_numbers, mean - std_division, mean + std_division)
    print(f"Прохождении частотного теста: {count_in_interval / n * 100}%")

    # Определение длины периода ГСПЧ
    print("Длина периода ГСПЧ (количество чисел до первого повторения):", GSPH(random_numbers))

def main():
    # начальное значение, зерно
    seed = 42
    # множитель
    k = 1664525
    # приращение
    b = 1013904223
    # модуль
    m = 2**32

    # Количество генерируемых чисел
    n = 1000000

    lcg = LinearCongruentialGenerator(seed, k, b, m)
    random_numbers = lcg.generate(n)

    print('[Ручная генерация]')

    # Вычисление математического ожидания
    mean = getMean(random_numbers, n)
    print("Математическое ожидание:", mean)

    # Вычисление дисперсии
    variance = getVariance(random_numbers, mean, n)
    print("Дисперсия:", variance)

    # Вычисление среднеквадратичного отклонения
    std_division = math.sqrt(variance)
    print("Среднеквадратическое отклонение:", std_division)

    # Вычисление количества чисел, попавших в интервал [0, 0.5]
    count_in_interval = getCountInterval(random_numbers, 0, 0.5)
    print(f"Процент чисел в интервале [0, 0.5]: {count_in_interval / n * 100}%")

    # Прохождении частотного теста
    count_in_interval = getCountInterval(random_numbers, mean - std_division, mean + std_division)
    print(f"Прохождении частотного теста: {count_in_interval / n * 100}%")

    # Определение длины периода ГСПЧ
    print("Длина периода ГСПЧ (количество чисел до первого повторения):", GSPH(random_numbers))

    print('\n###############################\n')

    # Сравнение с встроенным генератором
    compare_with_builtin_generator(n)

if __name__ == "__main__":
    main()
