# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def my_func():
    sum_result = 0
    ex = False
    while ex is False:
        number = input('Введите строку чисел через пробел, q fo exit: ').split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                result += int(number[el])
        sum_result += result
        print(f'Текущая сумма {sum_result}')
    print(f'Финальная сумма {sum_result}')


my_func()
