# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def prime_numbers(n):  # Функция поиска простых чиесел
  a = [2]
  for i in range(3,n+1):
    b = True
    for j in a:
      if i%j == 0:   # Если число делитьна то не добавляеться в список
        b = False
    if b:
      a.append(i)
  return a

def prime_factors(x: int, prime: list ): # разбивание на простые множители
  result = []
  for i in range(len(prime)):
    for j in prime:
      if x%j==0:
        x//=j
        result.append(j)     
  return result

num = int(input('Введите число: '))
primeNum = int(input('Введите конеч границу простых чисел: '))

print(f'Состоить из простых множителей = {prime_factors(num, prime_numbers(primeNum))}')
    
  