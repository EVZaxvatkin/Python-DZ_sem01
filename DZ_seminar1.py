from random import randint


#1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#Дано a, b, c - стороны предполагаемого треугольника.
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

#input("Введите длины сторон треугольника: ")
#a = int(input("Сторона а: "))
#b = int(input("Сторона b: "))
#c = int(input("Сторона c: "))
#if a<b+c and b<a+c and c<a+b:
#    print("Треугольник существует")
#    if a != b and a != c and b != c:
#        print("Разносторонний треугольник")
#    elif a == b == c:
#        print("Равносторонний треугольник")
#    elif a==b or a==c or b==c:
#        print("Равнобедренный треугольник")

#else:
#    print("Треугольник не существует")


#2 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

#n = int(input("Введите число от 1 до 100 000: "))

#count = 0

#for i in range(2, n+1):
#    if (n % i == 0):
#        count += 1
#if (count <= 0):
#    print("Число простое")
#else:
#    print("Число не является простым")

#3 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#Для генерации случайного числа используйте код:
#from random import randint
#num = randint(LOWER_LIMIT, UPPER_LIMIT)

#LOWER_LIMIT = 0
#UPPER_LIMIT = 1000

#num = randint(LOWER_LIMIT, UPPER_LIMIT)
#search_num = None
#count = 10

#while count != 0:
#    my_num = int(input("Угадайте число: "))

#    if my_num == num:
#        print("Вы угадали число")

#    elif my_num < num:
#        print("Искомое число больше")

#    elif my_num > num:
#        print("Искомое число меньше")

#    count-=1

#    if count == 0:
#        print("Попытки кочились, попробуйте в следующий раз")









