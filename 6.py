# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def str_a(x):
    a = str(x)
    b = ''
    c = 0  # сумма чисел в строке
    d = ''  # пустая строка для предмета
    e = []
    for el in a:
        if el.isdigit():
            b = b + el
        elif el == ' ':
            b = b + ' '
    d = a[0:a.find(':')]
    for el in b.split():
        c = c + int(el)
    e.append(d)
    e.append(int(c))
    return e


with open('my_f_6.txt', 'r', encoding='utf-8') as f:
    a = []
    for line in f:
        a.append(str_a(line))
c = dict(a)
print(c)




