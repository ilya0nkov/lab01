def euclidean(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


if __name__ == "__main__":
    num1 = int(input('Введите делимое число:\n'))
    num2 = int(input('Введите делитель:\n'))
    print('НОД: ', euclidean(num1, num2))