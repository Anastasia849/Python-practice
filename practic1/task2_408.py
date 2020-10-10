"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя метод format
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  и не делить слова.
"""


def wiki_function():
    f = open("wiki.txt", 'r')
    lines = []
    for line in f:
        if not line.isspace():
            lines.append(line)
    for i in range(len(lines)):
        for j in lines[i]:
            if not (j.isalpha() or j == ' '):
                lines[i] = lines[i].replace(j, '')
    str1 = ' '.join(lines)
    f.close()

    dict1 = {}
    allwords = str1.split()
    for i in allwords:
        dict1[i] = dict1.get(i, 0) + 1
    k = 0
    words = []
    words1 = []
    for i, x in sorted(sorted(dict1.items()), key=lambda y: y[1], reverse=True):
        k += 1
        words.append(i)
        print('{} place --- {} --- {} times \n'.format(k, i, x))
        if k == 10:
            break
    for i, x in sorted(sorted(dict1.items()), key=lambda y: y[1]):
        if x == 1:
            words1.append(i)
        if x > 1:
            break

    for i in allwords:
        for m in words1:
            if i == m:
                allwords.remove(i)

    for i in range(len(allwords)):
        for j in words:
            if allwords[i] == j:
                allwords[i] = 'PYTHON'

    f2 = open('file.txt', 'w')

    str2 = ''
    maxlen = 100
    c = 0
    for i in allwords:
        c += len(i)
        if c > maxlen:
            str2 += '\n'
            c = len(i)
        elif str2 != '':
            str2 += ' '
            c += 1
        str2 += i
    f2.write(str2)


# Вызов функции
wiki_function()
