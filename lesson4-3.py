# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

my_list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне [20..240): ", my_list)
