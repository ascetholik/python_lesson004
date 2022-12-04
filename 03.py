# Задайти два числа. Напишите программу, котороя найдет НОК (наименшее обшее кратное)
# этих двух чисел

def nok(x,y):
  cout = 1
  if x < b:
    multiBig = y           # переменая для большого числа 
    multiSmall = x         # пременая для меньшего числа

    while multiBig != multiSmall:  
      multiBig = y*cout
      for i in range(1,cout+y):
        multiSmall = x*i
        if multiSmall == multiBig:
          break
      cout+=1
  else:
    multiBig = x
    multiSmall = y

    while multiBig != multiSmall:
      multiBig = x*cout
      for i in range(1,cout+x):
        multiSmall = y*i
        if multiSmall == multiBig:
          break
      cout+=1
  return multiSmall

a = int(input('Введите 1 число :'))
b = int(input('Введите 2 число :'))

print(f'Наименьменьшая общая кратное = {nok(a,b)}')

