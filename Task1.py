# Задача №2 : Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# n = input("Введите трёхзначное число: ")

# a = int(n[0])
# b = int(n[1])
# c = int(n[2])
 
# print("Сумма цифр числа:", a + b + c)

# или

# num = input('Введите трёхзначное значное число: ')
# res = 0
# if len(num) == 3:
#     for i in num:
#         res += int(i)
#     print(res)
# else:
#     print('Вы ввели не трёхзначное значное число')

# Задача №4 : Петя, Катя и Сережа делают из бумаги журавликов. 
#             Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
#             если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#             а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# a = int(input("Введите количество журавликов: "))
# k = int((a/3)*2)
# p = int((k/2)/2)
# s = int(p)
# print(p, k, s)

# s = int(input("Введите количество журавликов: "))
# print((s//6), ((s//6)*4), (s//6))


# Задача №6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#            Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#            Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# t = input('Введите номер билета: ')
# l = int(t[0]) + int(t[1]) + int(t[2])
# r = int(t[3]) + int(t[4]) + int(t[5])
# if l == r:
#     print('Yes')
# else:
#     print('NO')

# Задача №8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#            если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# n,m,k = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
# if k%n == 0 or k%m == 0:
#     print('Yes')
# else: print('No')














