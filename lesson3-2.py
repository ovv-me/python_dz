# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(name, lastname, year_of_birth, city, email, phone):
    return f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}' \
           f' Город проживания: {city} Email: {email} Телефон: {phone}'


my_func(name='Olga',
        lastname='Voron',
        year_of_birth=1990,
        city='Spb',
        email='email',
        phone='0232')
