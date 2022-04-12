# Задача 5. Запросите у пользователя значения выручки и издержек фирмы.

revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

if revenue > costs:
    profit = revenue-costs
    print(f"Есть прибыль {profit} !")
elif revenue == costs:
    print("Прибыль равна издержкам! Вышли на точку безубыточности!")
else:
    profit = abs(revenue - costs)
    print(f"Фирма ушла в минус! Убыток {profit} !")
