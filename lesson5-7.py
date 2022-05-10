# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# A - Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# B - Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# C - Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

dic = []
with open('less5-7.data', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    prof = {}
    prof_sum = 0
    count_minus = 0
    for k in file:
        items = k.split(' ')
        polza = int(items[2]) - int(items[3])
        prof.update({items[0]: polza})
        if polza > 0:
            prof_sum += polza
        else:
            count_minus += 1
    dic.append(prof)
    dic.append({'average_profit': '{:.2f}'.format(prof_sum / (len(prof)-count_minus))})

with open('less5-7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(dic, json_file, ensure_ascii=False)

print(f"Словарь:\n{dic}\n")
