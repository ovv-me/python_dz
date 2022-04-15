# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

ss_list = ['Зима', 'Весна', 'Лето', 'Осень']
ss_dict = {1: 'January',
           2: 'February',
           3: 'March',
           4: 'April',
           5: 'May',
           6: 'June',
           7: 'Jule',
           8: 'August',
           9: 'September',
           10: 'October',
           11: 'November',
           12: 'December'}
month = int(input("Введите месяц по номеру "))
if month == 12 or month == 1 or month == 2:
    print(f"Месяц {ss_dict[month]}", ss_list[0])
elif month == 3 or month == 4 or month == 5:
    print(f"Месяц {ss_dict[month]}", ss_list[1])
elif month == 6 or month == 7 or month == 8:
    print(f"Месяц {ss_dict[month]}", ss_list[2])
elif month == 9 or month == 10 or month == 11:
    print(f"Месяц {ss_dict[month]}", ss_list[3])
else:
    print("Такого месяца нет")
