import os
import random
import  re
import matplotlib.pyplot as plt
import numpy as np

def print_char_list(array):
    for i in range(len(array)):
        print(array[i])


def task1():
    n = int(input("Введите длину массива "))
    array = ['a'] * n  # создает массив символов длиной n
    for i in range(n):
        input_value = str(input("Введите элемент массива "))  # в питоне по сути нет chr,
        # это почти то же самое что и str
        if len(input_value) > 1:  # char это 1 символ, так что обрезаем, если символов больше
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

def preobrazovanie(array):
    rows = len(array)
    cols = len(array[0])

    for i in range(rows):
        for j in range(cols):
            if array[i][j] != ' ':
                current_char = array[i][j]
                count = 1

                # Проверка вправо
                for k in range(j + 1, cols):
                    if array[i][k] == current_char:
                        count += 1
                    else:
                        break

                # Замена символов
                for k in range(j, j + count):
                    array[i][k] = str(count)

                # Проверка вниз
                for k in range(i + 1, rows):
                    if array[k][j] == current_char:
                        array[k][j] = str(count)
                    else:
                        break

def generate_random_2d_array(n):
    symbols = ['.', '*']
    array = [[random.choice(symbols) for _ in range(n + 1)] for _ in range(n + 1)]
    return array

def task2():
    n = int(input("Введите n: "))

    array = generate_random_2d_array(n)

    print("Исходный массив:")
    print_char_2d_array(array)

    preobrazovanie(array)

    print("\nМассив после преобразования:")
    print_char_2d_array(array)


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


def task7():
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    os.chdir(data_dir)

    file_path = "data/directory.txt"

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

        # Создание файл
        with open(path, "w") as new_file:
            new_file.write(f"Contens of {file_name}")

    print("Файловая структура успешно создана.")


def display_menu():
    print("Выберите действие:")
    print("1. Создать файл")
    print("2. Удалить файл")
    print("3. Создать директорию")
    print("4. Удалить директорию")


def create_file():
    filename = input("Введите имя файла: ")
    with open(filename, 'w'):
        print(f"Файл {filename} создан.")


def delete_file():
    filename = input("Введите имя файла для удаления: ")
    try:
        os.remove(filename)
        print(f"Файл {filename} удален.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


def create_directory():
    dirname = input("Введите имя директории: ")
    os.mkdir(dirname)
    print(f"Директория {dirname} создана.")


def delete_directory():
    dirname = input("Введите имя директории для удаления: ")
    try:
        os.rmdir(dirname)
        print(f"Директория {dirname} удалена.")
    except FileNotFoundError:
        print(f"Директория {dirname} не найдена.")
    except OSError as e:
        print(f"Ошибка при удалении директории {dirname}: {e}")


def task8():
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    os.chdir(data_dir)

    while True:
        display_menu()
        choice = input("Введите номер действия (или 'q' для выхода): ")

        if choice == '1':
            create_file()
        elif choice == '2':
            delete_file()
        elif choice == '3':
            create_directory()
        elif choice == '4':
            delete_directory()
        elif choice.lower() == 'q':
            print("Неверный выбор. Попробуйте снова.")


def task6():
    file_path = "variant8.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Находим строку, содержащую ключевое слово NODE
    node_line_index = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("NODE"):
            node_line_index = i
            break

    if node_line_index is None:
        print("Ключевое слово NODE не найдено в файле.")
        return

    # Получаем названия столбцов данных
    column_names_line = lines[node_line_index].strip().split()[1:]

    # Создаем массивы данных
    data_arrays = {name: [] for name in column_names_line}

    # Заполняем массивы данными из файла
    for line in lines[node_line_index + 1:]:
        # Разделение значений, учитывая, что они могут быть приклеены друг к другу
        values = re.findall(r'-?\d+\.\d+E[+-]\d+', line)
        for name, value in zip(column_names_line, values):
            data_arrays[name].append(float(value))

    # Создаем папку "data", если её нет
    data_folder = "data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Создаем файлы характеристик с расширением .dat в папке "data"
    for name, data in data_arrays.items():
        output_file_path = os.path.join(data_folder, f"{name}.dat")
        with open(output_file_path, 'w') as output_file:
            for value in data:
                output_file.write(f"{value}\n")

        print(f"Файл {output_file_path} создан.")

    # Выводим значения в виде графиков
    for name, data in data_arrays.items():
        plt.plot(data, label=name)

    plt.legend()
    plt.xlabel("Индекс")
    plt.ylabel("Значение")
    plt.title("Графики массивов данных")
    plt.show()

if __name__ == "__main__":
    task2()
