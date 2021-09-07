# ORM (Object-relational mapping) - это технология
# программирования, которая позволяет преобразовывать
# несовместимыен типы моделей в ООП, 
# в частности, между хранилищем данных о объектами программирования


# ORM используется для упрощения 
# процесса сохранения объектов 
# в реляционную базу данных и их извлечения 



# import psycopg2 

# connection = psycopg2.connect( #-> \с database name
#       database='practice', 
#       user='aziz',
#       password='1',
#       host='localhost',
#       port='5432'
# )
# print('Database successfuly conected')


# cursor = connection.cursor()

# cursor.execute (
#       '''CREATE TABLE company (
#             id serial PRIMARY KEY,
#             name VARCHAR (100) NOT NULL,
#             city VARCHAR (50) NOT NULL 
#       )
#       '''
# )
# print('Table successfuly created')
# connection.commit()
# connection.close()

# cursor.execute(
#       '''INSERT INTO company(name,city) VALUES ('IBM','Los-ANgeles'),
#       ('Sony','Tokyo'),
#       ('Alipay','Shanghai'),
#       ('Google','London')
#       '''
# )

# connection.commit()
# print('Inserted successfuly')
# connection.close()

# cursor.execute(
#       '''INSERT INTO company (name,city) VALUES ('Samsung','Seoul')
#       '''
# )

# cursor.execute(
#       '''INSERT INTO company (name,city) VALUES ('Volkswagen','Wolfsburg ')
#       '''
# )

# cursor.execute(
#       '''INSERT INTO company (name,city) VALUES ('Bayern','Munchen')
#       '''
# )

# connection.commit()
# print('i diagnose you with gay')
# connection.close()




# print(cursor.fetchall())
# data = cursor.fetchall()
# for item in data:
#       # print(f"id: {item[0]},name: {item[1]}, city: {item[2]}")
#       print(*item) # Распаковка кортежа 
# connection.close()


# cursor.execute(
#       'SELECT name,city FROM company WHERE id=2'
# )

# data = cursor.fetchone()
# print(data)

# cursor = connection.cursor()
# cursor.execute(
#       '''UPDATE company SET city='New-York' where id=1'''
# )
# connection.commit()



# cursor.execute(
#       'SELECT * FROM company ORDER BY  id'
# )
# data = cursor.fetchall()
# for item in data:
#       print(*item)
# connection.close()




# cursor.execute(
#       '''DELETE FROM company WHERE id=3'''
# )

# connection.commit()

# print(f"Total count of deleted: {cursor.rowcount}")

# cursor.execute(
#       '''SELECT * FROM company ORDER BY id'''
# )
# data = cursor.fetchall()
# for item in data:
#       print(*item)
# connection.close()


# ---------------------------------------------------



# from sqlalchemy.sql.sqltypes import Integer

# from sqlalchemy import create_engine
# engine = create_engine('postgresql+psycopg2://aziz:1@localhost:5432/practice') # то же самое что и  /c practice 

# print('database_connected')

# from sqlalchemy import Column,Table, String, MetaData

# metadata = MetaData()
# students_table = Table (
#       'students',metadata,
#       Column('id',Integer, primary_key= True),
#       Column('name',String),
#       Column('last_name',String)
# )


# students_table.create(bind=engine)
# print('Successfuly created table')


# inserted_data = students_table.insert().values(name='John',last_name='Frusciante')

# engine.execute(inserted_data)
# print('successfuly inserted')

# inserted_data = students_table.insert().values(name='Anthony',last_name='Kiedis')

# engine.execute(inserted_data)
# print('successfuly inserted')


# from sqlalchemy import select
# query = select([students_table.c.name,students_table.c.last_name])

# data = engine.execute(query).fetchall()
# for item in data:
#       print(*item)




# from sqlalchemy.sql.sqltypes import Integer

# from sqlalchemy import create_engine
# engine = create_engine('postgresql+psycopg2://aziz:1@localhost:5432/practice')


# from sqlalchemy import Column,Table, String, MetaData

# metadata = MetaData()
# company_table = Table (
#       'company',metadata,
#       Column('id',Integer, primary_key= True),
#       Column('name',String),
#       Column('city',String)
# )

# metadata.create_all(engine)
# class Company:
#       def __init__(self,name,city):
#             self.name = name 
#             self.city = city

#       def __str__(self):
#             return f'Company {self.name} in {self.city} city '


# from sqlalchemy.orm import mapper 
# mapper (Company,company_table)
# print('successfuly created table')







# from sqlalchemy import create_engine
# from sqlalchemy import Column,Table,Integer, String  
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import session
# from sqlalchemy.orm.session import Session

# engine = create_engine('postgresql+psycopg2://aziz:1@localhost:5432/practice')

# Base = declarative_base()

# class Company(Base):
#       __tablename__ = 'company'
#       id = Column(Integer, primary_key= True)
#       name = Column(String)
#       city = Column(String) 

#       def __init__(self,name,city):
#             self.name = name 
#             self.city = city 

      
#       def __str__(self):
#             return f'Company {self.name} in {self.city} city '

# Base.metadata.create_all(engine)
# # print('Table created')

# Session = sessionmaker(bind=engine)
# session = Session()
# sony = Company(name='Sony',city='Tokyo')
# # session.add(sony)
# # session.commit()


# query = session.query(Company.name, Company.city).all()
# print(query)

# from sqlalchemy import create_engine
# from sqlalchemy import Column,Table,Integer, String  
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import session
# from sqlalchemy.orm.session import Session

# engine = create_engine('postgresql+psycopg2://aziz:1@localhost:5432/practice')

# Base = declarative_base()

# class Company(Base):
#       __tablename__ = 'company'
#       id = Column(Integer, primary_key= True)
#       name = Column(String)
#       city = Column(String) 

#       def __init__(self,name,city):
#             self.name = name 
#             self.city = city 

      
#       def __str__(self):
#             return f'Company {self.name} in {self.city} city '

# Base.metadata.create_all(engine)
# # print('Table created')

# Session = sessionmaker(bind=engine)
# session = Session()
# sony = Company(name='Sony',city='Tokyo')
# # session.add(sony)
# # session.commit()


# query = session.query(Company.name, Company.city).all()
# print(query)





# import psycopg2
# from sqlalchemy.engine import result

# connection = psycopg2.connect('dbname=python13_test user=aziz password=1 host=localhost port=5432 ')

# cursor = connection.cursor()

# cursor.fetchall
# cursor.fetchone
# cursor.execute('SELECT * FROM phones where age <30 ;')
# results = cursor.fetchall()
# print(results)
# connection.close()

# phones = {'name': 'Asus Rogue','price':100000, 'category':'notebooks'}
# cursor.execute(
      # 'INSERT INTO phones (name,price,category) VALUES (%(name)s, %(price)s,%(category)s)',phones)
# connection.commit()
# cursor.execute('SELECT * FROM phones;')
# res = cursor.fetchall()
# print(res)
# cursor.close()
# connection.close()






# from sqlalchemy import create_engine

# engine = create_engine('postgresql://aziz:1@localhost:5432/python13_test')

# result = engine.execute(
#       '''SELECT * FROM phones'''
# )

# query = result.fetchall()
# print(query)


# engine.execute('''
#             INSERT INTO phones (name,price,category) VALUES ('Sony Vaio',40000,'notebooks')
# ''')




# import sqlalchemy as db


# engine = db.create_engine('postgresql://aziz:1@localhost:5432/python13_test')

# conn= engine.connect()
# metadata = db.MetaData()


# phones = db.Table('phones',metadata,autoload=True,autoload_with=engine)


# query = db.select([phones]).where(phones.columns.category.like ('notebooks%'))
# res = conn.execute(query)
# results = res.fetchall()
# print(results)







# ORM  

from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, relationship 
from sqlalchemy import Column,Integer,String,ForeignKey,PrimaryKeyConstraint,Numeric
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session, sessionmaker
from  sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://aziz:1@localhost:5432/python13_test')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
      __tablename__ = 'products'
      name = Column(String(50)),
      slug = Column(String(50)),
      primary_key=True)
      phones


class Phones(Base):
      __tablename__ = 'products'
      id = Column(Integer,primary_key=True)
      name = Column(String(50))
      price = Column(Numeric(2))
      category = Column(String,ForeignKey('categories.slug'))
      category = relationship
      ("Category",back_populates='phones')

prod1 = Phones(name='Acer Swift',price=40000,category='notebooks')
session.add(prod1)

prod2 = Phones(name='Acus Tuf gaming',price=100000,category='notebooks')
session.add(prod1)

prod3 = Phones(name='Xiaomi 15s',price=50000,category='notebooks')
session.add(prod1)

session.commit()


session.query(Phones).all()

session.query(Phones).filter(Phones.price > 40000)

session.query(Phones).filter(Phones.name.like('Samsung%'))

session.query(Phones).filter (Phones.price.between(30000,50000))

session.query(Phones).get(id=2):

prod1.price = 50000
session.commit()









