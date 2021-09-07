# Основные команды, которые необходимы при работе с данными:
# SELECT,INSERT,UPDATE,DELETE


# 1) SELECT - команда для получения строки из таблицы 

# select name, price_per_piece from products;


# 2) INSERT - используется для добавления строки в таблицу 

# insert into products values ('tomatoes',10,2);

# 3) UPDATE - используется для изменения строки в таблице 

# update products set price_per_piece=20 where name='Apples';

# 4) DELETE - используется для удаления записи

# delete from products where name='Stawberry'

# 5) ALTER TABLE - используется для добавления столбца
# 
# Alter table products add origin varchar(50) default 'kg/Bishkek';


# Фильтрация 

# операции для фильтрации 

# 1) операция сравнения 

# = равенство
# !=, <> неравенство
# > more
# < less 
# >= more or equal
# =< less or equal 



# and, or, not 

# сортировка нужна для отображения записей в указанном порядке 





            # ● С ПОМОЩЬЮ КОМАНДЫ ALTER TABLE МОЖНО:

# 1 Добавлять новые столбцы 

# 2 Переимеовывать стобцы 

# 3 Удалять столбцы 

# 4 Добавлять ограничения 

# 5 Убирать ограничения


# ALTER TABLE: Работа со столбцами внутри таблицы


# ● select name, last_name from info; 


# OUTPUT: BoratSagdiev

# ||' '|| конкатенация в таблицах

# ● select name ||','||last_name from info;

# OUTPUT: Borat,Sagdiev

# ● select name ||' '||last_name from info;

# OUTPUT: Borat Sagdiev

# ● select name ||' '||last_name from info;

# OUTPUT: Borat Sagdiev



# ● select name ||' '|| last_name from info;
#        ?column?       
# ---------------------
#  Borat Sagdiev



# ● Задать имя столбца 

# select name ||' '|| last_name as full_name from info;
#       full_name      
# ---------------------
#  Borat Sagdiev


# ● Получить имя столбца без символов underscore
# Имя столбца надо помсестить в двойные ковычки 


# select name ||' '|| last_name as "full name" from info;
      # full name 


# DISTINCT - избавляется от дубликатов

# ● Избавялется от всех повторяющихся значений

# select distinct age from info;


# ● Чтобы получить все имена которые начинаются на А
#  
# select * from info where name like 'А%';


# ● Чтобы получить все email которые заканчиваются на gmail.com

# select * from info where email like '%gmail.com';

# ● Чтобы получить все имена в которых есть буква а

# select * from info where name like '%a%';


# -------------------------------------------------------------------------------------------

# ● SQL-Программа состоит из последовательности команд
# команда представляет собой последовательность компонентов,
# оканчивающуюся точкой запятой ;


                  # ● Компонент команды:

# Компонентом команды может быть ключевое слово,
# идентификатор,идентификатор в кавычках,
# строка,специальныцй символ.  


# SELECT * FROM my_table

# SELECT - это ключеове слово 

# * - это специальный символ 

# FROM - это ключевое слово

# my_table - это идентификатор


# ● Идентификаторы определяют имена таблиц,
# столбцов или других объектов баз данных. 
# Поэтому иногда их называют просто << Именами>>









