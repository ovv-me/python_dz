# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, hours, money_per_hour, prem = argv


def salary(hours1, money_hour1, prem1):
    try:
        result = (int(hours1) * float(money_hour1)) + float(prem1)
    except ValueError:
        return
    return result


print(f"Зарплата {salary(hours, money_per_hour, prem)}")
