#string1 = "Makers"
#string2 = 'bootcamp'
#print (string1, string2)
#print (type(string1))


#string3 = "Maker's Bootcamp"
#print (string3)


#sentence = "you said: 'i'm crazy'"
#print (sentence)



# sentence = "i love maker\"s bootcamp"
# print (sentence)

#Экранирование

# string = "Dear friend, \n\nwelcome to makers bootcamp ! \nenjoy your time here with us!"
# print (string)



# string = """Dear friend, 
# welcome to makers bootcamp ! 
# enjoy your time here with us!"""
# print (string)



# string = 'this is a very long string.\
# The lenght of string in python should not be more than 79 symbols.\
# Remember this.'
# print (string)



# languages = 'languages:\n\t'
# description = 'Python: backend language \n\t JavaScript: frontend language'
# print (languages,description)

# вертикальное экранирование

# sentence = "there's \vno\vone \vlike \vyou \vi \vcan't \vwait \vfor \vthe \vnight \vwith \vyou"
# print (sentence)


# Сырая строка
# url =  r'hhtps://kaktus/\news\topic/\read'
# print(url)


# string1 = 'makers'
# string2 = 'bootcamp'
# # print (string1 + string2)
# print ('i study at ' + string1 +  string2 )

# num1 =  '6'
# num2 =  '7'
# result = num1 +num2 
# print (result)

# Дублирование строки
# string = "01010"
# print (string*8)
# найти длину строки 
# string = 'Makers bootcamp'
# print(len(string))

# lenght = len ('john')
# print (lenght)

# Доступ по индексу

# sentence = 'strings are ordered'
# print (sentence[18])
# print (sentence[13])
# print (sentence[9])

# Срез

# string = 'fed exppress'
# print (string[:6])
# print (string[2:-2])
# print (string[:6])
# print (string[:6])

# part_string = (string[:2])
# print (part_string)


# string ="system of a down"
# print(string[2:-2])
# print (string[6:-3])


# вывести строку наоборот 
# string ="ac'dc"
# print(string[:: -1])


# строки это упорядоченная неизменяеммая последовательнсоть символов.

# a = 'string'
# b = ' 295'
# c = ''
# d = '!@#$%'

# string = "here's aziz's laptop"
# string = "here's\ aziz's\ laptop"


#  строки завиясят от регистра. это значит что  string = 'string'
                                              # string2 = 'string'
# string != string2 #true


#  Пробелы и пробельные символы тоже являются элементами строки
# str = 'my string'
#        0123456789
#        -9-8-7-6-5-4-3-2-1
# string = 'sting'
# print (string[4])

#Проверочные методы
# is_...() -. True
# a = this is a text 
# a = 'this is a text'
# b ='alamedin - 1'
# c = 'hello'


# # isalpha() Проверяет что строка состоит из букв
# print(a.isalpha()) false 
# print(b.isalpha()) false
# print(c.isalpha()) true

# isdigit check that all symbols are digits

# a = 'Hi123' true
# b = '1234 5678' True
# c = '123456' True
 


# islower(), isupper()
# check that all symbols are in lower register/ upper register

# a = 'Hello wolrld' flase
# b = 'hello wolrd' true 
# c = 'HELLO WORLD'false 

# a. islower () False
# b. islower () True
# c. islower () False

# isupper

# a = 'Hello wolrld' True
# b = 'hello wolrd' False
# c = 'HELLO WORLD'True

# a = isupper ()True
# b = isupper () false
# c = isupper () True



# #  Преобразование строк (создается копия строки) текущяя строка остается неизменной 
# # methods 
# #  lower () chnage all symbols to lower register 
# a = 'Hello wolrd'
# b = 'HELLO WORLD'
# D = a.lower () #hello world 
# #  upper() chnage all symbols to upper register 
# a = 'Hello wolrd'
# b = 'hello wolrd'
# b.upper () #HELLO WOLRD 
# print (a)
# # swapcase ()   меняет все буквы в противоположный регистр
# a = 'Hello wolrd'
# b = 'hello wolrd'
# a.swapcase ()# hello world
# b.swapcase ()# HELLO WOLRD

# Capitalize() change only first letter to capital, 

# a = 'string'
# a.capitalize( )# 'string'

# b = JOHN
# B.capitalize () #'John'

# c = '2Pac'
# c.capitalize #'2pac'



# casefold() change all symbols to lower register 



# title () change all first letters of words to upper register

# a = 'it was good day'
# a.title ()# 'It Was Good Day'


# replace(pattern, new_value )
# a = It Was Good Day
# a.repalace ('a','*')
# it w*s good d*y

# it w*s good d*y
# a.lower (). replace ('a')
# a.repalce ('day'.night)

# count 

# a = today is a good day
# a.replace ('a','*'2)
# tod*y is good * good day


# strip убирает символы с обеих сторон.
# (по умолчанию пробел)

# s = '  string '
# a.strip()
# #'string' 
# b = '--- string-----'
# b.strip ('-') # 'string
# b.lstrip ('-') #'string----'
# b.rstrip ('-')# '---string'
# #'string'


# b = '----string++++'
# b.strip ('-+') #'string'

# Split - разбивает строку по разделителю
# a = Alan Claus Brian Bruce
# a.split ()
#['Alan', 'Claus', 'Brian' , 'Bruce' ]


#  Поиск в строке 

#  Find (str)
# ищет первое вхождение указанной подстроки если подстроки нет в строке выдает -1

# a = 'today is a good day'
# a.find ('a')#3 
# a.find ('e')# -1
# a.rfind('a')
#  index(str) ищет первое вхождение указанной подстроки если подстроки нет в строке выдает ошибку 

# a = 'today is a good day'
# a.index("a")#3
# a.index('e') #error
# a.index ('day')#2

#  count(str) считает скколько раз подстрока встречается в строке 

# a = 'today is a good day'
# a.count ('d')#3
# a.count ('e')#0
# a.count ('is')#1
# a.count ('day')#2

# конкатенация 

# a = 'hello'
# b = 'world'
# print (a+b) 


#Размножение строки 
 
# a = 'S'
# a * 5 #sssss

# b = 'string'
# b * 3 #stringstringstring

# In  проверка на вхождение подстроки  в строку 

# a = 'my brand new test string'
# 'e' in a #true 
# 'new' in a #true 
# 'o' in a #true
# 'old' in a #false




# Форматирование строк 
# total = 3500 

# name = "руслан"
# date = '15.07.2002'
# ''' здравствуйте руслан! спасибо за покупку. счет: 2000 сом дата: 15.06.2021'''
# res = f' здравствуйте {name} ! спасибо за покупку. счет: 2000 сом дата: {date}'
# print (res)


# квадрат числа 10 равен 100
# res = f ' квадрат числа {num} равен  {num ** 2}'

# print (res )

# a = 10 
# b = 15

# '10  меньше 15 ? True'

# res = f'{a} меньше {b} ? {a < b}'
# print (res)


# разделение строки с хэштэгом
# str = "#makers#bootcamp#программирование#it#курсы"
# print (str.split('#'))

# команда f"  

# name = "Till"
# surname = "lindeman"
# age = '58'
# job = 'vocalist and songwriter'

# res = f" Hello! {name} {surname}. You are {job} of Rammstein band. Your age is: {age} year old"
# print (res)


# name = 'Elon'
# surname = 'Musk'
# age = '47'

# res = f' Hello! Your name  {name} {surname} You are: {age} year old. You live in LA California '
# print (res)

# name = input ("enter your name")
# surname = input ("Enter your surname ")
# print (name, surname) 

# ИНДЕКСАЦИЯ  ИНДЕКСАЦИЯ   ИНДЕКСАЦИЯ  ИНДЕКСАЦИЯ  ИНДЕКСАЦИЯ
# fds = 'rolling stones'
# print (fds[5])

# Срез  Срез  Срез Срез  Срез  Срез  Срез  Срез  Срез
# fds = 'rolling stones'
# print (fds[:9])

# ШАГ - НУЖЕН ДЛЯ ТОГО ЧТОБЫ ИЗВЛЕКАТЬ СИМВОЛЫ ЧЕРЕЗ ОПРЕДЕЛЕННОЕ ЗНАЧЕНИЕ 


# ШАГ  ШАГ ШАГ ШАГ ШАГ ШАГ ШАГ   ШАГ  ШАГ  ШАГ  ШАГ  ШАГ
# fds = 'rolling stones'
# print (fds[: :2])

# МЕТОДЫ СТРОК 

# SPLIT ОТВЕЧАЕТ ЗА РАЗБИЕНИЕ СТРОКИ ПО РАЗДЕЛИТЕЛЮ РАЗДЕЛИТЕЛЬ УКАЗЫВАЕТСЯ 
# В СКОБКАХ НО ЕСЛИ ЕГО НЕТУ ТО ПО УМОЛЧАНИЮ МЕТОД SPLIT РАЗБИВАЕТ CТРОКУ ЧЕРЕЗ ПРОБЕЛ

# SPLIT  SPLIT   SPLIT  SPLIT  SPLIT  SPLIT  SPLIT  SPLIT  SPLIT  SPLIT  SPLIT

# motto = 'reliable*with*us'
# print (motto.split ('*'))


# motto = 'reliable with us'
# print (motto.split ())

# МЕТОД JOIN ОТВЕЧАЕТ ЗА СБОРКУ СТРОКИ ИЗ СПИСКА С ОПРЕДЕЛЕНННЫМ РАЗЕДЕЛИТЕЛЕМ
# В ДАННОМ МЕТОДЕ РАЗДЕЛИТЕЛЬ УКАЗЫВАЕТСЯ НЕ В СКОБКАХ А В КОВЫЧКАХ 
# ДО ПРОПИСЫВАНИЯ МЕТОДА JOIN

# JOIN   JOIN   JOIN  JOIN  JOIN  JOIN  JOIN  JOIN  JOIN JOIN  JOIN

# string = ['s','t','i','n','g']
# print ('*'.join(string))
# output
# s*t*i*n*g

# string = ['s','t','i','n','g']
# print (''.join(string))
# output 
# sting

# МЕТОД FIND ИЩЕТ ПОДСТРОКУ В СТРОКЕ И ВОЗВРАЩАЕТ INDEX ПЕРВОГО ЭЛЕМЕНТА
# НАЙДЕННОЙ ПОДСТРОКИ ЕСЛИ ЖЕ ПОДСТРОКА НЕ НАЙДЕНА ВОЗВРАЩАЕТ -1
# FIND  FIND  FIND  FIND  FIND FIND FIND  FIND FIND FIND  FIND  FIND  FIND FIND

# crt = 'south park is fucking good'
# print (crt.find( 'good'))
# output
# 22


# crt = 'south park is fucking good'
# print (crt.find( 'awesome'))
# output
-1

# МЕТОД replalce - ЗАМЕНЯЕТ ОДНУ ПОДСТРОКУ НА ДРУГУЮ НО ИСХОДНАЯ СТРОКА 
# НЕ ИЗМЕНЯЕТСЯ 

# replalce  replalce  replalce  replalce  replalce  replalce  replalce 

# string = 'makers bootcamp '
# print (string.replace('b','B'))
# output:
# makers Bootcamp

# Конкатенация (сложение)

# S1 = 'spam'
# S2 = 'eggs'
# print(S1 + S2) #'spameggs'


# ДУБЛИРОВАНИЕ СТРОКИ
# * * * * * * * * * * * *
# print('spam' * 3) #spamspamspam

# ДЛИНА СТРОКИ 
 
# LEN   LEN  LEN  LEN  LEN  LEN  LEN  LEN  LEN  LEN

# print (len('foo fighters')) #4


# ДОСТУП ПО ИНДЕКСУ

# S = 'toxic city'
# print(S[3]) #'i'


# Извлечение среза

# Оператор извлечения среза: [X:Y]. X – начало среза, а Y – окончание. 
# Символ с номером Y в срез не входит. По умолчанию первый индекс равен 0,
#  а второй - длине строки.

# #  ИЗВЛЕЧЕНИЕ СРЕЗА
# lrc = 'spameggs'
# print(lrc[3:6]) #'me'
# print(lrc[2:-2]) #'ameg'


# Кроме того, можно задать шаг, с которым нужно извлекать срез.
# print(lrc[::-1]) #'sggemaps'
# print(lrc[3:5:-1]) #''
# print(lrc[1::1]) #'aeg'






# ************* Функции и методы строк *****************

 

# S.find(str, [start],[end]) Поиск подстроки в строке. 
# Возвращает номер первого вхождения или -1


# S.rfind(str, [start],[end]) Поиск подстроки в строке.
#  Возвращает номер последнего вхождения или -1

# S.index(str, [start],[end]) Поиск подстроки в строке.
#  Возвращает номер первого вхождения или вызывает ValueError

# S.rindex(str, [start],[end]) Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
# S.replace(шаблон, замена) Замена шаблона
# S.split(символ) Разбиение строки по разделителю

# S.upper() Преобразование строки к верхнему регистру

# S.lower() Преобразование строки к нижнему регистру

# S.swapcase() Переводит символы нижнего регистра в верхний, а верхнего – в нижний

# S.startswith(str) Начинается ли строка S с шаблона str

# S.title() Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
# S.capitalize() Переводит первый символ строки в верхний регистр, а все остальные в нижний
# S.endswith(str) Заканчивается ли строка S шаблоном str
# S.join(список) Сборка строки из списка с разделителем S
# ord(символ) Символ в его код ASCII
# chr(число) Код ASCII в символ
# S.center(width, [fill]) Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
# S.count(str, [start],[end]) Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
# S.lstrip([chars]) Удаление пробельных символов в начале строки
# S.rstrip([chars]) Удаление пробельных символов в конце строки
# S.strip([chars]) Удаление пробельных символов в начале и в конце строки
# Методы строк, которые возвращают булевое значение(True/False):

# a.isdigit() Состоит ли строка из цифр
# a = '43423454'
# print (a.isdigit())

# abvc.isalpha() Состоит ли строка из букв
# abvc = 'FUCK'
# print (abvc.isalpha())



# lcd.isalnum() Состоит ли строка из цифр или букв
# lcd = '4000 rainy nights'
# print (lcd.isalnum())

# S.islower() Состоит ли строка из символов в нижнем регистре
# S.isupper() Состоит ли строка из символов в верхнем регистре
# S.isspace() Состоит ли строка из неотображаемых символов (пробелов, табуляции)
# S.istitle() Начинаются ли слова в строке с заглавной буквы



# Форматирование строк 

# Подстановку данных в строки можно осуществить с помощью форматирования строк:

# методом format:

# format() возвращает отформатированную версию строки, заменяя идентификаторы в фигурных скобках. Идентификаторы могут быть позиционными, числовыми индексами, ключами словарей, именами переменных. Аргументов в format() может быть больше, чем идентификаторов в строке. В таком случае оставшиеся игнорируются.

# name = 'Steve'
# hello = 'fuck you, {}'.format(name)
# print(hello)

# hmf = 'i hate bad  music'
# whatelse = '{},this is full shit '.format(hmf)
# print (whatelse)
 
# результат: i hate bad  music,this is full shit

      # с помощью f’string:

# внутри f-строки в паре фигурных скобок указываются имена переменных, которые надо подставить:


# name = 'John' 
# surname = 'Snow'
# print (f"{name},{surname}")
# name = John, surname = Snow
# результат: John, Snow


# cc = 'Hello, %s!'% 'world'
# print (cc)

# ЭКРАНИРОВАНИЕ  ЭКРАНИРОВАНИЕ   ЭКРАНИРОВАНИЕ   ЭКРАНИРОВАНИЕ  ЭКРАНИРОВАНИЕ  ЭКРАНИРОВАНИЕ  ЭКРАНИРОВАНИЕ ЭКРАНИРОВАНИЕ
# care = 'advice'
# who = ('wear  a glasses\nwhile computing\nits {}, for your health').format(care)
# print(who)

# ТАБУЛЯЦИЯ   ТАБУЛЯЦИЯ   ТАБУЛЯЦИЯ  ТАБУЛЯЦИЯ  ТАБУЛЯЦИЯ  ТАБУЛЯЦИЯ
# care = ' самых лучших'
# who = ('Песня"\n\t я свободен\n\tявляется одной из\n\t {}, песен').format(care)
# print(who)

startswith method
string = 'i love Makers'
print(string.startswith('#'))
