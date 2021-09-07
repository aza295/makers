# a = True
# print (type(a))


#Логические операторы
# > (больше), < (меньше), >= (больше или равно), <= (меньше или равно), == (равно), != (не равно).

#Если результатом вычисления  выражения может быть лишь правдда или ложь то такое выражение называется логическим

# работая с логическими выражениями мы используем  булевой тип данных у которого только  2 значения 

#  false приравнивают к нулю
#  True приравнивают к единице

# if elif else structure 

# rule = input ('how old are you?')
# age = 18
# if (age > 22):
#     print ('you can enter')
# elif (age >18, and,  <22):
#     print ('you can enter with adults')
# else (age <18):
#     print ('you can not enter')
 
# print(4 < 3) and (5>6)

#ord
# print ('makers'> 'bootcamp')
# print (ord('m'))

# print (chr(109))

# and, or
 
# Чтобы получить  true  используя  and необходимо чтобы результаты обоих простых выражений были true or false
# a = 15
# b = 25
# print (a >= 15 and b < 30)

# a = 15
# b = 25
# print (a > 15 and  b <30 )

# or command
# a = 15
# b = 25
# print (a == 15 or b > 30)

# Not
# x = 20
# print (not x == 10 )

# a = True
# b = False 
# print (not a)
# print(not b)



# rule = input ('how old are you?')
# age = 19
# if (age > 22):
#     print ('you can enter')
# elif (age >18  and age <22):
#     print ('you can enter with adults')
# else:
#     print ('you can not enter')


   
# null_variable = None
# not_null_variable = 'MAKERS'

# if null_variable is None:
#       print ('This is none')
# else:
#       print ('This is not None')

# print (id(null_variable))



# rule = input ('how old are you?')
# age = int(input("Ваше число: "))
# if (age > 22):
#     print ('you can enter')
#     print ('you can enter with adults')
# else:
#     print ('you can not enter')


#Условные и логические операторы

# сравнение 
# проверка
#
# #  '' < "+"
# '+'' <' 0' 
# '0' < 'A' 
# 'A' < 'a' 
# 'z' < '{'
# '{' < '~'     

# ann < annabel
# abc < abd 

# проверка 
# in -  прверка на вхождение
# is -  является ли 
# isinstance() проверяет относится ли объект к определнному классу 

# a = 4 
# isinstance ( a< int)


# issubclass()  (класс1) (класс2) проверяет являетсся ли класс1 потомком класса2 

# a = 5 
# b = 5
# a is b
# id(a) == id(b)

# a = none 
# a == none 

#  Методы проверок

# isdigit() islower() isdecimal()

# приведение  в bool 
# bool (0) #false
# bool (None) #false
# bool ('') #false
# bool ([]) #false
# bool (()) #false
# bool ({}) #false
# bool (set()) #false

# bool (-1) #True
# bool (10) #True
# bool ('') #True
# bool (1.2) #True

# if  условие 
#       действие 

# number = 20 
# if number > 15:
#       print('BYOB`)

# A = 'atwa'
# if 'e' in a:
#       print ('yes')


# b = 'Hello wolrd '
# if b.isalpha ():
#       c = 'good'
# списки обозначаются []

# al = [1,2,3,4]

# if len (al)> 0:
#       print('sugar')

# if bool (al):
#       print('wocao')


# if al:
#       print ('chifan')
      
# dhp_exp = 195
# if dhp_exp <105:
#       print ('IEAIEAO')
# else :
#       print ("bad boys ")

# temperature = 40

# if temperature < 18:
#       print ('it is cold')
# else:
#       if temperature < 28:
#           print ('it is good')
#       else:
#             if temperature < 35:
#                 print ('hot')
#             else: ('too hot')

#  вместо этого можно написать elif
# if temperature < 18:
#     print('cold')
# elif temperature < 28:
#     print ('normal')
# elif temperature < 35:
#     print ('hot')
# else:
#     print('too hot')

# mark = int(input(введите оценку от 1 до 100))
# 0 - 60 -> 2
# 61 - 75 -> 3
# 76 - 84 -> 4
# 85 - 100 -> 5

# if mark < 61:
#       result = 2
# elif mark < 75 :
#       result = 3
# elif mark < 84:
#       result = 4
# else:
#       result = 5
# print (result)


# x = 20 

# while True:
#     number = int(input('enter number'))
#     if x == number:
#           print ( 'you win!')
#           break
#       print ('попробуйте снова')


# ЛОГИЧЕСКИЕ ОПЕРАТОРЫ



# and 
# or
# not

# false and false #False
# true and false # false
# false and true# false
# true and true # true

# false or false #false
# true or False#true
# false or true #true
# true or true #true

# not true #False
# not falase# True


# How and works 
#  temperature = 100 
#  oressure = 5

#  if temperature > 80 and presssure >3:
#        print ('reaction on')

# time = 16.00

# if time < 15  or time > 18:
#       print ('work time')


# has_car = False 

# if not has_car:
#       print('you  can not go outside')

# color = input ('whuich color you want ?')

# match color:
#       case "red":
#             print ("ok,red")
#       case ' black':
#             print ('nice choice')
#       case 'black':
#             print ('awesome')
#       case _:
#             print ("Sorry we can't color into this color") 

# # ('red', 'black', 'yellow')




# if color == 'red':
#       print ('ok,red')
# elif color == 'white':
#       print ('nice choice')
# elif color == 'black':
#       print ('awesome')
# else : 
#       print ("we can't color in this")

# калькулятор на основе dict  
# number = int(input('enter first number'))
# number2 = int (input('enter second number'))
# choice = input ('choose - + % / // **')

# if choice == '/' and number2 == 0:
#     print ('целое число нельзя делитть на 0')

# dict_ = {
#       '+': number + number2,
#       '-': number + number2,
#       '*': number + number2,
#       '/': number + number2,
#       '%': number + number2,
#       '//': number + number2,
#       '**': number + number2,
# }      

# print (dict_.get(choice))


# pow (x,y [z]) 
# pow (9,3)


# mark = int (input('введите вашу оценку'))
# if mark  >= 90:
#       print ('Отлично ваша оценка 5')
# elif mark  >= 80:
#       print ('Здорово ваша оценка 4')
# elif mark  >=70:
#       print ('Здорово ваша оценка 3')
# elif mark  >= 60:
#       print ('Вам стоит подучить материал')
# else: 
#       print('Вы не сдали Экзамен')


# x = 7
# if x >= 5 and  x <= 5:
#       print('true' or 'false')
# if x <= 5:
#       print ('false')

# a = (input(18)

# b = (input(9)

# c = (input(7)

# if a == b == c:
#    print(3)
# elif a == b or b == c or a == c:
#    print(2)
# else:
#    print(0)

# back = "in black"

# if len('back') >= 5:
#     print('true')
# elif len ('back')<= 5:
#       print ('false')
# else:
#       print ('back')

# a = int(10)
# b = int(2)
# c = int(6)

# if a == b == c:
#    print(3)
# elif a == b or b == c or a == c:
#    print(2)
# else:
#    print(0)


# back = "in black"
# x = '1'

# if x == '-1':
#     print('negative')
# elif x == '1':
#       print ('positive')
# else:
#       print ('zero')


# b = 'in back'
# print (len('in black'))

# a = int(input(35))
# b = int(input(25))
# if a < b:
#       print(a)
# else:
#       print (b)


# a,b,c = int(input(25)),int(input(50)),int(input(37))
# if b >= c and c >= a:
#       print (a)
# elif a >= c and b <= a:
#       print (b)
# else:
#       print (c)

# a = int(input(678))
# b = int(input(23))
# if a%b == 0:
# print (a%b)
# else:
# print(%a не делится на %b % (a,b))
# print(Остаток, %d % (a%b))
# print(Частное, %d % (a//b)) 678
# 23
# 678 не делится на 23
# Остаток: 11
# Частное: 29

# 678
# 3
# 678 делится на 3
# Частное: 226


# year = int(input(2022))

# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# if a<=n<=z or A<=n<=Z:
#     print('Это буква', chr(n))
# else:
#     print('Это не буква, а символ', chr(n))

#     1
# 2
# 3
# 4

# x1 = int(input(4))


# y1 = int(input(2))


# x2 = int(input(4))


# y2 = int(input(8))

# if x1 == x2 or y1 == y2:
#     print('YES') 
# else:
#     print('NO')

x1 = int(input(4))
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')