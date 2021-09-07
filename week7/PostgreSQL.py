# 1) Что такое база данных 

# База данных (БД) - Это организованная структруа данных,
# Предназначенная для хранения, изменения и обработки 
# взаимосвязанной информации,преимущественно больших объемов


# Баз данных активно используется для динамических сайтов 
# со значительными объемами данных чаще всего интернет магазины 
# порталы, и корпоративные сайты



# Проще говоря база данных это хранилище данных 


# -------------------------------------------------------------------------------------------------------------------
# 2) Что такое SQL 

# SQL (Structure Query Language) - Это язык запросов, 
# который испольузется в качестве эффективного способа
# сохранения данных, поиска их частей, обновления,извлечения
# и удаления из базы


# ● SQL помогает управлять огромными данными эффективно, 
# то есть быстро получать расчеты на их основе 

# ● SQL Запросы могут быть простыми и вложенными 

# ● SQL-Программа состоит из последовательности команд
# команда представляет собой последовательность компонентов,
# оканчивающуюся точкой запятой ;

# ● В SQL есть свои типы данных 

# 1) Numeric types

# smallint 

# int 1

# bigint 

# decimal 

# numeric 

# real 1

# double precision 

# smallserial 

# serial  1

# bigserial 


# 2) Character Types

# CHAR строки с постоянной длинной 
# CHAR(10) test ->'test      '
# character varying(n)
# 
# varchar(n)
# varchar (10) test -> 'test'
# строки с максимальной длинной 

# character(n),char(n)

# text 

# 3) Boolean type
 
# boolean

# 4) Monetary Types

# money


# 5) Enumarate types
# 
# CREATE TYPE mood AS ENUM ('sad','ok','happy')

# enum - ограничение вариантов выбора 


# 6) Data/Time Types 

# timestamp 
# (дата и время) 
 
# timestamp 

# date
# дата
#  
# time
# время

# time 

# interval

# (временной промежуток)

# -------------------------------------------------------------------------------------------------------------------


# 3) СУБД 

# СУБД (Система управления базами данных) 
# - это комплекс програмнных средств, 
# необходимых для создания структуры данных новой базы, 
# ее наполнения,редактирования содержимого и отображения информации 

# -------------------------------------------------------------------------------------------------------------------


# 4)PostgreSQL

# Почему PostgreSQL:
 
# PostgreSQL - самая продвинутая функциональная СУБД 

# 1) У PostgreSQL Больше функций 

# 2) PostgreSQL - Расширяемая система, ее работа базируется на каталогах

# 3) PostgreSQL - Это объектно -реляционная система,
# которая совместима с принципами ACID

# ● atomicity - атомарность 

# ● consistency - согласованность

# ● isolation - изолтрованность

# ● durabillity - стойкость



#                  Характеристики PostgreSQL 
  
# 1) Открытый исходный код 

# 2) Расширенные настройки 

# 3) Долгая история 

# 4) Частые обновления 

# 5) Либеральная открытая лицензия 

# 6) Функции MVCC

# 7) Отзывчивое сообщество 

# 8) Высокая оценка пользователей 




#      Основные преимущества PostgreSQL для разработчиков 

# ● ОРСУБД, а не просто РСУБД 

# ● Отлично подходит для сложных запросов 

# ● Поддержка NoSQL и большое разнообразие типов данных 

# ● Спроектирована для управления очень большими базами данных 

# ● Управление Параллельным доступом посредством многоверсионности  
# (MVCC)

# ● Соответствие ACID

# -------------------------------------------------------------------------------------------------------------------


# Существует много типов баз данных 

# ● 1) Иерархическая 
# -------------------------------------------------------------------------------------------------------------------

# ● 2) Объектно и объектно-ориентированная 
# -------------------------------------------------------------------------------------------------------------------

# ● 3) Реляционная 

# 1) Отличительной чертой реляционных баз данных является 
# возможность построения отношений между таблицами в базе данных
# т.е таблицы могут иметь связи между собой 


# 2)  Нереляционные базы данных не имеют отношений между таблицами 
# и состоят из модели коллекции и модели документа,
# в которых данные хранятся по типу ключ и значение 

# -------------------------------------------------------------------------------------------------------------------

# ● 4) Объектно-реляционная 
# -------------------------------------------------------------------------------------------------------------------

# ● 5) Сетевая
# -------------------------------------------------------------------------------------------------------------------

# ● 6) Функциональная

# -------------------------------------------------------------------------------------------------------------------


                        # Команды 

# ● Чтобы войти в postgres  sudo -u postgres psql

# ● Создать базу данных - create data base название (БД);

# ● Чтобы удалить базу данных - drop database название(БД);

# ● Создание таблицы - create table (поля,столбцы)

# ●  

# ● Подключть одну(БД) к другой - \c название базы данных

# ● Чтобы увидеть какие имеются таблицы - \d or \dt

# ● Чтобы увидеть(узнать) какие баззы данных имеются - \l 

# ● Показать список всех users - \du

# ● Создать нового user - create user имя пользователя with password '';

# ● select * from name_of_table;

# ● Дать права опредленному пользователю 
# alter role имя пользователя with (какие права мы даем) superuser;
# alter role aza1 with superuser;
 

# ● Дать все привилегии 

# grant all privileges on database name_of_database to name_user

# grant all privileges on (имя базы данных) to (имя пользователя)

# ● Создать базу данных с определенным пользователем

# create database name_of_database with owner name_user

# create database (имя базы данных) with owner (имя пользователя)

# ● Изменение структуры таблицы - alter table 

# ● переименование таблицы 

# alter table название таблицы rename to новое название 

# ● Удаление таблицы - drop table название таблицы 

# ● добавление столбца в таблицу 
#- alter table название таблицы add column название столбца 
# тип_столбца

# ● удаление столбца из таблицы  
# alter table название таблицы drop column название столбца

# ● переименование столбца 

# alter table название таблицы rename column  название столбца to новое_название 

# ● Изменение типа 
# - alter table название таблицы alter column название столбца set data type  новый тип

# ● Установка или снятие значений по умолчанию 
# alter table название таблицы alter column название столбца set/drop default  значение 

# ● Установка или снятие not null 

# alter table название таблицы alter column название столбца set/drop not null 


# ● Установка ограничений 

# alter table  название таблицы add constraint название ограничения unique/check/...(столбец);

# SELECT,INSERT,UPDATE,DELETE 

# insert - добавление записей  

# insert into название таблицы (поля) values (запись1),(запись2);

# select  * from название таблицы; 

# update 

# delete


# alter table products add constraint price_check check (price > '0.00');

# -------------------------------------------------------------------------------------------------------------------

                        # CONSTRAINSTS
                        # (Ограничения) 
                        

# ● NOT NULL Constraint (важное) 

# ● UNIQUE Constraint - может ли значение в столбце повторяться 

# ● PRIMARY Key - определяет, какой столбец будет 
# идентификатором

# ● FOREIGN Key (важное) - ссылка на другую таблицу

# ● CHECK Constraint - Проверяет значение на определенное условие   

# ● EXLUSION Constraint 

# ● Default Constraint - Значение по умолчанию



# -------------------------------------------------------------------------------------------------------------------

                  # Создание таблиц 

# create table name_of_table


# test_user=# create table Person(
# test_user(# id serial primary key,
# test_user(# name varchar(50) NOT NULL,
# test_user(# last_name varchar(100) ,
# test_user(# age int) 


# -------------------------------------------------------------------------------------------------------------------

                  # Заполнение таблиц,
            # отправка простых запросов 

# 1) числовые
 
# целые числа:
# smallint (2байта)
# -32768 до 32676

# int(4 байта)
# -2_147_484_648 до 2_147_483_647

# bigint(8 байтов)
# -9_223_372_0366_854_775_808 
# до 9_223_372_0366_854_775_808

# insert into (name_of_table) (id,name,last_name)

# целые числа с автоувеличением
# smallserial (2байта)
# 1 до 32767

# serial (4 байта)
# 1 до 2_147_483_647

# bigserial (8 байтов)
# 1 до 9_223_372_0366_854_775_808


# чисс плавающей точкой (float)

# real

# money  дробное число с точностью 2 знака после запятой 
#  





# insert into person (name, last_name )values ()


# select name, age from person;


# select * from person where age > 30


# create table info(id serial primary key,
# name varchar(50) not null,
# last_name varchar(100),
# age int,
# Country varchar(50) not null, 
# email varchar(50) not null, 
# programming_language varchar(50) not null,
# experience int not null);




















