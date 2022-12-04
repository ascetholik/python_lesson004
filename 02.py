# Найдите корни квадртаного уравнения Ax^2 + Bx + C = 0 двумя способами (получить кортеж):
# 1) с помощью математических формул нахождения корней квадратного уравнения 
# 2) с помощбю допольнительных библиотек Python
# D=b^2-4ac. D>0 x1= (-b+sqrt(D))/2a , x2 = (-b - sqrt(D)/2a)    D=0 -b/2a
from math import sqrt 

result = ()
a = int(input('Введите A: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))

diskr = (b**2)-(4*a*c)

if diskr > 0:
  x1 = (-b+sqrt(diskr))/(2*a)
  x2 = (-b-sqrt(diskr))/(2*a)
  result = (x1,x2)
  print(result)
elif diskr ==0:
  x1 = (-1)*b/ (2*a)
  result = (x1,)
  result = tuple(result)
  print(result)
else:
  print('Нет керней')
