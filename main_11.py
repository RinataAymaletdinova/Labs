def p1():
#Задача «Ресторан»: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name (название ресторана) и cuisine_type (тип кухни). Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт. Создайте на основе своего класса экземпляр с именем newRestaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(self.restaurant_name, self.cuisine_type)

        def open_restaurant(self):
            print(self.restaurant_name, 'открыт!')


    newRestaurant = Restaurant('Рататуй', 'французская')
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def p2():
#На основе ранее созданного класса Restaurant из задания 11.1 создайте три разных экземпляра (три ресторана), вызовите для каждого экземпляра метод describe_restaurant().
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(self.restaurant_name, "-", self.cuisine_type)

        def open_restaurant(self):
            print(self.restaurant_name, 'открыт!')

    rest1 = Restaurant(input("Введите название ресторана 1"), input("Введите кухню ресторана 1"))
    rest1.describe_restaurant()

    rest2 = Restaurant(input("Введите название ресторана 2"), input("Введите кухню ресторана 2"))
    rest2.describe_restaurant()

    rest3 = Restaurant(input("Введите название ресторана 3"), input("Введите кухню ресторана 3"))
    rest3.describe_restaurant()


def p3():
#Добавьте в созданный класс Restaurant атрибут, задающий начальный рейтинг ресторана и метод, который получает на вход новое значение рейтинга и обновляет его.
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.stars = 1

        def describe_restaurant(self):
            print(self.restaurant_name, "-", self.cuisine_type, "\nЗвезд Мишлен:", self.stars)

        def open_restaurant(self):
            print(self.restaurant_name, 'открыт!')

        def set_stars(self, stars):
            self.stars = stars
            print(self.describe_restaurant())

    rest1 = Restaurant(input("Введите название ресторана 1"), input("Введите кухню ресторана 1"))
    rest1.describe_restaurant()
    rest1.set_stars(input('Введите новое количество звезд'))

p1()
p2()
p3()
