import matplotlib.pyplot as plt

def fibonacci_sequence(N):
    fib_sequence = [0, 1]  # Первые два числа Фибоначчи
    for i in range(2, N):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

if __name__ == "__main__":
    N = int(input("enter N\n"))
    fib_sequence = fibonacci_sequence(N)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, N + 1), fib_sequence, marker='o', linestyle='-')
    plt.title(f'Последовательность Фибоначчи ({N} чисел)')
    plt.xlabel('Номер числа Фибоначчи')
    plt.ylabel('Значение числа Фибоначчи')
    plt.grid(True)
    plt.show()