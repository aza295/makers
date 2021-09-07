#  """
# 1) Создайте класс Class1 с 2 любыми методами. 
# Создайте второй класс Class2, который наследуется от Class1, 
# и  vопределите в новом классе ещё 2 метода. 
# Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

class  class1:
    



# 2) Создайте класс A и определите в нём метод method1, 
# который будет печатать строку "Основной функционал". 
# Затем создайте второй класс B, который наследуется от класса 
# A, и дополните method1 таким образом, чтобы он печатал также строку
#  "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

# class A:
#       def method1(self):
#             print('Основной функционал')
# class B(A):
#       def method1(self):
#             print('Дополнительный функционал')

# b1=B()
# b2=A()
# b2.method1()
# b1.method1()





# 3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# # example = MyString('String')
# # example.append('hello')
# # print(example) -> 'Stringhello'
# # print(example.pop()) -> 'o'
# # print(example) -> 'Stringhell'


# class MyString(str):

#       def x():
#             print ('les paul')
#       def append

# def perfect(number):
#     lst = []
#     sum = 0
#     for i in range(1,number):
#         if number % i == 0:
#             lst.append(i)
#             sum += i
#     return (sum == number, lst, number)




# 4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. 
# Переопределите метод .get() 
# таким образом, чтобы при попытке получении несуществующего 
# ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.



# class MyDict(dict):
#       def get(self,key,default='Are you kidding?'):
#             return super().get(key,default)
# a = MyDict({'a':15,'b':20})
# print(a.get('c'))


 
#5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст.
#Создайте метод display(), который будет выводит данные об этом человеке.
#Создайте второй класс Student, который будет наследоваться от класса Person,
#он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут,
#  который будет описывать направление студента. Создайте метод display_student(), который будет выводить
#  данные об этом студенте.
# Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

# class Person:
#       name = 'Dave Mustaine'
#       age = '24 года'
#       def display(self):
#             print(self.name)
#             print(self.age)
# class Student(Person):
#       job = 'Студент'

#       def display_student(self):
#             print(self.job)
#             print('4 курс Политех направление IT')

# b1 = Student()
# print(b1.display())
# print(b1.display_student())

# 6) Создайте класс ContactList, который должен наследоваться 
# от встроенного класса list. В нем должен быть реализован метод 
# search_by_name, который должен принимать имя и возвращать список всех совпадений. 
# Создайте экземпляр класса all_contacts и передайте список ваших контактов.

class List(list):

    def __init__(self):
        self.all_contacts = []

    def search_by_name(self, *name):
        for i in name:
            self.all_contacts.append(i.title())
        ss = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
        sss = set(ss)
        print("Список совпадений: ")
        for a in sss:
            print("\t",a)
class ContactList(List):

    def __init__(self):
        super().__init__()
my_contacts = ContactList()
my_contacts.search_by_name("monkey","flowers","donkey","smile","donkey","monkey","books")