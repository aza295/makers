                  # План урока

# 1) Виды связей 
# 2) Составление отношений между таблицами 
# 3) Что такое  JOIN



                  # Виды связей: 

# Существует три вида связей:


# 1) Один к одному one to one

# Пользователь и профиль (у одного пользователя 
# может быть только один профиль, и к профилю привязан только один профиль)

# 2) Один ко многим  one to many 

# Категория и товары (У товара может быть
# только одна категория, но при этом в одной категории может быть много товаров)

# 3) Многие ко многим many to many 

# Заказы и товары (в одном заказе 
# может быть много товаров, и один товар может заказываться много раз)

# Foreign Key - ограничение, указывающее, что поле ссылается на другую таблицу  


# ------------------------------------------------------------------------------------
                        # JOIN 

# Оператор join нужен для того, 
# чтобы связать таблицы в одном запросе


# 1) INNER JOIN 

# SELECT * FROM phones AS p JOIN categories AS c ON p.category=c.slug;

# 2) LEFT OUTER JOIN 

# SELECT * FROM phones AS p LEFT JOIN categories AS c ON p.category=c.slug;


# 3) RIGHT PUTER JOIN 



# 4) FULL OUTER JOIN





  







#  alter table order_items add constraint fk_orderitems_order FOREIGN KEY (order_id) REFERENCES orders(id);
#  alter table order_items add constraint fk_orderitems_phones FOREIGN KEY (order_id) REFERENCES phones(id);
 







