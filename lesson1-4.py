# Задача 4. Пользователь вводит целое положительное число.

num = input("Enter number: ")

# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

x = 0
for n in str(num):
    while int(n) > x:
        x = int(n)
print(x)
