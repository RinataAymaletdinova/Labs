from PIL import Image, ImageFilter

def p1():
    #Напишите программу, которая открывает и выводит этот файл на экран. Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.
    name = "papug.jpg"
    with Image.open(name) as img:
        img.load()
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode

    print("Ширина:", width, "\nВысота", height, "\nФормат:", format, "\nМод:", mode,)

def p2():
#Напишите программу, которая создаёт уменьшенную в три раза копию изображения. Получите горизонтальный и вертикальный зеркальный образ изображения. Сохраните изображения в текущую папку под новым именем.
    name = "papug.jpg"
    with Image.open(name) as img:
        img.load()

    new_papug = img.resize((img.width // 3, img.height // 3))
    new_papug.save("newpapug.jpg")

    new_papug = img.rotate(180)
    new_papug.save("newpapug_rotate.jpg")


def p3():
#Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg. Напишите программу, которая применит ко всем этим файлам сразу любой фильтр (кроме размытия, т.к. он рассматривался на лекции). Сохраните изображения в новую папку под новыми именами.

   for i in range(1, 6):
        with Image.open(str(i)+'.jpg') as img:
            img.load()
        edge_photo = img.filter(ImageFilter.EDGE_ENHANCE)
        edge_photo.save("C:/Users/Lab_7/" + str(i) + '.jpg')

def p4():
#Напишите программу, которая добавляет на изображение водяной знак.
    ph = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    with Image.open('nlogo.png') as img:
        img.load()

    for i in ph:
        with Image.open(i) as f:
            f.paste(img, (40,40), img)
            f.save("C:/Users/Lab_7/" + "new/" + i)

