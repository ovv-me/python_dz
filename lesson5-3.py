# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

basa = []
sum_salaries = 0
with open('less5_3.data', 'r', encoding='UTF-8') as file:
    st = file.readlines()
#    print("Оклады сотрудников")
    for row in st:
        items = row.split(' ')
        basa.append([items[0], int(items[1])])
#        print(f"{items[0]}: {int(items[1])} руб.")
        sum_salaries += int(items[1])

print("\nСотрудники с окладом менее 20000 руб.")
[print(worker[0]) for worker in basa if worker[1] < 20000]

print(f"\nСредний оклад сотрудников {sum_salaries / len(basa):.2f} руб.")
