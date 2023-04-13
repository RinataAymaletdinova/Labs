def p1():
    pas = input("Введите пароль")
    if len(pas) > 6:
        pas2 = input("Введите пароль повторно")
        if pas == pas2:
            print("Пароль принят")
        else:
            print("Пароль не принят")
    else:
        print("Ненадежный пароль")

def p2():

    ticket = input("Введите номер места")
    if int(ticket) < 37:
        if int(ticket) % 2 == 0:
            print("Купе, верхнее место")
        else:
            print("Купе, нижнее место")
    else:
        if int(ticket) % 2 == 0:
            print("Боковое, верхнее место")
        else:
            print("Боковое, нижнее место")

def p3():
    N = input("Введите количество слов")
    s = ''
    for i in range(1, int(N) + 1):
        word = input("Введите слово")
        s = s + word + ' '
    print(s)

def p4():
    year = input("Введите год")
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        print("Год", year, "- високосный")
    else:
        print("Этот год не високосный")

def p5():
    c1 = input("Введите первый цвет")
    c2 = input("Введите второй цвет")
    if c1 == "красный" or c2 == "красный":
        if c1 == "синий" or c2 == "синий":
            print("фиолетовый")
        elif c1 == "желтый" or c2 == "желтый":
            print("оранжевый")

    elif c1 == "синий" or c2 == "синий":
        if c1 == "красный" or c2 == "красный":
            print("фиолетовый")
        elif c1 == "желтый" or c2 == "желтый":
            print("зеленый")

    elif c1 == "желтый" or c2 == "желтый":
        if c1 == "красный" or c2 == "красный":
            print("оранжевый")
        elif c1 == "синий" or c2 == "синий":
            print("зеленый")
    else:
        print("Требуется ввести основные цвет")

p1()
p2()
p3()
p4()
p5()
