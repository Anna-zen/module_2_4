# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# нахождение простых чисел
from traceback import print_tb

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range (len(numbers)) :  # в цикле от 0 до последнего элемента в списке
 # print ('i= ', i, 'numbers [i] = ',numbers [i])
  if  numbers [i] > 1 :
     for j in range ( 2, (numbers [i]//2 +1)) : # для делителей от 2 , до половины значения элемента
        # print('j = ', j )

         is_prime = True
         print('Проверяем элемент номер ', i, 'равный', numbers [i], 'на деление на ', j  )
         if numbers [i] > 2 and numbers [i] % j == 0 :
             is_prime = False
             print( 'Число', numbers [i] , ' делится на ' , j )
             not_primes.append (numbers [i])
             print ('добавляем в список не-простых',numbers [i] )
             break
     print ('is_prime = ', is_prime )
     if is_prime == True :
         print('добавляем в список простых', numbers[i])
         primes.append(numbers[i])


print('Список простых чисел', primes)
print('Список не-простых чисел', not_primes)







