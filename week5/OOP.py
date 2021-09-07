# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, 
# и число Пи(3.14). 
# Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. 
# Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.



# class Circle:
#     color = 'red'
#     pi = 3.14
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return f"Площадь круга: {self.pi * self.radius ** 2}"

# circle1 = Circle(5)
# circle1.color = 'green'
# print (circle1.area()






# 2) Создайте класс для песен Song. 
# Каждая песня имеет название, автора и год выпуска. 
# Добавьте три метода show_author, show_title, show_year, 
# выводящие утверждения о каждом атрибуте экземпляра класса Song, например:
#  "Эта песня вышла в 2010 году". Создайте экземпляр класса с 
#  вашей любимой песней и примените все методы.



# class Song: 
      

#       def __init__(self,show_author,show_title, show_year):
#             self.n = show_author 
#             self.l = show_title
#             self.a = show_year
#       def get_profile(self):
#             return f'{self.n},{self.l}, Эта песня вышла в {self.a} году '
      



# song1 = Song('Pantera','cowboys from hell',1990)
# song2 = Song('Duran duran','come undeone',1993)

# print(song2.get_profile())







# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         return f'Author is {self.author}'

#     def show_title(self):
#         return f'Name of song {self.title}'

#     def show_year(self):
#         return f'This song was relised in {self.year} year'

#     def show_info(self):
#         return f'Author is  {self.author}\nName of song {self.title}\nThis song was relised in {self.year} year'

# my_song = Song('Pantera','cowboys from hell',1990)
# print (my_song.show_info())



# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании,
#  стоимость посадки, стоимость за каждый пройденный километр. 
#  Также добавьте к классу метод расчитывающий стоимость поездки.
#   Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.



# class Taxi:
#     def init(self, name, landing, km):
#         self.name = name
#         self.landing = landing
#         self.km = km

#     def cost(self, km_count):
#         full_cost = self.landing + km_count * self.km
#         return f'Стоимость поездки на такси {self.name}: {full_cost} сом'

# taxi1 = Taxi('Namba', 30, 25)
# taxi2 = Taxi('Yandex', 25, 30)
# taxi3 = Taxi('Jorgo', 40, 20)

# print (taxi1.cost(2))
# print (taxi2.cost(8))
# print (taxi3.cost(0.2))





# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. 
# Также создайте метод get_info, который выводит информацию о контакте в следующем виде:
#  "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.

# class PhoneBook:
#     def init(self, name, last_name, phone_number):
#         self.name = name
#         self.last_name = last_name
#         self.phone_number = phone_number

#     def get_info(self):
#         return f"Контакт: {self.name} {self.last_name}, телефон: {self.phone_number}"

# contact1 = PhoneBook("Олег", "Петрович", "+996555555555")
# print(contact1.get_info()


# 5) Напишите класс Salary для расчета налогов на заработную плату. 
# У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. 
# Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. 
# Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. 
# Создайте экземпляр класса и посчитайте сумму вашего налога.


# class Salary:
#       percent = 0.08
      
#       def __init__(self,salary,years):
#             self.salary = salary
#             self.years = years

#       def tax(self):
            

      


class Dog:
      def __init__(self,name):
            self.name = name 
      def voice(self):
            print('Гав')

class Cat:
      def __init__(self,name):
            self.name = name 
      def voice(self):
            print('Мяу')   

c = Cat('wgre')
c.voice()
d = Dog('dfget')
d.voice()

def to_pet(animal):
      animal.voice()

for animal in (c,d):
      to_pet(animal)