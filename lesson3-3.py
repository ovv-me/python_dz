# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
#    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')
     my_list = [arg1, arg2, arg3]
     try:
        my_list.remove(min(my_list))
        return sum(my_list)
     except ValueError:
        return "Введите только число"


print(my_func(15, -6, 78))

# my_func(
#    int(input('Аргумент 1:')),
#    int(input('Аргумент 2:')),
#    int(input('Аргумент 3:')),
# )