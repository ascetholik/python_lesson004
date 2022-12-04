# Считат строку  набора чисел из файла.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.
# Рузультат записать в конец исходного файла (x1, x2)
# 'w' - перезапись/саздает, запись
# 'r' - чтение
# 'a' - дозапись вконец файла
# 'r+' - чтение + дозапись

from pathlib import Path   # Библиотека дла  питу к файлу

# Базовый вариант 

# file = open('test.txt','w')       # создать файл с помошью 'w'
# file.write('Hello world!!!')      # добоить текст в файл
# file.close()                      # ОБЪЯЗАТЕЛЬНО закрыи файл
# ----------------

# file_path = r'test.txt'               # перменая пути файла
# # file_path = Path('f','folder', 'test.txt')
# with open(file_path, 'r') as file:    # открывает и закрывает файл атоматически
#   print(file.read())                  # вывод читат файл

filePath = Path('text','data.txt')
saveFile = Path('text', 'test.txt')
listData = []
listDataInt = []
with open(filePath, 'r') as fileEnter:
  with open(saveFile, 'w') as fileData:
    fileData.write(fileEnter.read())

  with open(saveFile, 'r+') as fileData:
    listData = fileData.read().split(' ')
      # for i in listData:
      #   listDataInt.append(int(i))
    listDataInt = [int(i) for i in listData]     # перевод списка на инт
    max_num = max(listDataInt)
    min_num = min(listDataInt)
    fileData.write(str(f'\nMax = {max_num} Min = {min_num}'))