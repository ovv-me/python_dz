# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open('less5-5.new', 'w', encoding='utf-8') as file:
    for i in range(7):
        num = random.randint(0, 20)
        file.write(str(num) + ' ')

with open('less5-5.new', 'r', encoding='UTF-8') as file:
    count_str = file.read()
    count_lst = count_str.split()
    print(f"Содержимое файла:\n{count_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in count_lst])}")
