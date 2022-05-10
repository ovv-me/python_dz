# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('less5_test_2.data', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f"Всего строк: {len(lines)}")
    for key, st in enumerate(lines):
        words = st.split(' ')
        print(f"Слов в строке {key + 1}: {len(words)}")
