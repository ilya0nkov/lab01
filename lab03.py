import os
import random


def print_char_list(array):
    for i in range(len(array)):
        print(array[i])


def task1():
    n = int(input("Введите длину массива "))
    array = ['a'] * n  # создает массив символов длиной n
    for i in range(n):
        input_value = str(input("Введите элемент массива "))  # в питоне по сути нет chr,
        # это почти то же самое что и str
        if len(input_value) > 1: # char это 1 символ, так что обрезаем, если символов больше
            input_value = input_value[:1]
        array[i] = input_value
    print_char_list(array)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:  # ошибка будет если символ не имеет представления в виде int (например int("1") == 1)
        for i in range(n):
            if int(array[i]) in numbers:
                array[i] = "*"
    except:  # если ошибка, то просто пропускаем и идем дальше по циклу
        pass
    print("\n")
    print_char_list(array)


def print_char_2d_array(array):
    for i in range(len(array[0])):
        output = ""
        for j in range(len(array)):
            output += str(array[i][j]) + " "
        print(output)


'''
def preobrazovanie(array):
    rows = len(array)
    cols = len(array[0])

    for i in range(rows):
        for j in range(cols):
            current_char = array[i][j]

            if current_char == "*":
                count = 1

                # Поиск односвязных последовательностей вокруг текущего символа "*"
                for x in range(i + 1, rows):
                    if x < rows and array[x][j] == "*":
                        count += 1
                    else:
                        break

                for y in range(j + 1, cols):
                    if y < cols and array[i][y] == "*":
                        count += 1
                    else:
                        break

                # Замена односвязной последовательности символом числа повторений
                for x in range(i, i + count):
                    for y in range(j, j + count):
                        if x < rows and y < cols:
                            array[x][y] = str(count)


def task2():
    n = int(input("Введите длину массива n-1 "))
    base_chars = ["*", "."]
    array = [[random.choice(base_chars) for i in range(n + 1)] for j in range(n + 1)]

    print_char_2d_array(array)
    preobrazovanie(array)
    print_char_2d_array(array)
'''


def task3():
    file_path = "text.txt"  # если файл не в проекте, то нужен полный путь до файла вида C:\
                             # (не помню какой из слешей \/)
    input_value = str(input("Введите текст:\n"))
    with open(file_path, "w") as file:
        file.write(input_value)


def print_string_list(array):
    for word in array:
        print(word)


def random_choise(array):
    return random.choice(array)


def task4():
    physical_terms = [
        "Температура",
        "Энергия",
        "Скорость",
        "Масса",
        "Сила",
        "Давление",
        "Электричество",
        "Магнитизм",
        "Импульс",
        "Относительность",
        "Частота",
        "Сопротивление"
    ]
    print_string_list(physical_terms)
    while True:
        choice = random_choise(physical_terms)
        input_value = str(input("Для получания случайного элемента массива нажмите Enter: "))
        if input_value == "":
            print(choice)
        else:
            break


def task5():
    file_path = "task1.out"
    input_value = str(input("Введите текст:\n"))
    with open(file_path, "w") as file:
        file.write(input_value)


def task6():
    file_path = "variant8.txt"
    '''
    with open(file_path, "r") as file:
        count_lines = 0
        target_line = ""
        for line in file:
            if "NODE" in line:
                target_line = line
            count_lines += 1
        # создаем массив названий характеристик
        specifications = target_line.split()
        # создаем массивы по названиям характеристик
        specifications_dict = {}
        for word in specifications:
            specifications_dict[word] = []
    '''
    with open(file_path, "r") as file:
        # Читаем строки из файла и удаляем символы новой строки
        index = 0
        for line in file:
            if "NODE" in line:
                target_line = line
                index += 1
        print(index)

        lines = [line.strip() for line in file.readlines()]

    # Создаем двумерный массив, разбивая каждую строку на слова
    two_dimensional_array = [line.split() for line in lines]
    for row in two_dimensional_array:
        print(row)




def task7():
    file_path = "directory.txt"

    # Чтение исходного файла и запись путей в массив строк
    with open(file_path, "r") as file:
        paths = [line.strip() for line in file.readlines()]

    # Создание структуры директорий и файлов
    for path in paths:
        # Получение директории и имени файла
        folder, file_name = os.path.split(path)

        # Создание директории (если не существует)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        # Создание файла
        with open(path, "w") as new_file:
            new_file.write(f"Contens of {file_name}")

    print("Файловая структура успешно создана.")


if __name__ == "__main__":
    # array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print_char_2d_array(array)
    task7()