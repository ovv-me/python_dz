# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("test_1.txt", "w", encoding="utf-8") as my_f_1:
    while True:
        line = input("Введите строки: ")
        if not line:
            break
        my_f_1.write(f"{line}\n")
