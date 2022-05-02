# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

import re


def int_func(word):
    for i in word:
        if not re.match(r'[a-z]', i):
            return 'Это не латиница'
    return word.title()


imp = input('Введите латинское слово\n')
print(int_func(imp))
