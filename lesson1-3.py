# Задание 3. Узнайте у пользователя число n.

num = input("Enter number: ")

# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

a = int(num + num)
b = int(num + num + num)
itog = int(num) + a + b

print(itog)
