# Вычислить число c заданной точностью d
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

from math import pi

def accuracy(x: float):
  count = 0
  while x != 1:
    x *=10
    count+=1
  result = int(pi*(10**count))
  result = result/(10**count)
  return result
 
numFloat = float(input('Введите вешествено число точности: '))

print(accuracy(numFloat))
