import json
import re


def p1():
    # Имеется файл JSON с информацией о продуктах. Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде.
    with open("Products.json", "r", encoding='utf-8') as file:
        data = json.load(file)

        for prod in data["products"]:
            if prod['available']:
                available = 'В наличии'
            else:
                available = 'Нет в наличии'
            print('\nНазвание: ', prod['name'], '\nЦена: ', prod['price'], '\nВес: ', prod['weight'], '\n' + available)


def p2():
    # Модифицируйте программу 10.1 – добавьте в нее код, который добавляет данные в файл JSON (спрашивает их у пользователя) и потом также выводить содержимое итогового файла на экран.
    i = input("Введите товар")
    p = input("Введите его цену")
    w = input("Введите его вес")
    a = input("Наличие: True или False")
    new = {"name": i, "price": p, "available": a, "weight": w}

    with open("Products.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        data['products'].append(new)

        for prod in data["products"]:
            if prod['available'] == "True":
                available = 'В наличии'
            else:
                available = 'Нет в наличии'
            print('\nНазвание: ', prod['name'], '\nЦена: ', prod['price'], '\nВес: ', prod['weight'], '\n' + available)

    with open("Products.json", "w", encoding='utf-8') as newf:
        json.dump(data, newf, ensure_ascii=False, indent=4)


def p3():
    # Создание русско-английского словаря.
    dict = []
    rusdict = []
    rusdict = {}
    with open("en-ru.txt", "r", encoding='utf-8') as file:
        for lines in file:
            dict = lines.replace('\n', '')
            dict = re.split(' – |, ', dict)
            for rus in dict[1:]:
                if rus in rusdict:
                    rusdict[rus] = rusdict[rus] + ', ' + dict[0]
                else:
                    rusdict[rus] = dict[0]
    with open("ru-en.txt", "a", encoding='utf-8') as newfile:
        for key in sorted(rusdict):
            newfile.write(key + ' - ' + rusdict[key] + "\n")


p1()
p2()
p3()