# Записать генерацию строк длины 12, первые 5 символов которой - четные цифры, следующие 5 символов - буквы 'a' - 'z', следующие 2 символа - "AB", если среди первых пяти символов строки есть цифра 8, "XY"  - если нет.

# Строка состоит из слов, разделенных одним или несколькими пробелами. Поменяйте местами наибольшее по длине слово и наименьшее.
# Даны два предложения. Для каждого слова первого предложения определите количество его вхождений во второе предложение.

import random

#
# print(random.randint(97,122))
# #
# # print(ord('a'))
# # print(ord('z')) переводит из буквы в число
# print(chr(109))
# # print(chr(122)) переводит из чсла в букву
#
# f = ""
# for i in range(5):
#     f += str(random.choice(list(range(0, 10, 2))))
#
# for i in range(5):
#     f += chr(random.randint(ord('a'), ord('z')))
#
# if "8" in f:
#     f += 'AB'
# else:
#     f += 'XY'
#
# # print(f)
#
# s = input()
# # print(s)
#
# words = s.split(" ")
#
# d = []
# for i in words:
#     if i != '':
#         d.append(i)
#
#
# print(d)
# # print("/*-/*-/*-/*-".join(d))
#
# mm = [2,1,3,4,5,6,7,8,9,0,10]
#
# max = mm[0]
#
# for i in mm:
#     if i > max:
#         max = i
#
# print(max)
#
# longest = ""            #алгоритм по нахождению максимального слова! Как можно больше абстракций
# max_len = len(words[0])
# longest_index = 0
#
# for i in range(len(words)):
#     if len(words[i]) > max_len:
#         max_len = len(words[i])
#         longest = words[i]
#         longest_index = i
#
# short = ""
# min_len = len(words[0])
# short_index = 0
#
# for a in words:
#     if len(a) < min_len:
#         min_len = len(a)
#         short = a
#

#
# Посмотреть стандартные функции
#
# Методы в os os pass





#
# Песня о бутылках
# number_bootles_of_beer = 99
# while number_bootles_of_beer >= 0:
#     print(number_bootles_of_beer, 'Колличество бутылок пива на стене')
#     print(number_bootles_of_beer, 'бутылок пива')
#     print('Возьми одну, пусти по кругу')
#     number_bootles_of_beer = number_bootles_of_beer - 1
#     if number_bootles_of_beer == -1:
#         print('Нет бутылок пива на стене!')
#         print('Нет бутылок пива!')
#         print('Пойди в магазин и купи ещё (или пойди в магазин и стяни ещё)')
#         print('99 бутылок пива на стене')
