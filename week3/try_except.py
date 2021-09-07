# try:
#       num1 = int(input('enter number:'))
# except:
#       print('you enter not digit') 


# IF WE ENTER SYMBOL WILL BE
# OUTPUT:you enter not digit

# ●
# TRY
# EXCEPT
# ELSE 
# FINALLY STARTS ANYWAY DOESN'T MATTER THESE THREE WORK OR NOT

# ● 1
# IF WE ENTER NUMBER RESULT WILL BE DIVIDE 12/6

# try:
#       num1=int(input('enter first number:'))
#       num2=int(input('enter second number:'))
#       result = num1/num2
# except:
#       print('division by zero!')
# else:
#       print(result)  
# finally:
#       print('code is end')

# OUTPUT:
# 2.0
# code is end



#  ● 2
# BUT IF WE ENTER SYMBOL WILL BE 
# try:
#       num1=int(input('enter first number'))
#       num2=int(input('enter second number'))
#       result = num1/num2
# except: :
#       print (e)
# else:
#       print(result)  
# finally:
#       print('code is end')


# OUTPUT: you enter not number
#         code is end

#  ● 3
# METHOD EXCEPTION WILL SHOW ALL KIND OF ERRORS IN CODE

# try:
#       num1=int(input('enter first number'))
#       num2=int(input('enter second number'))
#       result = num1/num2
# except: Exception as e:
#       print (e)
# else:
#       print(result)  
# finally:
#       print('code is end')

# OUTPUT: invalid literal for int() with base 10: 'GH'




#  ● 4 USING 2 EXCEPTs in one 

# try:
#       num1=int(input('enter first number:'))
#       num2=int(input('enter second number:'))
#       result = num1/num2
# except ZeroDivisionError:
#       print('division by zero!')
# except ValueError:
#       print('you enter not number')
# else:
#       print(result)  
# finally:
#       print('code is end')



#  ● 5 will explain it later 


# dict_ = dict.fromkeys(('scorpions','wind','somewhere','storm'),0)
# dict_ = {key:len(key)for key,val in dict_.items()}
# dict_.update({'except':'Exception'})
# print(dict_)








# dict_ = dict.fromkeys(('scorpions','wind','somewhere','storm'),0)
# dict_ = {key:len(key)for key,val in dict_.items()}
# dict_.update({'except':'Exception'})
# print(dict_)

# while True:
#       try:
#           key = input(' enter word: ')
#           if key == 'exit':
#                 break
#           dict_[key] += 2
#       except (KeyError,TypeError):
#             print('This key does not exist or can not make concatanation wiyh digits')
#       else:
#             print(dict_[key])
#       finally:
#             print(dict_)




#  ● 6 LISTS

# list_ = [i for i in range (1,31)]

# try:
#     index = int(input('Enter number:'))
#     list_[index] = 'why are you gay ?'
# except IndexError:
#       print('You are out of list range')
# except ValueError:
#       print('invalid literal for int() with base 10:')
# else:
#       print("there's no exception")
# finally:
#       print(list_)


# try:
#     print(makers)
# except NameError:
#       print('you are not make this')



#  ● 7 raise
# ФУНКЦИЯ RAISE ПРЕДНАЗНАЧЕНА ДЛЯ ТОГО ЧТОБЫ СГЕНЕРИРОВАТЬ ОШИБКУ 
#  
# number = int(input('enter number from 1 to zero:'))
# if number not in range(1,71):
#       raise Exception('you enter digit which are not in range')
# print('okey')






# ● ОШИБКИ ЭТО КОГДА НЕПРАВИЛЬНО НАПИСАН КОД, ПРОБЛЕМА В СИНТАКСИСЕ

#   БЫВАЮТ ТРИ ВИДА ОШИБОК

# 1)SYNTAX ERROR
# 2)IDENTATION ERROR - ЭТО ПРОБЛЕМА С ОТСТУПАМИ
# 3)TAB ERROR - ЭТО НЕВЕРНАЯ ТАБУЛЯЦИЯ (СМЕШИВАНИЕ ТАБОВ И ПРОБЕЛОВ)


#  ● ИСКЛЮЧЕНИЯ ЭТО 

#  1) ZeroDivisionError
#  2) NameError (КОГДА НЕ ОБНАРУЖЕНО ИМЯ. НЕ ОБЪЯВЛЕНА ПЕРЕМЕННАЯ)
#  3) TypeError (КОГДА ТИП ОБЪЕКТА НЕ ПОДХОДИТ ДЛЯ ОПЕРАЦИИ)
#  4) ValueError (КОГДА ТИП ОБЪЕКТА ПОДХОДИТ ДЛЯ ОПЕРАЦИИ НО НЕ ЗНАЧЕНИЕ НЕТ)
#  5) IndexError (ЭТО ОБРАЩЕНИЕ К НЕСУЩЕСТВУЮЩЕМУ КЛЮЧУ)      
#  6) KeyError (ОБРАЩЕНИЕ К НЕСУЩЕСТВУЮЩЕМУ КЛЮЧУ)
#  7) ImportError (НЕПРАВИЛЬНЫЙ ИМПОРТ)
#  8) ModuleNotFoundError
#  9) AttributeError (ПОПЫТКА ВЫЗВАТЬ У ОБЪЕКТА НЕСУЩЕСТВУЮЩИЙ АТРИБУТ ИЛИ МЕТОД)


# try except обработка исключений


# dict1 = {'a':1,'b':2}
# random_key ='c'a

# try:
#     res = dict1[random_key]
# except KeyError:
#       res= None

# a = (1,2,3,4,5,6)
# random_index = 8 
# try:
#     res = a[random_index]
# except IndexError:
#     res = 0 
# if  random_index <= len(a) - 1:
#     res = a[random_index]
# print(res)


# assert - для проверки каких то условий,
# если условие не выполняется, возникает AssertionError



# raise - ОПЕРАТОР ДЛЯ ГЕНЕРАЦИИ ИСКЛЮЧЕНИЙ





# number = int(input('enter number from 1 to zero:'))
# if number not in range(1,71):
#       raise Exception('you enter digit which are not in range')
# print('okey')







# if temperature > 100:
#       raise ValueError(Температура не должна превышать 100 градусов)



# 3) Напишите программу которая будет получать два числа через input и делить одно на другое. 
# Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.




# numbers = int(input('Введите число:'))
# numbers2 = int(input('Введите число:'))
# try nu

# 4) Напишите программу, которая будет получать через инпут 
# 2 числа и будет печатать их сумму. Обработайте ошибку, 
# которая возникнет, если пользователь введёт не числовое значение и выведите сообщение.


# """
# 5) Дан словарь. Попытайтесь получить значение по ключу. 
# Обработайте ошибку, возникающую в том случае, если запрашиваемый ключ не существует.
a = ['slipknot','korn','Dmajor','ibanezz']
b = ['rhcp','offspring','green day']
print(b,a)