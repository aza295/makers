# 1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# """
# list_ = [1, 2, 3, 4,]
# sum(list_)

# def sum(x,y):
#       return x+y

# res = reduce(sum,list_)
# print(res)

# from functools import reduce 
# list_ = [1, 2, 3, 4,]
# list2 = reduce(lambda x,y:x+y,list_)
# print(list2)


# 2) Дан списка из чисел. Проверьте, что все числа больше трёх.

# a = [1,2,3,4,5,6]
# b = list(filter(lambda x: x >3 ,a))
# print(b)




# 3) Дан список из чисел. Проверьте, что в нём есть отрицательные числа.




# a = [-1,-2,-3,-4,-5, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = list(filter(lambda nums: nums < 0 ==0 , a))
# print(b)



# 4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.

# a = [1,2,3,4,5,6]
# b = list(map(lambda x: x **2 ,a))
# print(b)





# 5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.






# z = [2,5,7,8,13,16,27] # создаем список z 
# filtered_values = list(filter(lambda x:x %2==0,z)) #создаем новую переменную куда будем вкладывать отфильтрованные значения 
# print(filtered_values)
# """
# 6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.




# names = ['Sebastian','David','Eddie Van Halen','Wolfgang','Wangshengli']
# filtered_names = list(filter(lambda y: len(y)>7,names)) #
# print(filtered_names)
# """
# 7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
# 
# from functools import reduce

# list_ = [5, 6, 7, 8] # создаем список
# b = reduce(lambda y,z: y+z,list_) # reduce принимает два аргумента 
# print(b)


# 8) Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.




# a = [24,19,8,3,39,13,17]

# odd = list(filter(lambda x: x % 2 != 0, a))
# even = list(filter(lambda x: x % 2 == 0, a))

# print(f'{len(odd)} odd numbers, {len(even)} even numbers')




# 9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .

# НЕ ПОНЯЛ НАДО РАЗОБРАТЬ 

# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# filtered_values = list(map(lambda x,:x >0== False,list_))
# print(filtered_values)








# 10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.


# from functools import reduce

# list_ = [-1, 2, 3, 0, 5, -3, ]
# b = reduce(lambda y,z: y if y>z else z,list_) # reduce принимает два аргумента 
# print(b)




# from functools import reduce # first step import reduce 
# list_ = ['Stan','Butters','Kenny'] # creating a list
# name = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(name)






