# ## Задача 6. Совместное проживание 2
# Артём увлёкся предыдущим экспериментом и решил расширить его, создав целую семью из Мужа, Жены и Кота.
# Условия эксперимента следующие:
# Каждый день участники жизни могут делать только одно действие. Все вместе они должны прожить год и не умереть.
#
# Муж может:
# - есть,
# - играть,
# - ходить на работу,
#
# Жена может:
# - есть,
# - покупать продукты,
# - покупать шубу,
# - убираться в доме,
#
# Кот может:
# - есть,
# - спать,
# - драть обои
#
# Все они живут в одном доме, дом характеризуется:
# - кол-во денег в тумбочке (в начале - 100)
# - кол-во еды в холодильнике (в начале - 50)
# - еда для кота (в начале 30)
# - кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
# Все люди могут гладить кота (+5 к счастью)
#
# У кота есть имя и степень сытости (в начале - 30)
#
# Любое действие (в том числе и кота), кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Кот кушает максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе человек или кот умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
# Еда для кота тоже покупается: за 10 денег 10 еды.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если кот дерет обои, то грязи тоже становится больше на 5 пунктов
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в компьютер (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.
#
# Реализуйте такую программу.
# Подведите итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.
#
# Дополнительно: добавьте ещё ребёнка и несколько котов

from random import randint


def act(person, num):
    if person.satiety < 20:
        person.eat()
    else:
        if isinstance(person, Wife):
            if person.home.food < 30:
                person.buy_groceries()
            elif person.home.dirt > 90:
                person.clean_up()
            elif person.home.money >= 350:
                person.buy_fur_coat()
            elif num == 1:
                person.clean_up()
            elif num == 2:
                person.eat()
            elif num == 3:
                person.petting_cat()
        if isinstance(person, Husband):
            if person.home.money < 100:
                person.go_to_work()
            elif person.happiness < 250:
                person.play()
            elif num == 1:
                person.go_to_work()
            elif num == 2:
                person.eat()
            elif num == 3:
                person.petting_cat()
        if isinstance(person, Cat):
            if num == 1:
                person.tear_up_the_wallpaper()
            else:
                person.sleep()


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.food_for_cat = 30
        self.dirt = 0
        self.fur_coat = 0
        self.buy_food = 0
        self.buy_food_for_cat = 0
        self.profit = 0

    def __str__(self):
        return f'Съедено еды: {self.buy_food - 50}\n' \
               f'Съедено кошаком еды: {self.buy_food_for_cat - 30}\n' \
               f'Куплено шуб: {self.fur_coat}\n' \
               f'Заработано денег: {self.profit}\n'

    def print_info(self):
        print(f'\tMoney: {self.money}\n'
              f'\tFood: {self.food}\n'
              f'\tFood for cat: {self.food_for_cat}\n'
              f'\tDirt: {self.dirt}\n'
              f'\tFur coat: {self.fur_coat}')


class Person:
    def __init__(self, name, age, home):
        self.set_name(name)
        self.set_age(age)
        self.satiety = 30
        self.happiness = 100
        self.home = home

    def set_name(self, name):
        while not name.isalpha():
            name = input('Некорректное имя. Повторите ввод: ')
        self.__name = name

    def set_age(self, age):
        while age < 0 or age > 99:
            age = int(input('Некорректный возраст. Повторите ввод: '))
        self.__age = age

    def print_info(self):
        print(f'\tИмя: {self.__name}\n'
              f'\tВозраст: {self.__age}\n'
              f'\tСытость: {self.satiety}\n'
              f'\tСчастье: {self.happiness}\n')

    def die(self):
        if self.satiety < 0:
            print(f'{self.__name} - смерть от голода.')
            return True
        if self.happiness < 10:
            print(f'{self.__name} - смерть от депрессии.')
            return True

    def eat(self):
        if self.home.food >= 10:
            self.satiety += 10
            self.home.food -= 10
        elif self.home.food > 0:
            self.satiety += self.home.food
            self.home.food = 0

    def petting_cat(self):
        self.happiness += 5
        self.hungry()

    def hungry(self):
        self.satiety -= 10


class Husband(Person):
    def __init__(self, name, age, home):
        super().__init__(name, age, home)

    def play(self):
        self.happiness += 20
        self.hungry()

    def go_to_work(self):
        self.home.money += 150
        self.home.profit += 150
        self.hungry()


class Wife(Person):
    def __init__(self, name, age, home):
        super().__init__(name, age, home)

    def buy_groceries(self):
        if self.home.money >= 45:
            self.home.food += 35
            self.home.food_for_cat += 10
            self.home.buy_food += 35
            self.home.buy_food_for_cat += 10
            self.home.money -= 45
        elif self.home.money > 0:
            part = round(self.home.money / 3)
            self.home.food += 2 * part
            self.home.food_for_cat += part
            self.home.buy_food += 2 * part
            self.home.buy_food_for_cat += part
            self.home.money = 0
        self.hungry()

    def buy_fur_coat(self):
        if self.home.money >= 350:
            self.home.money -= 350
            self.happiness += 60
            self.home.fur_coat += 1
            self.hungry()

    def clean_up(self):
        self.home.dirt -= 50
        if self.home.dirt < 0:
            self.home.dirt = 0
        self.hungry()


class Cat:
    def __init__(self, name, age, home):
        self.set_name(name)
        self.set_age(age)
        self.satiety = 30
        self.home = home

    def set_name(self, name):
        while not name.isalpha():
            name = input('Некорректное имя. Повторите ввод: ')
        self.__name = name

    def set_age(self, age):
        while age < 0 or age > 20:
            age = int(input('Некорректный возраст. Повторите ввод: '))
        self.__age = age

    def eat(self):
        if self.home.food_for_cat >= 5:
            self.satiety += 10
            self.home.food_for_cat -= 6
        elif self.home.food_for_cat > 0:
            self.satiety += self.home.food_for_cat * 2
            self.home.food_for_cat = 0

    def sleep(self):
        self.satiety -= 10

    def tear_up_the_wallpaper(self):
        self.home.dirt += 5
        self.satiety -= 10

    def die(self):
        if self.satiety < 0:
            print(f'{self.__name} - смерть от голода.')
            return True

    def print_info(self):
        print(f'\tИмя: {self.__name}\n'
              f'\tВозраст: {self.__age}\n'
              f'\tСытость: {self.satiety}\n')


house = House()
husband = Husband('Mike', 30, house)
wife = Wife('Kate', 27, house)
cat = Cat('Tom', 5, house)
day = 0

while not husband.die() and not wife.die() and not cat.die():
    if day == 365:
        print('\nЖильцы прожили вместе целый год!\n')
        break
    cube = randint(1, 10)
    act(husband, cube)
    act(wife, cube)
    act(cat, cube)
    if house.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
    house.dirt += 5
    day += 1

print('Муж:')
husband.print_info()
print('Жена:')
wife.print_info()
print('Кот:')
cat.print_info()
print(house)
print('Home:')
house.print_info()
