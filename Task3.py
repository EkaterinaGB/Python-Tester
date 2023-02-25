# Задача №16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#            Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#            В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random
# N = int(input('Введите размер массива N: '))
# X = int(input('Введите число X: '))
# N_array = []
# for i in range(N):
#     N_array.append(random.randint(0, N//2))
# print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')
# print('Некорректный ввод. Попробуйте еще раз!')

# Задача №18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#             Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#             В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# k = int(input())
# m = abs(k - list_1[0]) 

# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# Задача №20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

# dict_with_letter = {1: ("А","Е","В","И","Н","О","Р","С","Т", 
#  'A','E','I','O','U','L','N','S','T','R'), 
#  2: ("Д","К","Л","М","П","У", 
#  'D', 'G'), 
#  3: ("Б","Г","Ё","Ь","Я", 
#  'B','C','M', 'P'), 
#  4: ("Й","Ы", 
#  'F', 'H', 'V', 'W', 'Y'), 
#  5: ("Ж","З","Х","Ц","Ч", 
#  'K'), 
#  6: ("Ш", "Э","Ю", 
#  'J','X'), 
#  7: ("Ф","Щ","Ъ", 
#  'Q','Z') 
#  } 
 
# def dicting(dict_with, words): 
#  sum_points = 0 
#  for key, value in dict_with.items(): 
#   for letter in words.upper(): 
#    if letter in value: 
#     sum_points += key 
#  print(sum_points) 
# word = str(input()) 
# dicting(dict_with_letter,word)