                  # Сериализация

# dump(),dumps()

# import json

# info = {
#       "name":"alice",
#       "age": 73,
#       "book":"alchoholism"
# }

# print(type(info))


# with open('info.json','w') as my_file:
#       json.dump(info,my_file)

# json_object = json.dumps(info)
# print(json_object) 
# j

# ------------------------------------------------------------------------------------------------

            # Десериализация

# load(), loads()

# import json 

# with open('info.json') as my_file:
#       python_object = json.load(my_file)
#       print(type(python_object))

# python_object['name'] = 'Claus'
# print(python_object)

# with open('info.json','w') as my_file:
#       json.dump(python_object,my_file)

# ------------------------------------------------------------------------------------------------------------


                        # loads     

# import json  

# json_str = '{"name": "Eddie","age":65,"book":"aint talking bout"}'
# python_object = json.loads(json_str)
# print(json_str)
# print(python_object)
# python_object.update({'color':'red and white'})
# print(python_object)


# ------------------------------------------------------------------------------------------------------------

# import json 

# with open ('HarryPotterBook.json') as my_file:
#       dictionary = json.load(my_file)
#       data = dictionary['books']
#       for book in data:
#             book['author'] = 'J.K.Rowling'
      
# with open ('HarryPotterBook.json','w') as my_file:
#       json.dump(dictionary, my_file)








# import random

# def Hangman():
#  print ('TIME TO PLAY HANGMAN')

# wordlist =['apples', 'oranges', 'grapes', 'pizza', 'cheese', 'burger']
# secret = random.choice(wordlist)
# guesses = 'aeiou'
# turns = 5

# while turns > 0:
#      missed = 0
#      for letter in secret:
#          if letter in guesses:
#              print (letter,end=' ')
#          else:
#            print ('_',end=' ')
#            missed= missed + 1

#      print

#      if missed == 0:
#          print ('\nYou win!')
#          break

#      guess = input('\nguess a letter: ')
#      guesses += guess

#      if guess not in secret:
#          turns = turns -1
#          print ('\nNope.')
#          print ('\n',turns, 'more turns')
#          if turns < 5: print ('\n  |  ')
#          if turns < 4: print ('  O  ')
#          if turns < 3: print (' /|\ ')
#          if turns < 2: print ('  |  ')
#          if turns < 1: print (' / \ ')
#          if turns == 0:
#              print ('\n\nThe answer is', secret)

# playagain = 'yes'
# while playagain == 'yes': 
#     Hangman()
#     print('Do you want to play again? (yes or no)')
#     playagain = input()






# json (JavaScript Object Notation) Формат обмена данными 

# notebook = {
#       'brand':'Acer',
#       'model':'Acpire',
#       'ram': 8,
#       'hdd': 500,
#       'has_type_c':True,
#       'cd_drive':None
# }


# Используются двойные ковычки 
# Ключом может быть только строка


# class Notebook: 
#       def __init__(self,brand,model,ram,hdd,accessories):
#             self.brand = brand
#             self.model = model
#             self.ram = ram
#             self.hdd = hdd
#             self.accessories = accessories

# note1 = Notebook('Apple','Macbook Pro', 16, 256,['headphones','case','mouse','bag'])
# note2 = Notebook('Asus','ROG',24,1000,[])
# notebooks = [note1, note2]
# import json 

# class NoteBooksEncoder(json.JSONEncoder):
#       def default(self,o):
#             return o.__dict__ 

# res = json.dumps(notebooks, indent=2, cls = NoteBooksEncoder)
# print(res)


# notes = '[{"brand":"Acer","model":"Acpire","ram": 8,"hdd": 500,"has_type_c":true,"cd_drive":null},{"brand":"Asus","model":"Zenbook","ram": 8,"hdd": 400,"has_type_c":false,"cd_drive":null}]'

# class Notebook:
#       def __init__(self,brand,model,ram,hdd,has_type_c,cd_drive):
#             self.brand = brand
#             self.model = model
#             self.ram = ram
#             self.hdd =hdd 
#             self.has_type_c = has_type_c
#             self.cd_drice = cd_drive

# import json 

# from collections import namedtuple

# def decoder(notebook_dict):
#       return namedtuple('Notebook',notebook_dict.keys())(*notebook_dict.values())

# notebooks = json.loads(notes,object_hook=decoder)
# print(notebooks)
# print(type(notebooks))
# import json

# students = [
#       {'name':'alisher','age':25},
#       {'name':'Ivan','age': 23}
# ]

# file = open ('test.json','w')
# res = json.dumps(students)
# file.write(res)
# file.close()

# file = open('test.json','w')
# json.dump(students,file)
# file.close




