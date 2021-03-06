# 1) • Что такое  HTTP 

# HTTP or Hyper Text Transfer Protocol 
# это протокол передачи гипертекста 

# Основная задача HTTP обмен данными между 
# пользовательским приложением и веб-сервером

# -------------------------------------------------------------------------------------------


# 2) • Структура  HTTP Requset (HTTP Запроса )

# 1. строка запроса (Request Line)

# 2. заголовки (Message Headers)

# Пустая строка (разделитель)

# 3. тело сообщения (Entity Body) – необязательный параметр



#                      метод   URI     HTTP версия
# Стартовая строка ->  GET    /shop   HTTP/1.1

                        # Host:texhome.kg  <-- Заголовок

                        # Body  <- тело

# 1) метод - указывает какую операцию нужно осуществить 
# 2) URI - идентфикатор ресурса (путь до конкретного ресурса)
# 3) HHTP версия 




# стартовая строка -> HTTP/1.1 200 OK 

#              server:nginx 
# заголовок    Date:Sun, 20 Dec 2020 11:21;57 UTC 
#              Content-type: application/josn 
#              content-Lenghth:100

#                   тело 
# -------------------------------------------------------------------------------------------


# 3) • Основные методы  HTTP 

# Метод запроса - последовательность из любых символов,
# которая определяет каким образом нужно работать с ресурсом

# 1) GET - используется для запроса содержимого указанного ресурса,
# не изменяя его содержимое

# 2) POST - применяется для передачи
# пользовательских данных заданному ресурсу

# 3) PUT - используются для изменения каких-либо данных на сервере
# полностью изменяет данные 


# 4) PATCH - используются для изменения каких-либо данных на сервере 
# частично изменяет данные 


# 5) DELETE - Удаляет указанный ресурс 



# URI (Uniform Resource Identifier, 
# унифицированный идентификатор ресурса) 
# путь до конкретного ресурса, над которым необходимо
# осуществлять операцию



# 4) • Статусы HTTP





