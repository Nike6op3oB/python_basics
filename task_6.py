"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def int_func(word):
    return word.title()


word = input('Введите слово: ')
print(int_func(word))

sentence = input('Введите несколько слов через пробел: ').split()
for i in range(0, len(sentence) - 1):
    sentence[i] = int_func(sentence[i])
print(*sentence)