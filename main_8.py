from PIL import Image, ImageDraw, ImageFont

def p1():
#Скачайте любую открытку из интернета, определите область, которую Вам нужно вырезать из данного изображения (обрезать текст, часть фото и т.д.). Напишите программу, которая выполнит эту операцию. Сохраните изображения в текущую папку под новым именем.


    with Image.open('good_day.jpg') as img:
        img.load()
    cropped = img.crop((240,0,550,430))
    cropped.save('cropped_cup.jpg')

def p2():

#Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему». Спросите у пользователя, к какому празднику ему нужна открытка и выведите нужную открытку на экран.
    celebrations = {"1":"NY.jpg", "2":"apple_spas.jpg", "3":"HB.jpg"}
    ask = input("Новый год - 1, Яблочный спас - 2, День рождения - 3\nВведите цифру нужного праздника")
    img = Image.open(celebrations[ask])
    img.show()


def p3():

#Модифицируйте задачу 8.1 так: спросите еще у пользователя, имя того, кого он хочет поздравить, добавьте на заданную открытку текст «…., поздравляю!», где вместо …. вставьте полученное имя  (выведите его разным цветом и шрифтами, посередине вверху или внизу фото). Найдите в сети интернет решение, как сделать надпись жирным текстом (по умолчанию, такого параметра нет). Сохраните новую открытку в файл с расширением png.

    celebrations = {"1":"NY.jpg", "2":"apple_spas.jpg", "3":"HB.jpg"}
    ask = input("Новый год - 1, Яблочный спас - 2, День рождения - 3\nВведите цифру нужного праздника")
    name = input("Кого поздравляем?")

    img = Image.open(celebrations[ask])
    width, height = img.size
    font1 = ImageFont.truetype('Pixeloid Sans.ttf', size=60)
    font2 = ImageFont.truetype('Montserrat.ttf', size=60)
    draw_name = ImageDraw.Draw(img)
    draw_name.text(
        ((width / 2) - 300 , 60),
        name + ', поздравляю!',
        font = font1,
        fill = ('#00FF7F'))
    draw_name.text(
        ((width / 2) - 300 , (height - 150)),
        name + ', поздравляю!',
        font = font2,
        stroke_width=2,
        stroke_fill="#2F4F4F",
        fill = ('#2F4F4F'))

    img.save("named_card.png")



p3()
