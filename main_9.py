from PIL import Image, ImageFilter
import os, csv

def p1_2():
#Модифицируйте программу из практики 7.3 (7 лабораторная работа ) или создайте заново: обработать любой операцией все картинки в заданной папке, используя для обхода файлов в папке модуль os (или Pathlib). При этом каталог для итоговых (обработанных) изображений должен тоже создаваться с помощью модуля os или Pathlib.
    Files = []
    if not os.path.isdir("parror"):
        os.mkdir("parrot")
    for file in os.listdir():
        if file.endswith(".jpg") or file.endswith(".png"):
            Files.append(file)

    for i in Files:
        with Image.open(i) as img:
            img.load()
        edge_photo = img.filter(ImageFilter.EDGE_ENHANCE)
        edge_photo.save("C:/Users/Lab_9/parrot/" + i)

def p3():
 #Имеется файл с данными в формате csv. Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит данные в виде.
    with open("data.csv", newline='') as i:
        reader = csv.reader(i)
        count = 0
        print('Нужно купить:')
        for row in reader:
            count += int(row[1]) * int(row[2])
            print(row[0], "-", row[1], "шт. за", row[2], 'руб.')
        print('Итоговая сумма:', count, 'руб.')


p1_2()
p3()

