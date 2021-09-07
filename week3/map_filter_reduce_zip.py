# ●  Встроенная в Python функция map() 
# используется для применения функции к каждому элементу итерируемого объекта 
# (например, списка или словаря) и возврата нового итератора для получения результатов.
#  Функция map() возвращает объект map (итератор), который мы можем использовать в других частях нашей программы. 
#  Также мы можем передать объект map в функцию list() или другой тип последовательности для создания итерируемого объекта.

# ●  ФУНКИЦЯ MAP()ПРИНИМАЕТ 2 АРГУМЕНТА.
# ПЕРВЫЙ АРГУМЕНТ ЭТО ФУНКЦИЯ, 
# ВТОРОЙ - ИТЕРИРУЕМЫЙ ОБЪЕКТ.MAP()ПРИМЕНЯЕТ  К КАЖДОМУ
# ЭЛЕМЕНТУ ИТЕРИРУЕМОГО ОБЪЕКТА,ПЕРЕДАННОГО ВТОРЫМ АРГУМЕНТОМ,
# ФУНКЦИЮ,КОТОРУЮ МЫ ПЕРЕДАЛИ ПЕРВЫМ АРГУМЕНТОМ. 



# ● 1) РАССМОТРИМ ФУНКЦИЮ MAP() В КОДЕ, У НАС ЕСТЬ СПИСОК С ЧИСЛАМИ КОТОРЫЙ ИМЕЕТ СТРОКОВЫЙ ТИП ДАНЫХ 
# НАМ НЕОБХОДИМО КАЖДОЕ ЧИСЛО КОНВЕРТИРОВАТЬ В int

# number_str = ['1','2','3','4','5'] # ДЛЯ НАЧАЛА МЫ СОЗДАЕМ СПИСОК number_str С ЧИСЛАМИ КОТОРЫЙ ИМЕЕТ СТРОКОВЫЙ ТИП ДАНЫХ 
             #1   #2  #3    #4
# number_int = list(map(int,number_str))# ● ЧТОБЫ СДЕЛАТЬ ПОСТАВЛЕННУЮ ЗАДАЧУ МЫ ДОЛЖНЫ ИСПОЛЬЗОВАТЬ  map, #2
# print(number_int)
# ● ЧТОБЫ map ВЕРНУЛ СПИСОК МЫ ОБОРАЧИВАЕМ ВСЮ КОНСТРУКЦИЮ В ФУНКЦИЮ Я list (#1)
# ● ЗАКИДЫВАЕМ В map ПЕРВЫМ АРУГМЕНТОМ ВСТРОЕННУЮ ФУНКЦИЮ INT (#3)
# ● А ВТОРЫМ АРГУМЕНТОМ ЗАКИДЫВАЕМ СПИСОК,ПЕРЕМЕННУЮ number_str (#4)


# OUTPUT: [1, 2, 3, 4, 5]


# ● 2) lambda ЭТО АНОНИМНАЯ ФУНКЦИЯ 

# lambda ЯВЛЯЕТСЯ ОДНОСТРООЧНЫМ ВЫРАЖЕНИЕМ И НЕ ИММЕТ НАЗВАНИЯ ПОЭТОМУ ОНА НАЗЫВАЕТСЯ АНОНИМНОЙ 

# ЧАЩЕ ВСЕГО В КАЧЕСТВЕ ПЕРВОГО АРГУМЕНТА ИСПОЛЬЗУЕТСЯ ФУНКЦИЯ lambda 

# numbers = [3,6,9,12,15] # ● ДЛЯ НАЧАЛА МЫ СОЗДАЕМ СПИСОК ЧИСЕЛ
# double_numbers = list(map(lambda x: x *3,numbers)) #МЫ ПЕРЕДАЕМ  B lambda  ПАРАМЕТР = Х 
# print(double_numbers)

# ● ДАЛЕЕ ПОСЛЕ lambda ИДЕТ ТЕЛО ФУНКЦИИ, х*3 ВНУТРИ КОТОРОГО МЫ ПРОПИСЫВАЕМ ИНСТРУКЦИЮ В ДАННОМ СЛУЧАЕ 
# ● МЫ ХОТИМ ЧТОБЫ lambda  УДВОИЛА ЗНАЧЕНИЕ х
# ● МЫ ПЕРЕДАЛИ ФУНКЦИЮ lambda В КАЧЕСТВЕ ПЕРВОГО АРГУМЕНТА 
# ● А В КАЧЕСТВЕ ВТОРОГО АРГУМЕНТА МЫ ПЕРЕДАЕМ СПИСОК ЧИСЕЛ numbers





# ● 3) filter() ОТВЕЧАЕТ ЗА ФИЛЬТРАЦИЮ ИТЕРИРУЕМОГО ОБЪЕКТА. ОНА ПРИНИМАЕТ ДВА АРГУМЕНТА.  
# ● ПЕРВЫЙ - ЭТО ФУНКЦИЯ, 
# ● ВТОРОЙ ИТЕРИРУЕМЫЙ ОБЪЕКТ, 
# ● КОТОРЫЙ НЕОБХОДИМО ОТФИЛЬТРОВАТЬ


# filter ОСТАВЛЯЕТ В ИТЕРИРУЕМОМ ОБЪЕКТЕ ТОЛЬКО ТЕ ЭЛЕМЕНТЫ,
# ДЛЯ КОТОРЫХ ФУНКЦИЯ,ПЕРЕДАННАЯ ПЕРВЫМ АРГУМЕНТОМ ВОЗВРАЩАЕТ ИСТИНУ -TRUE


# strings = ['Makers','MAKERS','BOOTCAMP','bootcamp'] # У НАС ЕСТЬ СПИСОК СО СТРОКАМИ НАДО ОТФИЛЬТРОВАТЬ ЕГО ОСТАВИВ ТОЛЬКО ТЕ В КОТОРЫХ БУКВЫ ВСЕ ЗАГЛАВНЫЕ  
# upper_strings = list(filter(lambda word:word.isupper(),strings))
# print(upper_strings)


# ● ДЛЯ ТОГО ЧТОБЫ ЭТО СДЕЛАТЬ НАМ НЕОБХОДИМО В ФУНКЦИЮ filter 
# ● ПЕРВЫМ АРГУМЕНТОМ ПЕРЕДАТЬ lambda КОТОРАЯ ПРИНИМАЕТ ПАРАМЕТР word
# ● ВНУТРИ ТЕЛА ПОМЕЩАЕМ ВЫРАЖЕНИЕ word.isupper() 



# names = ['john','anthony','Flea','Chad'] 
# filtered_names = list(filter(lambda name: name.startswith('a'),names))
# print(filtered_names)






# ● 4) reduce 






# ● 5) Аннотация типов - это дополнительное описание в классах, 
# функциях, переменных, которое указывает какой тип данных должен быть в этом месте.

# ● 

# def capital(word:str)-> str: # ТУТ МЫ СОЗДАЛИ СПИСОК capital
#       return word.title() # ХОТИМ ЧТОБЫ ФУНКЦИЯ ВЕРНУЛА СПИСОК ТОЛЬКО С ОЗАГЛАВЛЕННЫМИ ПЕРВЫМИ СИМВОЛАМИ
# list_names = ['tommy','ozzy','robert','claus'] #СОЗДАЕМ СПИСОК 
# new_list = list(map(capital,list_names)) 
# print(new_list)


# ● 
# def dollars_to_soms(dollars:int)->int:
#       return f'{round(dollars *84.80)}soms'

# dolalrs=[100,50,20,10,5,1,570]      

# soms = list(map(dollars_to_soms,dolalrs))
# print(soms)




# # ● 6) lambda 
# print((lambda x: x*2)(333))

# OUTPUT: 666


# square = lambda x:x *2 
# print(square(333))

# OUTPUT: 666

# ●
# print((lambda x,y,z:x+y+z)(1,2,3))

# OUTPUT:6

# ●
# В ФУНКЦИИ lambda НЕОБХОДИМО ПЕРЕДАВАТЬ СТОЛЬКО ЖЕ АРГУМЕНТОВ СКОЛЬКО И ПАРАМЕТРОВ

# print((lambda x,y,z:x+y+z)(1,2,))

# OUTPUT: TypeError: <lambda>() missing 1 required positional argument: 'z'




# list1 = [1,2,3]
# list2 = [4,5,6]

# def mani(a,b):
#       return a + b

# new_list = list(map(mani,list1,list2))
# print(new_list)

# 1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# list_ = [1, 2, 3, 4]
# new_list = list(map(lambda x: x+list))

# list1 = [1,2,3]
# list2 = [4,5,6]

# new_list = list(map(lambda x,y: x + y,list1,list2))
# print(new_list)


# ● РАБОТА С ЦИКЛОМ
# num_list = [2,4,6,8,10,12]
# num_list1 = []
# for i in num_list:
#       num_list1.append(i*2)
# print(num_list1)

# OUTPUT: [4, 8, 12, 16, 20, 24]




# ● РАБОТА С list_comprehension 

# num_list = [1,3,5,7,9,11]
# num_list1= [i*2 for i in num_list]
# print(num_list1)

# OUTPUT: [2, 6, 10, 14, 18, 22]


# ● РАБОТА C map + lambda


# num_list = [5,10,15,20,25,30]
# num_list1= list(map(lambda i: i *2,num_list))
# print(num_list1)










# all Iterable - проверяет чтобы все элементы были истинными

# any(iterable)- проверяет чтобы хотя бы один элемент был исттинным 

# a = [0,0,0,0]
# b = (0,0,1,0)

# any(a) #false
# any(b) #True


# bin(number) - возвращает двоичное представление числа

# num = 10 
# print(bin(num))
# OUTPUT: 0b1010


# hex(number) возвращает шестнадцатеричное представление числа
# '0123456789abcdef'
# num = 12
# print(hex(num))
# OUTPUT: 0xa


# oct(number)
# '01234567'
# num=10
# print(oct(num))
# OUTPUT:0o12


# hex_value = '0x12'
# print (int(hex_value,16))



# ord() - принимает символ и возвращает позицию символа 
# ord('a')#97


# dir (оъект) - возвращает спсиок свойств и методов объекта 

# divmod(num1,num2) - возвращает резултат двух операций: num1//num2,num1%num2

# divmode(10,3)-3(3,1)



# eval() - выполняет какое то выражение 

# expr1 = 'print(10)'
# print(eval(expr1))

#   OUTPUT:10

# exec() - может выполнять блоки кода

# loop1 = 'for i in range (1,11)
# :\n\tprint(i)'
# exec(loop1)



# getattr(),hasattr(),setattr(),delattr()


# id(объект) - возвращает адрес объекта в памяти 


# isinstance (объект,класс) проверяет, является ли объект экзмепляром указанного класса 


# type(объект) возвращает тип объекта 


# round округляет  число 







# enumerate(iterable) - пронумеровывает элементы iterable объекта 

# a = ['a','b','c']
# print(list(enumerate(a)))

# OUTPUT:[(0, 'a'), (1, 'b'), (2, 'c')]

# zip(*iterables) - связывает элементы разынх последовательностей 

# a = [1,2,3,4,5,6]
# b = ['john','anthony','flea','chad','smith','stan']
# print(list(zip(a,b)))

# OUTPUT:[(1, 'john'), (2, 'anthony'), (3, 'flea'), (4, 'chad')]





# map(func,iterable)  - применяет функцию к каждому элементу iterable 



# filter(func,iterable) -  фильтрует элементы по определнному условию 

# a = [25,37,45,55,65,43,71]
# b = list(filter(lambda x: x % 5 ==0 ,a))
# print(b)



# reduce нужен для того чтобы брать какой то iterable и сводить элементы в одно значение 
# сумма.произведение.мин.макс.

# from functools import reduce 

# list_ = [1, 2, 3, 4,]
# sum(list_)

# def sum(x,y):
#       return x+y

# res = reduce(sum,list_)
# print(res)





# names = ['john','anthony','flea','chad'] 
# filtered_names = list(filter(lambda name: name.startswith('a'),names))
# print(filtered_names)

























































