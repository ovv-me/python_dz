# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('less5-4.data', 'r', encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus_dict[i[0]] + '  ' + i[1])
#    print(new_file)

with open('less5-4-new.data', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)
